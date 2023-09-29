[![Maintainability](https://api.codeclimate.com/v1/badges/655c5b016946c1dde774/maintainability)](https://codeclimate.com/github/Dobrovera/uploading_processing_files/maintainability)
![Test Coverage](https://api.codeclimate.com/v1/badges/655c5b016946c1dde774/test_coverage)


Simple Django REST API to upload files to the server and then process them asynchronously using Celery.

[link](http://85.143.223.201:8000/files) to the domain 

[link](https://github.com/Dobrovera/uploading_processing_files/assets/100479798/6113f66a-4387-4136-9452-5b484d32e1b9) link to video demonstration

### How it works?
There are 2 endpoints:
* [files/](http://85.143.223.201:8000/files/) — returns a list of all files in db and their data (GET request)

* [upload/](http://85.143.223.201:8000/upload/) — downloading a file and adding it to the database
(POST request). Asynchronous process processes file status with a delay of 10 seconds
