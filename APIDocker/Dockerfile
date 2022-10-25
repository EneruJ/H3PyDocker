FROM python:3.6
RUN pip3 install fastapi uvicorn
RUN pip install -r requirements.txt
COPY ./app /app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "15400"]