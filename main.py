from contextlib import asynccontextmanager
from fastapi.middleware.gzip import GZipMiddleware
from fastapi import FastAPI

# Internal deps
from src.routes import routes


@asynccontextmanager
async def lifespan(app: FastAPI):
    # 1. APPLICATION START | Perform any pre-startup actions here
    print("Starting server...")

    # 2. Give way to application so it can run
    yield

    # 3. APPLICATION STOP: Run any post-shutdown actions here
    print("Server disconnected")


app = FastAPI(lifespan=lifespan)
app.add_middleware(GZipMiddleware, minimum_size=1000)
app.include_router(routes, prefix="/v1")
