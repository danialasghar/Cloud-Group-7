# Get image from dockerhub
FROM openjdk:16
# Create a directory in container
RUN mkdir /app
# Copy app files from host to image
COPY out/production/HelloWorldDockerNew/ /app
# Set directory to execute further commands
WORKDIR /app
# Run the main class
CMD java Main
