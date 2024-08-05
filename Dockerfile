# Use the official Python image as the base image 
FROM python:3.9-slim

# Set the working directory inside the container 
WORKDIR /app

# Copy the requirements file and install dependencies 
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the container
COPY . .

# Expose the port the Flask app will run on
EXPOSE 5000

# Command to run the application
CMD ["python", "app.py"]
