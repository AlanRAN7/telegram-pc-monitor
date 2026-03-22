import time
import psutil


psutil.cpu_percent()          # discard first call
time.sleep(0.5)
print(psutil.cpu_percent())   # meaningful value