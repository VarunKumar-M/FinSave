# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy code
COPY . .

# Expose port (make sure it matches your FastAPI port)
EXPOSE 8001

# Run app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]
