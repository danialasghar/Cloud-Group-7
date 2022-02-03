# Pull the specific version of tomcat
FROM tomcat:10-jdk16
# Add the application code from the host machine to the image file system /user/local.. is where tomcat stores its information
ADD target/MyWebApp.war /usr/local/tomcat/webapps/MyWebApp.war
# Expose the port running the tomcat server within the container
EXPOSE 8080
# Invoke the catalina.sh script to run the tomcat server
CMD ["catalina.sh", "run"]