FROM openjdk:11-slim

WORKDIR /app

COPY . /app

RUN apt-get update && apt-get install -y python3 python3-pip && pip3 install flask

EXPOSE 5002

CMD ["python3", "app.py"]
