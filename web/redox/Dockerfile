FROM python:alpine
RUN pip install fastapi uvicorn
COPY ./app /app

WORKDIR /app
EXPOSE 8001
CMD ["uvicorn", "main:app", "--reload", "--port", "8001"]