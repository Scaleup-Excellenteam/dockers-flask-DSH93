FROM dart:stable

WORKDIR /app

COPY app.py requirements.txt ./
# Install bash to run the entrypoint script
RUN apt-get update && apt-get install -y python3-venv python3-pip \ 
    && python3 -m venv venv \
    && . venv/bin/activate \
    && pip install --no-cache-dir -r requirements.txt

ENV VIRTUAL_ENV=/app/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

CMD ["python", "app.py"] 
