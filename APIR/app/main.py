from fastapi import FastAPI
import aioredis

app = FastAPI()
 
@app.get("/")
async def read_root():
    redis = aioredis.from_url("redis://redis:6379")
    value = await redis.get("nb_click") or 0
    await redis.set("nb_click", int(value)+1)
    result = await redis.get("nb_click")
    return {"Nombre d'entrées": result}
