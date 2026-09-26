from fastapi import FastAPI
import os

app = FastAPI(title="My DevOps Pet App")

@app.get("/")
def read_root():
    return {
        "status": "ok",
        "message": "Hello, DevOps World!",
        "version": os.getenv("APP_VERSION", "1.0.0")
    }

@app.get("/health")
def health_check():
    return {"status": "healthy"}
