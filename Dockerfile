# Use the official Python image as a base image
FROM python:3.9

# Set environment variables
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Set the working directory in the container
WORKDIR /app

# Copy the application code into the container
COPY . .

# Install dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Expose the port on which the Flask app will run
EXPOSE 5000

# Command to run the Flask application
CMD ["flask", "run"]
