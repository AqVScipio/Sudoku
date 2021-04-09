import time

class Timer:
    def __init__(self):
        self.__paused = False
        self.__timePassed = 0
        self.resume()

    def getTimePassedSinceStart(self):
        if not self.__paused:
            self.__timePassed = int(time.time() - self.__startTime)
        return str(self.__timePassed)

    def pause(self):
        self.__paused = True

    def resume(self):
        self.__startTime = time.time() - self.__timePassed
        self.__paused = False

    def isPaused(self):
        return self.__paused