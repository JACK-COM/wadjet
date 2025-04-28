"""
Project `FastAPI` router instance. Import and embed subrouters in it.

EXAMPLE:

from .auth import router as authRouter

routes.include_router(authRouter)
"""

from fastapi import APIRouter

routes = APIRouter()
""" FastAPI router instance for routing to server endpoints """
