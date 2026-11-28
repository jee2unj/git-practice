# orderlab/api.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from orderlab.pricing import subtotal


class OrderIn(BaseModel):
    price: int = Field(ge=0)
    quantity: int = Field(gt=0)


def create_app() -> FastAPI:
    app = FastAPI()
    store: dict[int, int] = {}

    # Endpoint
    @app.post("/orders", status_code=201)  # POST/orders APT 규약 -> 201
    def create_order(data: OrderIn):
        order_id = len(store) + 1
        store[order_id] = subtotal(data.price, data.quantity)
        return {"id": order_id, "subtotal": store[order_id]}

    @app.get("/orders/{order_id}")
    def get_order(order_id: int):  # GET/orders/1 -> 200
        if order_id not in store:
            raise HTTPException(status_code=404, detail="Not found")  # 없는 ID -> 404
        return {"id": order_id, "subtotal": store[order_id]}

    return app
