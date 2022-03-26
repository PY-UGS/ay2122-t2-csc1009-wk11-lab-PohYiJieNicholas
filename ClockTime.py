class ClockTime:

    def setHours(self,hours):
        self.hours = hours

    def setMinutes(self,minutes):
        self.minutes = minutes

    def setSeconds(self,seconds):
        self.seconds = seconds

    def setTime(self,hours,minutes,seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def showTime(self):
        return self.hours+":"+self.minutes+":"+self.seconds


time = ClockTime()
print("Enter hour: ")
hour = input()
print("Enter minutes: ")
minutes = input()
print("Enter seconds: ")
seconds = input()


time.setHours(hour)
time.setMinutes(minutes)
time.setSeconds(seconds)
print(time.showTime())
