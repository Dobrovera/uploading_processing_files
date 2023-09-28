[![Maintainability](https://api.codeclimate.com/v1/badges/655c5b016946c1dde774/maintainability)](https://codeclimate.com/github/Dobrovera/uploading_processing_files/maintainability)
![Test Coverage](https://api.codeclimate.com/v1/badges/655c5b016946c1dde774/test_coverage)


Simple Django REST API to upload files to the server and then process them asynchronously using Celery.

#### [link](85.143.223.201:8000) to the domain

###For What?
There are 2 endpoints:
<li>files/ — returns a list of all files in db and their data (GET request)
</li>
<li>upload/ — downloading a file and adding it to the database
(POST request). Asynchronous process processes file status with a delay of 10 seconds
</li>

[!(renamed webm)](video/video.mp4)


