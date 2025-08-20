FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY ./service/data_loader/ /app/

EXPOSE 8000

CMD ["uvicorn", "data_loader_server:app", "--host", "0.0.0.0", "--port", "8000"]