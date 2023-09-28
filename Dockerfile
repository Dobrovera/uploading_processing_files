FROM python:3.8
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /uploading_processing_files
COPY . .
RUN pip install -r requirements.txt
