FROM python:3.11-slim

WORKDIR /app

# Copy your Flask app
COPY app.py .

# Install dependencies
RUN pip install --no-cache-dir flask

# Expose the app port
EXPOSE 5000

# Run the service
CMD ["python", "app.py"]
