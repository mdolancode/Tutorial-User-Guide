from fastapi import FastAPI

app = FastAPI()

# Cannot have two endpoints with the same path operation and parameters
@app.get("/users")
async def read_users():
    return ["Rick", "Morty"]


@app.get("/users")
async def read_users2():
    return ["Bean", "Elfo"]
