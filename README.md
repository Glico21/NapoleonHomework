# Napoleon Homework
Выпускной проект курса NapoleonIT school Junior Backend Dev.
Проект представляет собой бэкенд для оффлайн мессенджера.
В проекте используется Sanic фреймворк.
## Установка
Для использования приложения необходим Docker.
1. Используйте git для клонирования репозитория на локальную машину.
```
git clone https://github.com/Glico21/NapoleonHomework
```
2. Запустите сборку контейнеров Docker.
```
docker-compose up
```
## Использование
Для работы с приложением требуется отправить http-запрос по адресу:
```
localhost:8000/
```
Тело запроса представляет собой json формата raw.
Приложение поддерживает маршрутизацию по адресам представленным в таблице, приведенной ниже.
|                URL              |   Методы   |                                                                             Назначение    |                                                        Тело запроса  |Аутентификация|
| :-----------------------------: | :--------: | :-------------------------------------------------------------  |:---------------------------------------------- | :----------: |
|          ```localhost:8000/```        |  **GET/POST**  |           helloworld-эндоинт, предназначен для проверки работоспособности приложения.     |                                                        Не требуется  |-  |
|        ```localhost:8000/user```      |    **POST**    |                                                                 Создание пользователя.    |  ```{```<br>```"login":str,``` <br>  ``` "password":str,``` <br>``` "first_name":str,```<br> ``` "last_name":str```<br> ```}```<br>|- |
|     ```localhost:8000/user/auth```    |    **POST**    |                                                            Аутентификация пользователя.   |                                        ```{```<br> ```“login”:str,```<br> ```“password”:str```<br> ```}```|-|
|  ```localhost:8000/user/<user_id>```  |     **GET**    |                 Получение информации о пользователя. Работает по указанному user id в url.|                                                          Не требуется|+|
|  ```localhost:8000/user/<user_id>```  |**PATCH/DELETE**|      Изменение информации о пользователе. Обновление или удаление в зависимости от метода |                                  ```{```<br> ```“first_name”:str,```<br> ```“last_name”:str```<br> ```}```|+|
|     ```localhost:8000/user/all```     |     **GET**    |                                   Получение информации о всех неудалённых пользователях.  |                                                          Не требуется|-|
|       ```localhost:8000/msg```        |  **GET/POST**  |                              Создание сообщения или получение всех сообщений для авторизованного пользователя. Действие определяется методом|                                    ```{``` <br>```“message”:str,```<br> ```“recipient”:str```<br> ```}```|+|
| ```localhost:8000/msg/<message_id>``` |      **GET**   |                                                                     Получение сообщения.  |                                                        Не требуется                                   |+|
| ```localhost:8000/msg/<message_id>``` |**PATCH/DELETE**|Изменение сообщения. Обновление или удаление сообщения в зависимости от метода.            |```{```<br> ```“id”:int,```<br> ```“sender_id”:int,```<br> ```“recipient_id”:int,``` <br>```“created_at”:str,```<br> ```“updated_at”:str,```<br> ```“message”:str```<br> ```}```|+|
