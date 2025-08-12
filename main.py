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
            "created_at": "14/07/2025",
            "items": []
        }],
    },
    "100000000": {
        "has_error": False,
        "error_detail": None,		
        "status": "complete_late",			
        "latest_shipping_date": "17/08/2025",
        "earliest_shipping_date": "25/08/2025",
        "created_at": "05/07/2025",			
        "shipments": [],
    },
    "100000001": {
        "has_error": False,
        "error_detail": None,		
        "status": "closed",			
        "latest_shipping_date": "12/07/2025",
        "earliest_shipping_date": "17/07/2025",
        "created_at": "05/07/2025",			
        "shipments": [],
        "shipped_at": "15/07/2025",
    },
    "100000002": {
        "has_error": False,
        "error_detail": None,		
        "status": "processing_partial_delivery",			
        "earliest_shipping_date": "01/08/2025",
        "latest_shipping_date": "30/09/2025",
        "created_at": "05/07/2025",	
        "shipments": [{
            "carrier_code": "colissimo",		
            "tracking_link": "https://www.laposte.fr/outils/suivre-vos-envois?code=9M00832571464",		
            "created_at": "14/07/2025",
            "items": [
                {
                    "ref": "1",
                    "name": "Chaussures Nike AirMax - rouge - 32",
                    "qty":1
                },
                {
                    "ref": "2",
                    "name": "Chaussures Adidas - Noir - 32",
                    "qty":1
                }
            ]
        },
        {
            "carrier_code": "colissimo",		
            "tracking_link": "https://www.laposte.fr/outils/suivre-vos-envois?code=9M0083271464",		
            "created_at": "16/07/2025",
            "items": [
                {
                    "ref": "3",
                    "name": "Chaussures Adidas - Vertes - 32",
                    "qty":1
                }
            ]
        }],
        "shipped_at": None,
        "items": [
            {
                "ref": "1",
                "name": "Chaussures Nike AirMax - rouge - 32",
                "qty":1
            },
            {
                "ref": "2",
                "name": "Chaussures Adidas - Noir - 32",
                "qty":1
            },
            {
                "ref": "3",
                "name": "Chaussures Adidas - Vertes - 32",
                "qty":1
            },
            {
                "ref": "4",
                "name": "Chaussures Adidas - Bleues - 32",
                "qty":1
            }
        ]
    },
    "100000003": {
        "has_error": False,
        "error_detail": None,		
        "status": "processing_partial_delivery",			
        "earliest_shipping_date": "01/08/2025",
        "latest_shipping_date": "30/09/2025",
        "created_at": "05/07/2025",	
        "shipments": [{
            "carrier_code": "colissimo",		
            "tracking_link": "https://www.laposte.fr/outils/suivre-vos-envois?code=9M00832571464",		
            "created_at": "14/07/2025",
        },
        {
            "carrier_code": "colissimo",		
            "tracking_link": "https://www.laposte.fr/outils/suivre-vos-envois?code=9M0083271464",		
            "created_at": "16/07/2025",
        }],
        "shipped_at": None,
        "items": [
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
                "qty":1,
                "qty_shipped": 1
            }
        ]
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

    if ref not in shipments:
        response["error"] = "unknown ref"
        response["has_error"] = True

    if response["has_error"] is True:
        return response

    return shipments[ref]
