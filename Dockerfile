# Use an official Python runtime as a parent image
FROM python:3.11.0-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /usr/src/app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable
ENV JWT_SECRET_KEY=dirghpatel

# Run app.py when the container launches
CMD ["python", "app.py"]