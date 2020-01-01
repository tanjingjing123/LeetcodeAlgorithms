class EngineStateEvent:
    def __init__(self, state, time):
        self.state = state
        self.time = time

    def getState(self):
        return self.state

    def getTime(self):
        return self.time


class AlertProcessor:
    def __init__(self, minIdlePeriod):
        self.minIdlePeriod = minIdlePeriod
        self.lastState = None
        self.lastTime = -1
        self.lastAlert = False

    def isOverTime(self, time):
        return time - self.lastTime >= self.minIdlePeriod

    def processEvent(self, event):
        if not self.lastState:
            self.lastState = event.state
            self.lastTime = event.time
            return

        if self.lastState == "idle" and event.state != "idle":
            if self.isOverTime(event.time):
                if not self.lastAlert:
                    print("ALERT!" + str(event.time))
                print("RESOLVED!" + str(event.time))
                self.lastAlert = False
                self.lastTime = event.time
                self.lastState = event.state

        elif self.lastState == "idle" and event.state == "idle":
            if self.isOverTime(event.time):
                if not self.lastAlert:
                    print("ALERT!" + str(event.time))
                    self.lastAlert = True

        elif self.lastState != "idle" and event.state == "idle":
            self.lastState = event.state
            self.lastTime = event.time




event1 = EngineStateEvent('driving', 2)
event2 = EngineStateEvent('off', 12)
event3 = EngineStateEvent('driving', 35)
event4 = EngineStateEvent('idle', 36)
event5 = EngineStateEvent('driving', 37)
event6 = EngineStateEvent('idle', 38)
event7 = EngineStateEvent('idle', 56)
event8 = EngineStateEvent('idle', 76)
event9 = EngineStateEvent('driving', 96)
event10 = EngineStateEvent('idle', 101)
event11 = EngineStateEvent('idle', 102)
event12 = EngineStateEvent('idle', 103)
event13 = EngineStateEvent('driving', 200)
event14 = EngineStateEvent('idle', 203)
event15 = EngineStateEvent('driving', 204)

processor = AlertProcessor(15)
processor.processEvent(event1)
processor.processEvent(event2)
processor.processEvent(event3)
processor.processEvent(event4)
processor.processEvent(event5)
processor.processEvent(event6)
processor.processEvent(event7)
processor.processEvent(event8)
processor.processEvent(event9)
processor.processEvent(event10)
processor.processEvent(event11)
processor.processEvent(event12)
processor.processEvent(event13)
processor.processEvent(event14)
processor.processEvent(event15)
