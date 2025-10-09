# Dockerfile

# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /code

# Copy the local directory contents into the container at /code
# This will copy the 'app' and 'tests' folders
COPY . .

# --- Optional: If you had a requirements.txt file, you would install it here ---
# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

# Run the command-line interface (cli.py) as a module within the 'app' package
# This is the correct way to run a file inside a Python package.
CMD ["python", "-m", "app.cli"]