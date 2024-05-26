# Use an official Python runtime as a parent image
FROM python:3.11

# Set environment variables
ENV PYTHONUNBUFFERED 1

# Install Node.js and npm
RUN apt-get update && apt-get install -y \
    nodejs \
    npm

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
# RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entrypoint script into the container
COPY docker-entrypoint.sh /app/

# Make the entrypoint script executable
RUN chmod +x docker-entrypoint.sh

# Copy the rest of the application code into the container
COPY . .

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define the entrypoint script as the default command to run when the container starts
ENTRYPOINT ["./docker-entrypoint.sh"]