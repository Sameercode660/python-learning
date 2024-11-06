from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def home():
    return {'data': 'Welcome to home page'}

@app.get('/contact')
def contact():
    return {'data': 'Welcome to contact page'}


import uvicorn

uvicorn.run(app)