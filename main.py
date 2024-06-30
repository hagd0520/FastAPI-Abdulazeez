from contextlib import asynccontextmanager
from fastapi import FastAPI
from starlette.responses import RedirectResponse
import uvicorn

from db.connection import conn
from routes.users import user_router
from routes.events import event_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    conn()
    yield
    
    
app = FastAPI(lifespan=lifespan)

app.include_router(user_router)
app.include_router(event_router)


@app.get("/")
async def home():
    return RedirectResponse(url="/event/")


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)