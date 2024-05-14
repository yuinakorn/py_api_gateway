from fastapi import APIRouter, Depends
from controllers import query_controller

from utils.oauth2 import access_user_token

router = APIRouter(prefix="/query", tags=["query"])


@router.get("/all_client/", dependencies=[Depends(access_user_token)])
def get_status_all():
    return query_controller.get_status_all()


@router.get("/status/{hoscode}", dependencies=[Depends(access_user_token)])
def get_status_by_hoscode(hoscode: str):
    return query_controller.get_status_by_hoscode(hoscode)

