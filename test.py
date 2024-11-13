import requests
from SECRET import API_KEY
import datetime
import time

start = time.time()

deg = int

def conv_deg_to_ws(deg):
    if 337 <= deg <= 360 or 0 <= deg <= 22:
        return 'N'
    elif 22 <= deg <= 67:
        return 'NW'
    elif 67 <= deg <= 112:
        return 'W'
    elif 112 <= deg <= 157:
        return 'SW'
    elif 157 <= deg <= 202:
        return 'S'
    elif 202 <= deg <= 247:
        return 'SE'
    elif 247 <= deg <= 292:
        return 'E'
    elif 292 <= deg <= 337:
        return 'NE'


end = time.time()
print(end - start)