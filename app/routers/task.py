# Import
from fastapi import APIRouter, Depends, status, HTTPException, FastAPI
# Сессия БД
from sqlalchemy.orm import Session
# Функция подключения к БД
from app.backend.db_depends import get_db
# Аннотации, Модели БД и Pydantic.
from typing import Annotated
from app.models.user import User
from app.schemas import CreateUser, UpdateUser
# Функции работы с записями.
from sqlalchemy import insert, select, update, delete
# Функция создания slug-строки
from slugify import slugify

router = APIRouter(prefix='/task', tags=['task'])



# GET
@router.get('/')
async def all_tasks():
  pass

@router.get('/task_id')
async def task_by_id():
  pass


# POST
@router.post('/create')
async def create_task():
  pass


# PUT
@router.put('/update')
async def update_task():
  pass


# DELETE
@router.put('/delete')
async def delete_task():
  pass