FROM python:3.9-slim

WORKDIR /app
COPY . .

RUN pip install requests

CMD ["python", "monitor.py"]