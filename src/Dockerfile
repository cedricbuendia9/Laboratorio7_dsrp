FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install -r src/requirements.txt

EXPOSE 5000

CMD ["python","src/app.py"]