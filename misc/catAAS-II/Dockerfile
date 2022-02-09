FROM python:3.8-alpine

RUN pip install fastapi uvicorn aiofiles
RUN adduser -D alphaCTF
COPY ./app /home/alphaCTF/app
RUN chown alphaCTF:root /home/alphaCTF/app -R

USER alphaCTF
WORKDIR /home/alphaCTF/app
EXPOSE 5000
CMD ["python", "main.py"]