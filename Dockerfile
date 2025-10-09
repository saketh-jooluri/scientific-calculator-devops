#  Dockerfile for Scientific Calculator

# Use lightweight Python base image
FROM python:3.12-slim

# Set working directory inside container
WORKDIR /app

# Copy all project files into container
COPY . /app

# Upgrade pip and install dependencies if any
RUN python -m pip install --upgrade pip && \
    if [ -f requirements.txt ]; then pip install -r requirements.txt; fi

# Run unit tests during build (optional but good for CI)
RUN python -m unittest discover -v -s tests || true

# Default command — run the CLI calculator
CMD ["python", "-m", "app.cli"]
