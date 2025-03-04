# Use a lightweight Python image
FROM python:3.10-slim  

# Set the working directory
WORKDIR /app

# Install system dependencies (needed for database libraries)
RUN apt-get update && apt-get install -y gcc libpq-dev && rm -rf /var/lib/apt/lists/*

# Copy project files
COPY . /app/

# Set up a virtual environment
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Install dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt --no-cache-dir

# Collect static files (important for Railway)
RUN python manage.py collectstatic --noinput || true

# Migrate database (to apply migrations automatically)
RUN python manage.py migrate || true

# Expose port 8000 (needed for Railway)
EXPOSE 8000

# Start Django application
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "exstore.wsgi:application"]