# Choose an appropriate slim base image.
FROM python:slim
#keeps python from generating .pyc files in the container 
ENV PYTHONDONTWRITEBYTECODE=1
# turns on buffering for eaiser container logging
ENV PYTHONBUFFERED=1
#creates a copy inside of the container so that dependencies will work correctly
COPY requirements.txt  ./
# requirements.txt are automatically placed in local computer but not in container. so that when you run pip install it doesnt crash
RUN python -m pip install -r requirements.txt

WORKDIR /app
COPY ./ /app


RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

CMD ["python", "drf_jwt_backend/manage.py", "runserver", "0.0.0.0:8000"]