from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json
import get_profile_img
import asyncio

app = FastAPI()

origins = [
    "chrome-extension://hiehibifnfkcajcihldapggjbnelkogm",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 用于测试的接口
@app.get("/")
async def root():
    return {"message": "Hello World from FastAPI"}

@app.get("/search")
def search_value(author: str):
    user_profile_dict = {}
    res = []
    
    # 从 bb.json 文件中查找 author 对应的值
    with open('res-play_100k_2_authors_r500_new_30-zh.json') as f:
        authors_list = json.load(f)
        author_names = list(authors_list.keys())
    with open('user_info.json') as user_file:
        user_info_list = json.load(user_file)

    if author in author_names:
        for user in user_info_list:
            if 'face' in user and 'top_photo' in user and 'sign' in user:
                user_profile_dict[user['mid']] = {'face': user['face'], 'top_photo': user['top_photo'], 'sign': user['sign']}
        similar_authors = authors_list[author]
        
        for similar_author in similar_authors:
            similar_author_mid = similar_author['mid']
            author_profile = similar_author
            if similar_author_mid in user_profile_dict:
                user_profile = user_profile_dict[similar_author_mid]
                similar_author.update(user_profile)
                res.append(similar_author)
        print("res", res)
        return res
    else:
        return '没有找到结果'
