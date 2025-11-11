# Dockerfile

# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /code

# Copy the local directory contents into the container at /code
# This will copy the 'app' and 'tests' folders
COPY . .

# Run the command-line interface (cli.py) as a module within the 'app' package
CMD ["python", "-m", "app.cli"]