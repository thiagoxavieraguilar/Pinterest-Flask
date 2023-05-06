# Pinterest-Flask


###### Pinterest-Flask is a web application inspired by Pinterest, built using Flask framework. It allows users to create accounts, upload images, and view a feed of all images uploaded by all users. The app uses a MySQL database to store user information and uploaded images.


## Prerequisites
- Docker 

## Clone the repository

Clone this repository to your local machine using the following command:

```
git clone https://github.com/your-username/Pinterest-Flask.git
```

## Docker Installation

Before running the application, you need to install Docker on your machine. You can download the appropriate installer for your platform from the following links:

- Docker for Windows: https://docs.docker.com/docker-for-windows/install/
- Docker for Mac: https://docs.docker.com/docker-for-mac/install/
- Docker for Linux: https://docs.docker.com/engine/install/

## Docker Build
###### To build the Docker image for this application, run the following command in the project directory:

```
docker build -t pinterest_flask .
```
###### This will create a Docker image with the tag pinterest_flask.

## Docker Compose

###### To start the application using Docker Compose, run the following command in the project directory:

```
docker-compose up
```

###### This will start the application and its dependencies (i.e., the MySQL database) in separate Docker containers.


###### After starting the application, you can access it by navigating to http://localhost:5000 in your web browser. From there, you can create an account, log in, upload images, and view a feed of all images uploaded by all users in db.