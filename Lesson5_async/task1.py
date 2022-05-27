"""1.	Using threading library to verify URL's.
В файле links.txt содержится список url-адресов которые нужно провалидироавть на доступность.

Нам необходимо наиболее эффективное решение. Используйте библиотеку threading, чтобы инициировать множество web-запросов одновременно.
Результат выполнения скрипта сохраните в файл в формате JSON (см. пример ниже)

Примечание:
•	Используйте библиотеку requests (pip install requests)
•	Проперти Response.ok может быть полезной для определения валидности респонза (github/requests)
Пример результата:

[
  {
    "url": "https://www.does_not_exist.com/",
    "is_ok": false,
    "status_code": null
  },
  {
    "url": "http://lucumr.pocoo.org/",
    "is_ok": true,
    "status_code": 200
  },
  {
    "url": "http://jinja.pocoo.org/docs/",
    "is_ok": true,
    "status_code": 200
  }
]
"""
from threading import Thread
import requests
import os
import json
from timeit import timeit
import aiohttp
import asyncio

response_list = []
threads = []


def get_connection(request_url):
    try:
        r = requests.get(request_url)
        # r.raise_for_status() # <---- Exception is to general
    except Exception as e:
        print(f"Exception is raised for {e}")
        is_ok = False
        status_code = None
    else:
        is_ok = r.ok
        status_code = r.status_code
    r_obj = {"url": request_url, "is_ok": is_ok, "status_code": status_code}
    response_list.append(r_obj)


def main_():
    lines = [] 
    with open(os.getcwd() + "/links.txt", "r") as data_urls:
        lines.extend(data_urls.readlines())
    
    for line in lines:
        url = line.rstrip("\n")
        t = Thread(target=get_connection, args=(url,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
      
    with open("url_results.json", "w") as data_json:
        json.dump(response_list, fp=data_json, indent=2)
        print(f"{data_json.name} is created in current directory")

async def main():
    lines = [] 
    with open(os.getcwd() + "/links.txt", "r") as data_urls:
        lines.extend(data_urls.readlines())

    async with aiohttp.ClientSession() as session:
        is_ok = False
        status_code = None
        async def get(request_url):
            try:
                async with session.get(request_url) as response:
                    is_ok = response.ok
                    status_code = response.status
            except Exception as exc:
                print(f"Exception is raised for {exc}")
                is_ok = False
                status_code = None
            else:
                is_ok = 'ok'
                status_code = 'status_code'
                r_obj = {"url": request_url, "is_ok": is_ok, "status_code": status_code}
                response_list.append(r_obj)
        
        tasks = [get(line.rstrip("\n")) for line in lines]
        await asyncio.gather(*tasks)

    with open("url_results.json", "w") as data_json:
        json.dump(response_list, fp=data_json, indent=2)
        print(f"{data_json.name} is created in current directory")
                
        

    

if __name__ == "__main__":
    time_ = timeit(lambda: main_(), number=3)
    print(time_)
