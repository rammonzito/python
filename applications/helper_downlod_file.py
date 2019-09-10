import requests


# requests.get('https://api.github.com/user', auth=requests.auth.HTTPBasicAuth('user', 'pass'))

url = 'https://readthedocs.org/projects/python-guide/downloads/pdf/latest/'
myfile = requests.get(url, allow_redirects=True)
open('C:/Lab/python/applications/downloaded.pdf', 'wb').write(myfile.content)


# import os
# import urllib.request
# import asyncio

# async def coroutine(url):
#     r = urllib.request.urlopen(url)
#     filename = "couroutine_downloads.txt"
#     with open(filename, 'wb') as f:
#         for ch in r:
#             f.write(ch)
#     print_msg = 'Successfully Downloaded'
#     return print_msg

# async def main_func(urls_to_download):
#     co = [coroutine(url) for url in urls_to_download]
#     downloaded, downloading = await asyncio.wait(co)
#     for i in downloaded:
#         print(i.result())
# urls_to_download = ["https://www.python.org/events/python-events/801/", 
# "https://www.python.org/events/python-events/790/", 
# "https://www.python.org/events/python-user-group/816/", 
# "https://www.python.org/events/python-events/757/"]

# eventLoop = asyncio.get_event_loop()
# eventLoop.run_until_complete(main_func(urls_to_download))