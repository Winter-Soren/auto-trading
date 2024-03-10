FROM python:3.11.4

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

# EXPOSE 8000

# CMD ["python", "app.py"]