# Flask example
## Постановка задачи

Разработать Flask-сервер - шаблон для разработки, создав сервер для обработки, 
хранения и передачи файлов различных форматов (картинок или текста) в pandas DataFrame

## Промежуточные шаги
### app.py
Написать app.py, используя расширение для Flask - connexion
```
import connexion
from typing import Tuple, Dict

def health() -> Tuple[Dict[str, str], int]:
    return {"health_status": "running"}, 200

app = connexion.App(__name__)
app.add_api('swagger.yaml')
application = app.app

if __name__ == "__main__":
    app.run(port=8080)
```
### swagger.yaml

https://swagger.io/docs/specification/2-0/describing-request-body/

Для полноценной работы с connexion нужен swagger.yaml файл, в котором содержится 
описание всех методов и их параметров:
```
swagger: "2.0"

info:
  title: FlaskApi
  version: "0.1"
  description: RESTApi for documents in Pandas dataframe

consumes:
  - application/json
  - multipart/form-data
  - text/plain

produces:
  - application/json

paths:
  /health:
    get:
      tags: [Health]
      operationId: app.health
      summary: Health Check
      responses:
        '200':
          description: Status message from server describing current health

```
Пример для post-метода:
```
paths:
    /post_file:
        post:
          tags: [POST]
          operationId: app.post_file
          summary: Post row info at database
          consumes:
            - multipart/form-data
          parameters:
            - in: formData
              name: file
              type: file
              description: file to write
          responses:
            '200':
              description: Successful writing made
```
### POST-метод
Во втором пункте в описании метода post в разделе operationId указано название функции, 
которая должна соджержаться в app.py:
```
def post_file() -> int:
    
    # CODE 

    return 200
```

Дополните app.py этой функцией, которая принимает post-запрос, считывает содержимое файл. Затем возможны две опции:

- если файл с таким именем уже существует в DataFrame, то не нужно ничего делать
- если файл с таким именем не существует в DataFrame, то запишите его туда 

**HINT** : Для записи содержимого файла воспользуйтесь кодировкой base64
### fullREST API: GET, PUT, HEAD, DELETE
Реализовать fullREST API: GET, PUT, HEAD, DELETE аналогично тому, как был написан метод POST

**HINT** : Что должны делать методы:

- GET - по имени файла вернуть его содержимое, либо, если файла нет в DataFrame, то вернуть 
сообщение об этом
- PUT - обновить содержимое файла, либо, если файла нет в DataFrame, то вернуть 
сообщение об этом
- HEAD - вернуть названия всех файлов из DataFrame
- DELETE - удалить название и сождержимое файла из DataFrame, либо, если файла нет в DataFrame, то вернуть 
сообщение об этом

**WARNING** Не забудьте дописать методы в swagger.yaml эти методы!
```
def get_file(file_name) -> Tuple[Dict[str, str], int]:
    
    # CODE

    return {"result": encoded_string}, 200


def put_file() -> int:
    
    # CODE

    return 200


def head_file(extensions) -> Tuple[Dict[str, str], int]:

    # CODE

    return {"result": header}, 200


def delete_file(file_name) -> int:
    
    # CODE

    return 200
```

### Дополнительные опции:

- Логирование
- Проверка расширения файла
