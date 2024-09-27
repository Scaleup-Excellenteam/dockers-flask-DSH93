FROM python:3.9-slim

WORKDIR /app

COPY app.py requirements.txt ./

RUN python3 -m venv venv \
    && . venv/bin/activate \
    && pip install --no-cache-dir -r requirements.txt

ENV VIRTUAL_ENV=/app/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

CMD ["python", "app.py"]
