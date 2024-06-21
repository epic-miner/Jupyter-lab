# Use the official Python base image
FROM python:3.9-slim

# Install sudo
RUN apt-get update && apt-get install -y sudo

# Install necessary dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the start script
COPY start.sh /start.sh
RUN chmod +x /start.sh

# Allow passwordless sudo for all users (use with caution)
RUN echo "ALL ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

# Set environment variables
ENV PORT=8888

# Expose the port
EXPOSE 8888

# Run the start script
CMD ["/start.sh"]
