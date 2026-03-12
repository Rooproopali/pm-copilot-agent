from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "PM Copilot Agent Running"}
