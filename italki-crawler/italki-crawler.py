import requests
from bs4 import BeautifulSoup

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('itaki-crawler')


url_ashtyn = "https://api.italki.com/api/v2/teacher/9075328"

url_teacher_api = "https://api.italki.com/api/v2/teachers"

# data_raw = {
#     "teacher_info": {"origin_country_id": ["US"]},
#     "teach_language": {"language": "english"},
#     "page_size": 20,
#     "page": 3
# }
#
# crawler_headers = {
#     "authority": "api.italki.com",
#     "x-browser-key": "770cdb52-a1c0-47ef-8419-b2c411c6aa1f",
#     "accept": "application/json, text/plain, */*",
#     "content-type": "application/json;charset=UTF-8",
#     "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
#     "origin": "https://www.italki.com",
#     "sec-fetch-site": "same-site",
#     "sec-fetch-mode": "cors",
#     "referer": "https://www.italki.com/",
#     "accept-language": "en-US,en;q=0.9"
# }


headers = {
    'authority': 'api.italki.com',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'x-browser-key': '770cdb52-a1c0-47ef-8419-b2c411c6aa1f',
    'accept': 'application/json, text/plain, */*',
    'x-device': '10',
    'sec-ch-ua-mobile': '?0',
    'content-type': 'application/json;charset=UTF-8',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
    'origin': 'https://www.italki.com',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.italki.com/',
    'accept-language': 'en-US,en;q=0.9',
    'connection': 'keep-alive'
}

data = '{"teacher_info":{"origin_country_id":["US"]},"teach_language":{"language":"english","is_native":1},"page_size":20,"page":1}'

resp = requests.post('https://api.italki.com/api/v2/teachers', headers=headers, data=data)

resp_json = resp.json()


resp.text
print(resp.text)