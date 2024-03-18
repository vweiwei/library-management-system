"""
@Time : 2021/7/4 11:53 AM
@Author : Xiaoming
采用pydantic读取环境变量，初始化部分参数
"""
from pydantic import BaseSettings


class Settings(BaseSettings):
    mongo_uri: str = 'mongodb://localhost:27017'
    mongodb_name: str = 'ClassroomManager'
    # collection: str = 'user'


settings = Settings()
