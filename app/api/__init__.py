from fastapi import APIRouter
from .redditapi import subfeddit_router
# TODO: import your modules here.

api_router = APIRouter()
api_router.include_router(subfeddit_router, tags=["reddit"])