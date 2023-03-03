from fastapi import FastAPI
from controller import user, auth
from config import config

app = FastAPI()
app.config = config

app.include_router(user.router, prefix=f"/user")
app.include_router(auth.router, prefix=f"/auth")


