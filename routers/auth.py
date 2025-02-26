# from typing import Annotated

from fastapi import APIRouter  # , Form, Request, status

# from fastapi.responses import RedirectResponse
from icecream import ic
from misc.usermanager import auth_backend, fastapi_users
from schemas.models import User, UserCreate  # , UserLog, UserReg

router = APIRouter(prefix="/auth", tags=["Auth"])


# @router.post("/log", tags=["Redirect"])
# async def log(form_data: Annotated[UserLog, Form()], request: Request):
#     data = form_data.model_dump()
#     responce = await arequest("post", f"{request.base_url}auth/login/", data=data)
#     if not responce.ok:
#         ic(responce.status, responce.reason)
#         return RedirectResponse(f"{request.base_url}auth/", 303)
#     cookie_value = (
#         responce.cookies["fastapiusersauth"]
#         .OutputString()
#         .split("=", maxsplit=1)[1]
#         .split(";")[0]
#     )
#     responce = RedirectResponse("/competitions/", status_code=status.HTTP_303_SEE_OTHER)
#     responce.set_cookie("fastapiusersauth", cookie_value)
#     return responce


# @router.post("/reg", tags=["Redirect"])
# async def reg(form_data: Annotated[UserReg, Form()], request: Request):
#     data = form_data.model_dump()
#     responce = await arequest("post", f"{request.base_url}auth/register/", json=data)
#     if not responce.ok:
#         ic(responce.status, responce.reason)
#         return RedirectResponse(f"{request.base_url}auth/", 303)
#     return await log(
#         UserLog(username=data["email"], password=data["password"]), request
#     )


router.include_router(fastapi_users.get_register_router(User, UserCreate))
router.include_router(fastapi_users.get_auth_router(auth_backend))
