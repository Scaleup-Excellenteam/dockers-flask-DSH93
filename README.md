```markdown
# Multi-Language Code Execution System

This project implements a multi-language code execution system using Docker and Flask. It supports executing code written in Java, Python, and Dart within isolated Docker containers. The system consists of four Docker containers that communicate with each other using HTTP requests.

## Project Structure

```
.
├── dart-executor
│   ├── app.py
│   ├── Dockerfile
├── java-executor
│   ├── app.py
│   ├── Dockerfile
├── python-executor
│   ├── app.py
│   ├── Dockerfile
├── router
│   ├── app.py
│   ├── Dockerfile
│   ├── example.dart
│   ├── example.java
│   ├── example.py
├── README.md
├── requirements.txt
├── docker-compose.yml
```

## Components

1. **router**: The central component that receives code submissions, saves them, and forwards execution requests to the appropriate language executor.
2. **dart-executor**: Executes Dart code.
3. **java-executor**: Executes Java code.
4. **python-executor**: Executes Python code.

## Setup Instructions

### Prerequisites

- Docker
- Docker Compose

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/Scaleup-Excellenteam/dockers-flask-DSH93.git
    cd dockers-flask-DSH93
    ```

2. Build and start the Docker containers using Docker Compose:
    ```sh
    docker-compose up --build
    ```

## Usage

### Submitting Code

You can submit code in Python, Java, or Dart using the `/submit` endpoint.

#### Python Example

```sh
CODE=$(<router/example.py)
curl -X POST http://localhost:5000/submit -F "language=python" -F "code=$CODE"
```

#### Java Example

```sh
CODE=$(<router/example.java)
curl -X POST http://localhost:5000/submit -F "language=java" -F "code=$CODE"
```

#### Dart Example

```sh
CODE=$(<router/example.dart)
curl -X POST http://localhost:5000/submit -F "language=dart" -F "code=$CODE"
```

### Executing Code

After submitting the code, you can execute it using the `/execute/<language>` endpoint.

#### Python Execution

```sh
curl http://localhost:5000/execute/python
```

#### Java Execution

```sh
curl http://localhost:5000/execute/java
```

#### Dart Execution

```sh
curl http://localhost:5000/execute/dart
```

## Logs

You can check the logs of each container to debug any issues:

```sh
docker-compose logs router
docker-compose logs python-executor
docker-compose logs java-executor
docker-compose logs dart-executor
```


```
