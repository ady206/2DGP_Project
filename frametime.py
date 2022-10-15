import time

Start_Time = None
def SetStartTime():
    global Start_Time
    Start_Time = time.time()
    pass

def GetStartTime():
    global Start_Time
    return Start_Time

def FrameTime():
    frameTime = time.time() - GetStartTime()
    return float(frameTime)