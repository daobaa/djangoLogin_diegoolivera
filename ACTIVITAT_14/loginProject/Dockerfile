# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory inside the container to /app
WORKDIR /app

# Copy the contents of the logIn directory (where manage.py is located) into the container
COPY . /app/

# Install any dependencies listed in requirements.txt
RUN pip install --upgrade pip
RUN pip install -r /app/requirements.txt  # Assuming requirements.txt is in logIn/

# Expose port 8000 to the host machine
EXPOSE 8000

# Set the command to run the Django app on the container's start
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]