# Quizzes_test_project
A test project implemented using the FastAPI framework and SQLAlchemy to interact with an API service that generates questions for a quiz (https://jservice.io/api).
**How to start a project**

1) Docker must be installed on your system.
2) Clone the Repository
3) Сreate a .env file in the project's root directory and set the necessary values for your database (host, username, password, ports).
  For example, use the .env.example file.
4) Start the Containers:
   > docker-compose up
This command will start the containers defined in the docker-compose.yml file. You should see output indicating that the services are running.

5) Once the containers are running, you can access application in a web browser or via the specified URL.
   URL for POST-request - http://0.0.0.0:8080/questions/
   URL for GET-request - http://0.0.0.0:8080/questions/<questions_id>/

   Example POST request (you can use Postman):
   JSON: {"questions_num": 5} - if you want to save 5 random quiz questions
   

      

  
