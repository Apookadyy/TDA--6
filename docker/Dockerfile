FROM python:3.10

WORKDIR /app
COPY . .

RUN pip install flask pytest requests

CMD ["python", "src/main.py"]