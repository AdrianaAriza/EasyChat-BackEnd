from fastapi import APIRouter
from .login import login, logout
from .schemas import LoginResponse
from validators.error import FieldError

router = APIRouter(
    tags=["user"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)


router.add_api_route(
    "/login",
    login,
    responses={
        200: {"model": LoginResponse},
        400: {"model": FieldError}
    },
    methods=["POST"]
)

router.add_api_route(
    "/logout",
    logout,
    responses={
        200: {},
        400: {"model": FieldError}
    },
    methods=["GET"]
)