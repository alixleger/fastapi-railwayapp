from fastapi import FastAPI, Query, HTTPException
from fastapi.responses import JSONResponse
import random

ORDER_STATUSES = ["pending", "processing", "shipped", "delivered", "cancelled"]


app = FastAPI()

@app.get("/")
async def root():
    return {"greeting": "Hello, World!", "message": "Welcome to FastAPI!"}


@app.get("/status")
def get_status(ref: str = Query(...)):
    if not ref.isdigit():
        raise HTTPException(
            status_code=400,
            detail={"error": "invalid ref format"}
        )
    
    status = random.choice(ORDER_STATUSES)
    return {"ref": ref, "status": status}
