from fastapi import APIRouter, HTTPException

from app.api.utils.persons import *
from app.api.schemas.persons import *

persons_router = APIRouter(tags=["Persons"])