from fastapi import FastAPI

app = FastAPI()


from routers.myAppRouters import router1, router2

app.include_router(router1, prefix="/api", tags=["r1"])
app.include_router(router2, prefix="/info", tags=["r2"])

from utils import middlewares