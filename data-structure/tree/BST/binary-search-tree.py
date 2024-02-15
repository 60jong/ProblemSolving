import requests
import time

start = time.time()
response = requests.get("http://localhost:8888/posts")
print('elapsed :', time.time() - start)
print(response.text)