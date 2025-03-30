

from collections import deque
import time

lights = deque([("Red", 10), ("Green", 3), ("Yellow", 2)])

for _ in range(6): 
    color, duration = lights[0]  
    print(f"Light: {color} ({duration} sec)")
    time.sleep(duration)  
    lights.rotate(-1)  
    
