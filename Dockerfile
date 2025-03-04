# Use a lightweight Python image
FROM python:3.10-slim  

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y gcc libpq-dev && rm -rf /var/lib/apt/lists/*

# Copy project files
COPY . /app/

# Set up virtual environment
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Install dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt --no-cache-dir

# Collect static files (if using Django)
RUN python manage.py collectstatic --noinput || true

# Expose the application port
EXPOSE 8000

# Run Django application with Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "exstore.wsgi:application"]