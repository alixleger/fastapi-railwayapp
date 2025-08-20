from fastapi import FastAPI, Query

products = [
    {
        "ref": "1",
        "name": "Chaussures Nike AirMax - rouge - 32",
        "qty":1,
        "qty_shipped": 1
    },
    {
        "ref": "2",
        "name": "Chaussures Adidas - Noir - 32",
        "qty":1,
        "qty_shipped": 1
    },
    {
        "ref": "3",
        "name": "Chaussures Adidas - Vertes - 32",
        "qty":1,
        "qty_shipped": 1
    },
    {
        "ref": "4",
        "name": "Chaussures Adidas - Bleues - 32",
        "qty":1,
        "qty_shipped": 1
    },
    {
        "ref": "5",
        "name": "Chaussures Nike AirMax - noire - 32",
        "qty":1,
        "qty_shipped": 1
    },
    {
        "ref": "6",
        "name": "Chaussures Nike AirMax - verte - 32",
        "qty":1,
        "qty_shipped": 0
    },
    {
        "ref": "7",
        "name": "Chaussures Nike AirMax - bleue - 32",
        "qty": 2,
        "qty_shipped": 1
    }
]

order = {
    "100000000": {
        "status": "processing",			
        "created_at": "05/07/2025",
        "earliest_shipping_date": "01/10/2025",
        "latest_shipping_date": "30/11/2025"
    },
    "100000001": {
        "status": "cancelled",			
        "created_at": "05/07/2025",
        "earliest_shipping_date": "01/10/2025",
        "latest_shipping_date": "30/11/2025"
    },
    "100000002": {
        "status": "holded",			
        "created_at": "05/07/2025",
        "earliest_shipping_date": "01/10/2025",
        "latest_shipping_date": "30/11/2025"
    },
    "100000003": {
        "status": "fraud",			
        "created_at": "05/07/2025",
        "earliest_shipping_date": "01/10/2025",
        "latest_shipping_date": "30/11/2025"
    },
    "100000004": {
        "status": "pending_payment",			
        "created_at": "05/07/2025",
        "earliest_shipping_date": "01/10/2025",
        "latest_shipping_date": "30/11/2025"
    },
    "100000005": {
        "status": "complete_late",			
        "created_at": "05/07/2025",
        "earliest_shipping_date": "01/08/2025",
        "latest_shipping_date": "10/08/2025"
    },
    "100000006": {
        "status": "processing_shipment",			
        "created_at": "05/07/2025",
        "earliest_shipping_date": "01/08/2025",
        "latest_shipping_date": "30/08/2025"
    },
    "100000007": {
        "status": "complete",			
        "created_at": "05/07/2025",
        "shipped_at": "25/07/2025",
        "shipments": [{
            "carrier_code": "colissimo",		
            "tracking_link": "https://www.laposte.fr/outils/suivre-vos-envois?code=9M0083271464",		
            "created_at": "16/07/2025",
        }],
        "items": [products[0]] 
    },
    "100000008": {
        "status": "complete_delivery_in_progress",			
        "created_at": "05/07/2025",
        "shipped_at": "19/08/2025",
        "shipments": [{
            "carrier_code": "colissimo",		
            "tracking_link": "https://www.laposte.fr/outils/suivre-vos-envois?code=9M0083271464",		
            "created_at": "19/08/2025",
        }],
        "items": [products[0]] 
    },
    "100000009": {
        "status": "complete_delivered",			
        "created_at": "05/07/2025",
        "shipped_at": "17/08/2025",
        "shipments": [{
            "carrier_code": "colissimo",		
            "tracking_link": "https://www.laposte.fr/outils/suivre-vos-envois?code=9M0083271464",		
            "created_at": "17/08/2025",
        }],
        "items": [products[0]] 
    },
    "100000010": {
        "status": "complete_delivered_removal_point",			
        "created_at": "05/07/2025",
        "shipped_at": "17/08/2025",
        "shipments": [{
            "carrier_code": "colissimo",		
            "tracking_link": "https://www.laposte.fr/outils/suivre-vos-envois?code=9M0083271464",		
            "created_at": "17/08/2025",
        }],
        "items": [products[0]] 
    },
    "100000011": {
        "status": "complete",			
        "created_at": "05/07/2025",
        "earliest_shipping_date": "01/08/2025",
        "latest_shipping_date": "30/08/2025",
        "shipments": [{
            "carrier_code": "colissimo",		
            "tracking_link": "https://www.laposte.fr/outils/suivre-vos-envois?code=9M0083271464",		
            "created_at": "16/07/2025",
        }],
        "items": [products[0], products[1]] 
    },
    "100000012": {
        "status": "processing_partial",			
        "created_at": "05/07/2025",
        "earliest_shipping_date": "01/08/2025",
        "latest_shipping_date": "30/08/2025",
        "shipments": [{
            "carrier_code": "colissimo",		
            "tracking_link": "https://www.laposte.fr/outils/suivre-vos-envois?code=9M0083271464",		
            "created_at": "16/07/2025",
        },
        {
            "carrier_code": "colissimo",		
            "tracking_link": "https://www.laposte.fr/outils/suivre-vos-envois?code=3149389348",		
            "created_at": "17/07/2025",
        }],
        "items": [*products] 
    }
}


app = FastAPI()

@app.get("/")
async def root():
    return {"greeting": "Hello, World!", "message": "Welcome to FastAPI!"}


@app.get("/status")
def get_status(ref: str = Query(...)):
    response = {
        "has_error": False,
        "error": None,
    }

    if not ref.isdigit():
        response["error"] = "invalid ref format"
        response["has_error"] = True

    if ref not in order:
        response["error"] = "unknown ref"
        response["has_error"] = True

    if response["has_error"] is True:
        return response

    return order[ref]
