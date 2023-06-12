ARG PYTHON_VERSION=3.11.3

FROM python:${PYTHON_VERSION}-slim-buster

LABEL maintainer="Asaf Ben-Menachem <asafbenmenachem@gmail.com>"

# Set working directory
WORKDIR /app

# Copy and install packages
COPY requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY app/ /app/app

# Create the appUser
RUN useradd -m appUser

# Create the logs directory and set ownership and permissions
RUN mkdir -p /app/logs/app_logs \
    && chown -R appUser:appUser /app/logs/app_logs \
    && chmod -R 775 /app/logs/app_logs

# Give the appUser permissions to write to the system_data files
RUN mkdir -p /app/system_data \
    && chown -R appUser:appUser /app/system_data \
    && chmod -R 755 /app/system_data

# Change ownership and permissions of the working directory
RUN chown -R appUser:appUser /app \
    && chmod -R 755 /app

# Switch to non-root user
USER appUser

# Expose the port
EXPOSE 8050

# Run the application using Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8050", "app.main:server"]