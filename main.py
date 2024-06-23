from fastapi import FastAPI
import uvicorn

from routes.users import user_router
from routes.events import event_router


app = FastAPI()

app.include_router(user_router)
app.include_router(event_router)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)