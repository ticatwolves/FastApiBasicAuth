"""FastAPI Authentication Module

A reusable authentication and user management module for FastAPI applications.
"""
__version__ = "0.1.0"
from fastapi import FastAPI
from .api.v1.user import users_router


def configure_auth_routes(fast_api_app, prefix: str = "/", tags: list = None):
    """
    Configure authentication routes on a FastAPI app

    Args:
        fast_api_app: FastAPI application instance
        prefix: URL prefix for auth routes
        tags: OpenAPI tags for the routes
    """
    if tags is None:
        tags = [""]
    fast_api_app.include_router(users_router, prefix=prefix, tags=tags)


app = FastAPI()
configure_auth_routes(app, prefix="/accounts", tags=["users"])
