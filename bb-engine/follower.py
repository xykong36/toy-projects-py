# from bilibili_api import user, sync

# u = user.User(660303135)
# # print(u.get_relation_info())

# print(sync(u.get_relation_info()))
# print(sync(u.get_user_info()))

# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# import json

# app = FastAPI()

# origins = [
#     "chrome-extension://hiehibifnfkcajcihldapggjbnelkogm",
# ]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # 用于测试的接口
# @app.get("/")
# async def root():
#     return {"message": "Hello World from FastAPI"}

# @app.get("/search")
# def search_value(author: str):
#     # 从 bb.json 文件中查找 author 对应的值
#     with open('res-play_100k_2_authors_r500_new_30-zh.json') as f:
#         data = json.load(f)
    
#     if author in data:
#         return data[author]
#     else:
#         return '没有找到结果'

# with open('res-play_100k_2_authors_r500_new_30-zh.json') as f:
#     data = json.load(f)
    
# if author in data:
#     return data[author]
# else:
#     return '没有找到结果'

import concurrent.futures
from bilibili_api import user, sync

def get_user_info(uid):
    u = user.User(uid)
    return sync(u.get_user_info())

# 列表中包含了你想要查询的用户ID
uids = [4401694, 404204597, 11739937, 15639667]

with concurrent.futures.ThreadPoolExecutor() as executor:
    # 使用线程池并发地获取每个用户的信息
    user_infos = list(executor.map(get_user_info, uids))


for user_info in user_infos:
    print(user_info)
