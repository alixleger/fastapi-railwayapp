from fastapi import FastAPI, Query

shipments = {
    "690003171": {
    "has_error": False,
    "error_detail": None,		
    "status": "completed_delivered",			
    "latest_shipping_date": "17/07/2025",
    "earliest_shipping_date": "25/07/2025",
    "created_at": "05/07/2025",			
    "shipments": [{
        "carrier_code": "colissimo",		
        "tracking_link": "https://www.laposte.fr/outils/suivre-vos-envois?code=9M00832571464",		
        "created_at": "14/07/2025"		
    }],
}
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

    if ref not in shipments:
        response["error"] = "unknown ref"

    if response["error"] is not None:
        return response

    return shipments[ref]
