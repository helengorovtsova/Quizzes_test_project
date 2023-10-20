# Quizzes Test Project with FastAPI and SQLAlchemy
A test project implemented using the FastAPI framework and SQLAlchemy to interact with an API service that generates questions for a quiz (https://jservice.io/api).
**How to start a project**

1) Ensure that Docker is installed on your system.
2) Clone the repository
3) Create a `.env` file in the project's root directory and configure the necessary database settings (host, username, password, ports). You can use the `.env.example` file as a reference.
4) Navigate to the project's root directory (where the `docker-compose.yml` file is located).
5) Start the containers by running the following command:
   > docker-compose up
This command will initiate the containers defined in the docker-compose.yml file. You should see output indicating that the services are running.

6) Once the containers are up and running, you can access the application in a web browser or through the specified URLs.
7) To make a POST request, use the URL: http://localhost:8080/questions/ and provide the request data in JSON format.
For example:
{
    "questions_num": 5
}

   Example of a POST request response:
{
    "text": "Several bridges, including El Tahrir, cross the Nile in this capital",
    "answer": "Cairo",
    "created_at": "2022-12-30T20:45:54.227Z"
}

8) To make a GET request, use the URL: http://localhost:8080/questions/<question_id>/.


All dependencies are listed in the requirements.txt file and are installed when running the docker-compose up command.





  
