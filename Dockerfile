FROM python:latest

WORKDIR /app

COPY src/ ./src/ 

RUN pip install --no-cache-dir --upgrade pip

# Default command can be overridden by docker-compose
CMD ["python", "src/app/main.py"]