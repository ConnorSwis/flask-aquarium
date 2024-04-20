FROM python:slim
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY . /app
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app:app"]