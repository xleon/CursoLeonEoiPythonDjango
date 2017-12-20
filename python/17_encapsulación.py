class MyCounter:
    __secretCount = 0

    def count(self):
        self.__internal_count()
        print(self.__secretCount)

    def __internal_count(self):
        self.__secretCount += 1

counter = MyCounter()
counter.count()
counter.count()
counter.__internal_count()
print(counter.__secretCount)