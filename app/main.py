from fastapi import FastAPI

app = FastAPI(
    title="AI Cold Outreach Agent",
    version="0.1.0"
)

@app.get("/")
def root():
    return {"message": "Outreach Agent API is running"}