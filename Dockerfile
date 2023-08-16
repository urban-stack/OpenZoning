# Use the official Python image from the Docker Hub
FROM python:3.8-slim-buster

# Install necessary system dependencies (if any)
RUN apt-get update -y && \
    apt-get install -y libproj-dev proj-data proj-bin libgeos-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install GeoPandas and its dependencies (or other required packages)
RUN pip install geopandas
RUN pip install shapely

# Set a default working directory in the container (this will be overridden by the docker-compose.yml)
WORKDIR /app

# Set up the entry point to run bash
CMD ["/bin/bash"]
