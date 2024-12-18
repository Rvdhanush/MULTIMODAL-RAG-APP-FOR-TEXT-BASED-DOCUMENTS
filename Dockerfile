# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 9000 available to the world outside this container
EXPOSE 9000

# Define environment variable
ENV NAME=World

# Run uvicorn server on port 9000
CMD ["uvicorn", "app.app:app", "--host", "0.0.0.0", "--port", "9000"]

# Copy faiss_index directory to the container
COPY faiss_index /app/faiss_index

