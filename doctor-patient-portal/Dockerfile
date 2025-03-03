# Dockerfile
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN apt-get update && apt-get install -y \
    gcc \
    postgresql-client \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project
COPY . .

# Make sure manage.py is executable
RUN chmod +x /app/src/manage.py

# Add the project root to PYTHONPATH
ENV PYTHONPATH=/app:$PYTHONPATH

# Update the command to use the correct path
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--chdir", "/app/doctor-patient-portal/src", "portal.wsgi:application"]