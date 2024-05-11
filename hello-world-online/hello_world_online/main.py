from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def index():
    return {"hello": "world"}


@app.get('/ntu')
def ntu():
    return {"class": "GEN-AI"}
