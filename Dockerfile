FROM python:3.11.3-slim-buster

LABEL maintainer "Asaf Ben-Menachem, asafbenmenachem@gmail.com"

# Copy and install packages
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt \
    && rm requirements.txt


# Copy all files to the docker image
COPY app/ /app


# Create the appUser
RUN useradd -m appUser

# Create the logs directory and set ownership and permissions
RUN mkdir -p /app/logs/app_logs \
    && chown -R appUser:appUser /app \
    && chmod -R 775 /app

# Give the appUser permissions to write to the system_data files
RUN mkdir -p /app/system_data \
    && chown -R appUser:appUser /app/system_data \
    && chmod -R 755 /app/system_data

# Changing to non-root user
USER appUser


# Run the application using Gunicorn
CMD gunicorn --bind 0.0.0.0:8050 app.main:server