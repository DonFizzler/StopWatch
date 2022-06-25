from StopWatch import StopWatch

def TestFunc() -> int:
    index = 0
    for _ in range(10000000):
        index += 0
    return index

if __name__ == "__main__":
    Timer = StopWatch()
    Timer.Start()
    TestFunc()
    Timer.Stop()
    print(f"Elapsed time: {Timer.Elapsed} MS")