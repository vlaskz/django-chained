# simple FastApi demonstration
# just trynna learn this faster(hahaha) as I can.
# Author: Isaias Velasquez.

from typing import Optional

import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    return {"hello": "world"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

if __name__ == '__main__':
    uvicorn.run(app)
