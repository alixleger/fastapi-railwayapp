from fastapi import FastAPI, Query, HTTPException
from fastapi.responses import JSONResponse
import random

ORDER_STATUS_REF_MAPPING = {
    "690003171": "shipped",
    "1234567": "pending",
    "000000": "processing",
    "11111111":  "cancelled",
    "666666": "delivered",
}



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
    
    if ref not in ORDER_STATUS_REF_MAPPING:
        raise HTTPException(
            status_code=400,
            detail={"error": "unkwown ref"}
        )

    status = ORDER_STATUS_REF_MAPPING[ref]
    
    return {"status": status}
