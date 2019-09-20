FROM python:2.7
RUN pip install Django Pillow

WORKDIR /app
COPY . .

EXPOSE 80
CMD ["python", "manage.py", "runserver", "0.0.0.0:80", "--insecure"]

