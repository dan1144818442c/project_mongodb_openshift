from fastapi import FastAPI ,Request
from  soldier import Soldier
from mongoDal import MongoLoad

app = FastAPI(title="Data Loader API (MongoDB)")
loader  =MongoLoad("data")
col = loader.create("soldier")


@app.get("/soldiersDB/data")
async def get_data():
    return  loader.get_info(collection=col)

@app.post("/soldiersDB/new_soldier")
async def add_person(first , last , rank , phone ):
    new_soldier = Soldier(first_name=first , last_name=last , rank=rank , phone_number=phone)
    return  loader.build(collection=col  , soldier=new_soldier)

@app.put("/soldiersDB/update/{id}/{update_field}/{update_value}")
async def update_person(id,update_field,update_value):
    return  loader.update(col,id,update_field,update_value)

@app.delete("/soldiersDB/delete/{id}")
async def delete_person(id):
    return  loader.delete(col , id)

# @app.get("/data")
# async def a():
#     return {"a"  : "200"}


# if __name__ == "__main__":
#
#
#     uvicorn.run(app, host="localhost", port=8000)