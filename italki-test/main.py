# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import csv

import requests
from bs4 import BeautifulSoup


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# from urllib.request import urlopen
#
# url = "http://www.baidu.com"
# resp = urlopen(url)
#
# with open("mybaidu.html", mode="w", encoding="utf-8") as f:
#     f.write(resp.read().decode("utf-8"))
# print("over!")


url_jay_zhou = "https://www.google.com/search?q=%E5%91%A8%E6%9D%B0%E4%BC%A6"


dic_headers = {
    # "Cookie": "ABTEST=4|1632321340|v17; IPLOC=USUS36; SUID=189A47478935990A00000000614B3F3E; SUV=1632321341394193; browerV=3; osV=1; SNUID=76F429296F6BA2F80065CFFF6F1808F4; sst0=933; ld=BZllllllll2Pv8dRlllllpVa5LtlllllS1WzplllllwlllllVklll5@@@@@@@@@@",
    # "Host": "www.sogou.com",
    # "Pragma": "no-cache",
    # "sec-ch-ua-mobile": "?0",
    # "Sec-Fetch-Dest": "document",
    # "Sec-Fetch-Mode": "navigate",
    # "Sec-Fetch-Site": "none",
    # "Sec-Fetch-User": "?1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
}

# resp = requests.get(url_jay_zhou, headers=dic_headers)
# print(resp.text)
# resp.close()

nba_player_stat_url = "https://nba.hupu.com/stats/players"
resp = requests.get(nba_player_stat_url)
print(resp.text)
resp.close()

f = open("nba球员2020-2021赛季统计数据.csv", mode="w", encoding="utf-8")

csv_writer = csv.writer(f)

page = BeautifulSoup(resp.text, "html.parser") # 指定html解析器
data_rows = page.find("table", attrs={"class": "players_table"}) # tag: "table"

trs = data_rows.findAll("tr")[1:]

for tr in trs:
    tds = tr.find_all("td")
    player_rank = tds[0].text
    player_name = tds[1].text
    player_team = tds[2].text
    print("rank: ", player_rank, "name: ", player_name)
    player_points_per_game = tds[3].text
    player_two_shoot = tds[4].text
    # player_field_percentage = tds[5].text
    # player_three_shots = tds[6].text
    # player_three_percentage = tds[7].text
    # player_free_throw = tds[8].text
    # player_free_throw_percentage = tds[9].text
    # player_free_game = tds[10].text
    # player_free_time = tds[11].text
    csv_writer.writerow([player_rank, player_name, player_team, player_points_per_game, player_two_shoot])
f.close()
print("Done")