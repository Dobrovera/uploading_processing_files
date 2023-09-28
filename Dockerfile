FROM python:3.8
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /upf
COPY requirements.txt /upf/
RUN pip install -r requirements.txt
COPY . /upf/