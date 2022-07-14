# Napoleon Homework
Graduation project of NapoleonIT school Junior Backend Dev course.
The project is a backend for offline messenger.
Implementation in the [Sanic framework](https://sanic.readthedocs.io/en/stable/) v20.12.1.
Dockerized application.
1. Use git to [clone](https://git-scm.com/docs/git-clone) the repository to your local machine.
```
git clone https://github.com/Glico21/NapoleonHomework
```
2. Start the Docker container via [docker-compose](https://docs.docker.com/compose/) file.
```
docker-compose up
```
## Usage
To work with the application you need to send an http-request to:
```
localhost:8000
```
The body of the request is a json in raw format.
The application supports routing to the addresses shown in the table below.
|                URL              |   Methods   |                                                                             Destination    |                                                        Request body  |Authentication|
| :-----------------------------: | :--------: | :-------------------------------------------------------------  |:---------------------------------------------- | :----------: |
|          ```localhost:8000/```        |  **GET/POST**  |           helloworld-endoint, designed to test the performance of the application.     |                                                        Not requiredя  |-  |
|        ```localhost:8000/user```      |    **POST**    |                                                                 User creation    |  ```{```<br>```"login":str,``` <br>  ``` "password":str,``` <br>``` "first_name":str,```<br> ``` "last_name":str```<br> ```}```<br>|- |
|     ```localhost:8000/user/auth```    |    **POST**    |                                                            User authentication.   |                                        ```{```<br> ```“login”:str,```<br> ```“password”:str```<br> ```}```|-|
|  ```localhost:8000/user/<user_id>```  |     **GET**    |                 Get user details. Work via user id in url.|                                                          Not required|+|
|  ```localhost:8000/user/<user_id>```  |**PATCH/DELETE**|      Changing user details. Update or delete depending on method |                                  ```{```<br> ```“first_name”:str,```<br> ```“last_name”:str```<br> ```}```|+|
|     ```localhost:8000/user/all```     |     **GET**    |                                   Getting a list of all undeleted users.  |                                                          Not required|-|
|       ```localhost:8000/msg```        |  **GET/POST**  |                              Message creation or getting all messages for authorized user. Action is determined by the method. |                                    ```{``` <br>```“message”:str,```<br> ```“recipient”:str```<br> ```}```|+|
| ```localhost:8000/msg/<message_id>``` |      **GET**   |                                                                     Получение сообщения.  |                                                        Not required                                   |+|
| ```localhost:8000/msg/<message_id>``` |**PATCH/DELETE**|Changing message. Update or delete message depending on method.            |```{```<br> ```“id”:int,```<br> ```“sender_id”:int,```<br> ```“recipient_id”:int,``` <br>```“created_at”:str,```<br> ```“updated_at”:str,```<br> ```“message”:str```<br> ```}```|+|
| ```localhost:8000/msg/<sender_id>/recipient_id>``` |**GET**|Getting dialog between user and id sender_id and recipient_id.            |                                                        Not required  |+|
