import time

class StopWatch:
    def __init__(self) -> None:
        self.Elapsed = 0
        self.StartTimeStamp = 0
        self.IsRunning = False
    
    def Start(self) -> None:
        if not self.IsRunning:
            self.StartTimeStamp = self.GetTimeStamp()
            self.IsRunning = True

    def StartNew(self) -> None:
        self.Elapsed = 0
        self.StartTimeStamp = self.GetTimeStamp()
        self.IsRunning = True          

    def Stop(self) -> None:
        if self.IsRunning:
            self.Elapsed = round((self.GetTimeStamp() - self.StartTimeStamp)  * 1000)
            self.IsRunning = False

    def Reset(self) -> None:
        self.Elapsed = 0
        self.StartTimeStamp = 0
        self.IsRunning = False
    
    def Restart(self) -> None:
        self.Elapsed = 0
        self.StartTimeStamp = self.GetTimeStamp()
        self.IsRunning = True

    def GetTimeStamp(self) -> float:
        return time.time()



