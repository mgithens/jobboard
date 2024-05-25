# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the requirements file into the container
COPY requirements.txt /usr/src/app/

# Install any needed packages specified in requirements.txt
RUN pip3 install --upgrade pip
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the entrypoint script into the container
COPY docker-entrypoint.sh /usr/src/app/

# Make the entrypoint script executable
RUN chmod +x docker-entrypoint.sh

# Copy the rest of the application code into the container
COPY . /usr/src/app

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define the entrypoint script as the default command to run when the container starts
ENTRYPOINT ["./docker-entrypoint.sh"]