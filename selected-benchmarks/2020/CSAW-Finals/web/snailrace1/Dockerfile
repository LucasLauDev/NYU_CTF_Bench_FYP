FROM python:3.10-slim
WORKDIR /app
COPY handout/ /app/
RUN pip install --no-cache-dir flask pyjwt redis obs-websocket-py || true
EXPOSE 49383
CMD ["python3", "server.py"]
