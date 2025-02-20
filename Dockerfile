FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt /app/
RUN apt update && apt install -y git
RUN pip install -r requirements.txt

COPY src/ /app/

EXPOSE 5000

ENV PYTHONPATH='./src:$PYTHONPATH'

CMD ["python", "/app/app.py"]
