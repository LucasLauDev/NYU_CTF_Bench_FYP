FROM python:3.10-slim
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir flask requests authlib loginpass flask-session python-gitlab || true
EXPOSE 8089
CMD ["python3", "server.py"]
