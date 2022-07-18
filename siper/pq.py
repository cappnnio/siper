from datetime import datetime

import requests
from pyquery import PyQuery as pq
import re
import io

url = 'https://ssr1.scrape.center/'
html = requests.get(url).text
doc = pq(html)
items = doc('.el-card').items()
file = open('movies.txt', 'w', encoding='utf-8')

for item in items:
    # 电影名称
    name = item.find('a > h2').text()
    # file.write(f'名称∶{name}\n')
    # 类别
    categories = [item.text() for item in item.find('.categories button span').items()]
    # file.write(f'类别∶{categories}\n')
    longtime = item.find('.info:contains(分钟)').text()
    print(longtime)
    longtime1 = longtime.split("/")[1]
    print(longtime1)
    longaddress = longtime.split("/")[0]
    print(longaddress)
    # 上映时间
    published_at = item.find('.info:contains(上映)').text()
    print(published_at)

    # published_at =  re.search('(\d{4} - \d{2} - \d{2})', published_at).group(1) if published_at and  re.search('\d{4} - \d{2} - \d{2}', published_at).group(1) else None
    published_at = re.search('(\d{4}-\d{2}-\d{2})', published_at).group(1) if published_at and re.search(
        '\d{4}-\d{2}-\d{2}', published_at) else None
    # published_at = str(published_at[0-10])
    print(published_at)
    # file.write(f'上架时间∶{published_at}\n')
    # 评分
    score = item.find('p.score').text()
    with open('movies.txt', 'w', encoding='utf-8'):
        file.write(f'名称;{name}\n')
        file.write(f'类别∶{categories}\n')
        file.write(f'上映时间∶{published_at}\n')
        file.write(f'时长∶{longtime1}\n')
        file.write(f'产地∶{longaddress}\n')

        file.write(f'评分∶{score}\n')
        file.write(f'====================================\n')

    # file.write(f'评分∶{score}\n')
    # file.write(f'{"=" * 50}\n')
#     print('datetime' )
# file.close()
print("ok")