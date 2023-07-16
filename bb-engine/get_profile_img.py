import asyncio
from itertools import cycle
import random
import aiohttp
from bs4 import BeautifulSoup
import json


proxy_list = cycle([
    'http://xuser1356:pass2356@216.170.122.111:6149',
    'http://xuser1356:pass2356@216.170.122.97:6135',
    'http://xuser1356:pass2356@45.196.33.88:6069',
    'http://xuser1356:pass2356@154.194.16.89:6008',
    'http://xuser1356:pass2356@45.196.52.190:6205',
    'http://xuser1356:pass2356@193.160.83.178:6499',
    'http://xuser1356:pass2356@154.194.24.186:5796',
    'http://xuser1356:pass2356@45.196.63.92:6726',
    'http://xuser1356:pass2356@192.46.200.219:5889',
    'http://xuser1356:pass2356@45.196.52.174:6189',
    'http://xuser1356:pass2356@192.53.137.0:6288',
    'http://xuser1356:pass2356@154.194.16.213:6132',
    'http://xuser1356:pass2356@45.196.54.246:6825',
    'http://xuser1356:pass2356@192.53.69.55:6693',
    'http://xuser1356:pass2356@185.253.122.209:6018',
    'http://xuser1356:pass2356@185.253.122.150:5959',
    'http://xuser1356:pass2356@185.253.122.249:6058',
    'http://xuser1356:pass2356@193.160.83.184:6505',
    'http://xuser1356:pass2356@193.160.82.26:5998',
    'http://xuser1356:pass2356@193.160.82.36:6008' 
])

headers_list = [
    {
        "Connection": "keep-alive",
        "DNT": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
    },
    {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", 
        "Accept-Encoding": "gzip, deflate", 
        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8", 
        "Dnt": "1", 
        "Host": "httpbin.org", 
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36", 
    },
    {
        "Connection": "keep-alive",
        "DNT": "1",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_1_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.1 Mobile/15E148 Safari/604.1",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
    },
    {
        "Connection": "keep-alive",
        "DNT": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9"
    },
    {
        "Connection": "keep-alive",
        "DNT": "1",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:89.0) Gecko/20100101 Firefox/89.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.5"
    },
    {
        "Connection": "keep-alive",
        "DNT": "1",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1 Safari/605.1.15",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-us"
    }
]

BASE_URL = "https://space.bilibili.com/{}"
# CONCURRENT_REQUESTS = 10

# async def send_request(user_dict, semaphore):
#     async with semaphore:
#         url = BASE_URL.format(user_dict['mid'])
#         print("*****url:*****", url)
#         proxy = next(proxy_list)
#         headers = random.choice(headers_list)
#         async with aiohttp.ClientSession(headers=headers) as session:
#             async with session.get(url, proxy=proxy) as response:
#                 # 处理响应
#                 content = await response.text()
#                 print("*****content:*****", content)
#                 # 创建一个BeautifulSoup对象，解析HTML内容
#                 soup = BeautifulSoup(content, 'html.parser')

#                 # 解析URL
#                 link_element = soup.find('link', rel='apple-touch-icon')
#                 print("==== link_element ====: ", link_element)
#                 href = link_element['href']
                
#                 # 将href添加到输入的字典中
#                 user_dict['href'] = href
#                 return user_dict

# async def main(users):
#     semaphore = asyncio.Semaphore(CONCURRENT_REQUESTS)
#     tasks = []
#     for user_dict in users:
#         task = asyncio.create_task(send_request(user_dict, semaphore))
#         tasks.append(task)

#     results = await asyncio.gather(*tasks)
#     return results

import concurrent.futures
import requests
from bs4 import BeautifulSoup

SPACE_URL = "https://space.bilibili.com/{}"
FOLLOWERS_URL = "https://api.bilibili.com/x/relation/stat?vmid={}"
CONCURRENT_REQUESTS = 5

def get_profile_img(user_dict, proxy):
    url = SPACE_URL.format(user_dict['mid'])
    headers = random.choice(headers_list)
    
    max_retries = 3
    for _ in range(max_retries):
        response = requests.get(url, proxies={"http": proxy, "https": proxy}, headers=headers)
        if response.status_code == 200:
            break
    else:
        print(f"Failed to get response from {url} after {max_retries} attempts.")
        return None

    content = response.text
    soup = BeautifulSoup(content, 'html.parser')
    link_element = soup.find('link', rel='apple-touch-icon')
    
    if link_element is not None:
        href = link_element['href']
        user_dict['face'] = href + '@240w_240h_1c_1s_!web-avatar-space-header.avif'
    else:
        print(f"No link element found in {url}")
        return None

    return user_dict


import json

def get_followers(user_dict, proxy):
    url = FOLLOWERS_URL.format(user_dict['mid'])
    print("*****url:*****", url)
    headers = random.choice(headers_list)
    response = requests.get(url, proxies={"http": proxy, "https": proxy}, headers=headers)
    content = response.text
    print("*****content:*****", content)

    try:
        data = json.loads(content)  # 尝试解析为JSON格式
        user_dict['follower'] = data['data']['follower']
    except json.JSONDecodeError as e:
        print("JSONDecodeError:", e)
        # 处理JSON解析错误
        # 可以将user_dict['follower']设置为默认值或进行其他适当的处理

    return user_dict


def main(users, proxies=proxy_list):
    with concurrent.futures.ThreadPoolExecutor(max_workers=CONCURRENT_REQUESTS) as executor:
        futures = []
        for user_dict, proxy in zip(users[10: 13], proxies):
            future = executor.submit(get_followers, user_dict, proxy)
            futures.append(future)
        
        results = []
        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            results.append(result)
        
        return results
