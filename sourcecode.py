import random
import time
tick = 0
while(True):
	tick = tick + 1
	sleep = random.randint(0, 1000)
	time.sleep(sleep/1000)
	print("Tick", tick, "Time_Used", sleep, "ms")
