# dart-executor Dockerfile
FROM python:3.9-slim

# Install necessary packages and Dart
RUN apt-get update && apt-get install -y python3 python3-pip curl unzip \
    && mkdir -p /opt/dart-sdk \
    && curl -o /tmp/dart.zip https://storage.googleapis.com/dart-archive/channels/stable/release/latest/sdk/dartsdk-linux-x64-release.zip \
    && unzip /tmp/dart.zip -d /opt/dart-sdk \
    && rm /tmp/dart.zip \
    && apt-get clean

ENV PATH="/opt/dart-sdk/dart-sdk/bin:${PATH}"
