# Use the Python image from the Docker Hub
FROM python:3.9-slim

# Install necessary packages and Dart
RUN apt-get update && apt-get install -y python3 python3-pip wget unzip \
    && wget -qO- https://storage.googleapis.com/dart-archive/channels/stable/release/latest/sdk/dartsdk-linux-x64-release.zip \
    | funzip > /tmp/dart.zip \
    && unzip /tmp/dart.zip -d /usr/lib \
    && apt-get clean

ENV PATH="/usr/lib/dart-sdk/bin:${PATH}"

WORKDIR /app

COPY . /app

RUN pip3 install flask requests

EXPOSE 5000

CMD ["python3", "app.py"]
