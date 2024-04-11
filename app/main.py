from typing import Union

from fastapi import FastAPI

from core.config import settings

print("Mysql user", settings.MYSQL_USER)
print("Mysql password", settings.MYSQL_PASSWORD)
print("Mysql database uri", settings.MYSQL_DATABASE_URI)

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}