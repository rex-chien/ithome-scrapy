import requests
from datetime import time
import random

for page in range(1, 11):
    requests.get('https://ithelp.ithome.com.tw/')
    # 隨機暫停 1~5 秒
    time.sleep(random.uniform(1, 5))
