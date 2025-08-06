from fastapi import FastAPI, Query, HTTPException
from fastapi.responses import JSONResponse
import random

ORDER_STATUS_REF_MAPPING = {
    "690003171": "delivered",
    "1234567": "pending",
    "000001": "processing",
    "11111111":  "cancelled",
    "666666": "shipped",
}

TRACKING_LINK_REF_MAPPING = {
    "690003171": "https://www.laposte.fr/outils/suivre-vos-envois?code=9M00832571464",
    "1234567": None,
    "000001": None,
    "11111111": None,
    "666666": "https://www.laposte.fr/outils/suivre-vos-envois?code=9M00832571464",
}

REFUND_DATE_REF_MAPPING = {
    "690003171": None,
    "1234567": None,
    "000001": None,
    "11111111": "17/07/2025",
    "666666": None,
}

PAYMENT_METHOD_REF_MAPPING = {
    "690003171": "bank card",
    "1234567": "bank card",
    "000001": "bank card",
    "11111111": "bank card",
    "666666": "bank card",
}

SHIPPING_DATE_REF_MAPPING = {
    "690003171": "03/10/2025",
    "1234567": "08/10/2025",
    "000001": "08/10/2025",
    "11111111": None,
    "666666": "03/10/2025",
}


app = FastAPI()

@app.get("/")
async def root():
    return {"greeting": "Hello, World!", "message": "Welcome to FastAPI!"}


@app.get("/status")
def get_status(ref: str = Query(...)):
    response = {
        "error": None,
        "status": None,
        "tracking_link": None,
        "refund_date": None,
        "payment_method": None,
        "shipping_date": None,
    }

    if not ref.isdigit():
        response["error"] = "invalid ref format"

    if ref not in ORDER_STATUS_REF_MAPPING:
        response["error"] = "unknown ref"

    if response["error"] is not None:
        return response

    response["status"] = ORDER_STATUS_REF_MAPPING[ref]
    response["tracking_link"] = TRACKING_LINK_REF_MAPPING[ref]
    response["refund_date"] = REFUND_DATE_REF_MAPPING[ref]
    response["payment_method"] = PAYMENT_METHOD_REF_MAPPING[ref]
    response["shipping_date"] = SHIPPING_DATE_REF_MAPPING[ref]

    return response
