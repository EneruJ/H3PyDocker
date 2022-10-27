FROM python:3.6-slim
RUN pip3 install fastapi uvicorn requests aioredis
COPY ./app /app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "15400"]