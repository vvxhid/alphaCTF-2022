FROM python:alpine
RUN pip install fastapi uvicorn
COPY ./app /app

WORKDIR /app
EXPOSE 8001
ENV FLAG=alphaCTF{read_the_docs_please}
CMD ["uvicorn", "main:app", "--reload", "--port", "8001"]