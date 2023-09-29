FROM python:3.8

RUN pip install --upgrade pip

WORKDIR /uploading_processing_files
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]