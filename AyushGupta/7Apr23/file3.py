# Decorator funtion
# Calculate the time taken by the function using decorator

import time
def time_taken(fx):
    def mfx():
        start = time.perf_counter()
        fx()
        end = time.perf_counter()
        print("Time Taken =",end-start)
    return mfx

@time_taken
def add(x=2, y=5):
    print("Addition =",x+y)
add()