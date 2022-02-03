# Use the python image as the base image
FROM openjdk
# Create a new app directory for my application files
RUN mkdir /app
# Copy the app files from host machine to image filesystem
COPY / /app
# Set the directory for executing future commands
WORKDIR /app
# Run the Main class
CMD java Main