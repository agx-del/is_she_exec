import datetime


class Count():
    def __init__(self):
        self.stChangeCnt = 2
        self.lastState = None
        self.stateContinueCnt = 0
        self.stateChangeContinueCnt = 0
        self.stateTrueSumSec = 0
        self.stateFalseSumSec = 0
        self.lastTime = datetime.datetime.now()

    def setState(self, st):
        if self.lastState == None:  # 初始化
            self.lastState = st
        # print("setState(), last/cur state is: %s/%s" %
        #      (self.lastState, st), end=", ")
        secDuring = self.getSecDuring()
        #print("setState(): secDuring:%d" % secDuring)
        if self.lastState == st:
            self.stateContinueCnt += 1
            self.sumDuring(self.lastState, secDuring)  # 状态未改变，累加对应状态的记时
        else:
            # 进入此则表示状态实际已发生转换，后续主要排除抖动因素
            self.stateChangeContinueCnt += 1
            if self.stateChangeContinueCnt >= self.stChangeCnt:
                # 如果连续变化次数大于阈值，才算做状态改变，并重置所有状态计数
                # print(
                #    "\nsetState(): self.stateChangeContinueCnt >= self.stChangeCnt is True ")
                self.lastState = st
                self.stateContinueCnt = 1
                self.stateChangeContinueCnt = 0
            else:
                # 虽然状态有改变，但仍在抖动幅度内，不算做状态真实变化，所以继续累加原状态的记时
                self.sumDuring(self.lastState, secDuring)

    def getSecDuring(self):
        secondDuring = (datetime.datetime.now()-self.lastTime).seconds
        self.lastTime = datetime.datetime.now()
        return secondDuring

    def sumDuring(self, validSt, secDuring):
        if validSt == True:
            self.stateTrueSumSec += secDuring
            #print("adding  True")
        else:
            self.stateFalseSumSec += secDuring
            #print("adding  False")
        # print("sumDuring():True:%d,False:%d" %
        #      (self.stateTrueSumSec, self.stateFalseSumSec))

    def getStateDuring(self, st):
        #print("St:%s during is %d" % (True, self.stateTrueSumSec))
        #print("St:%s during is %d" % (False, self.stateFalseSumSec))
        if st == True:
            return self.stateTrueSumSec
        else:
            return self.stateFalseSumSec

    def getLastState(self):
        if self.lastState == None:  # 初始化
            return False
        else:
            return self.lastState


if __name__ == "__main__":
    cnt = Count()
    cnt.setState(True)

    for i in range(1, 25000000):
        pass
    cnt.setState(True)

    for i in range(1, 25000000):
        pass
    cnt.setState(True)

    for i in range(1, 25000000):
        pass
    cnt.setState(False)

    for i in range(1, 25000000):
        pass
    cnt.setState(False)

    for i in range(1, 25000000):
        pass
    cnt.setState(False)

    for i in range(1, 25000000):
        pass
    cnt.setState(True)

    for i in range(1, 25000000):
        pass
    cnt.setState(True)

    for i in range(1, 25000000):
        pass
    cnt.setState(True)

    cnt.getStateDuring(True)
