class Time:

    def __init__(self,hour=0, minute=0, second=0):

        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return "{}:{:02d}:{:02d}".format(self.hour,
                self.minute,self.second)

    def __add__(self, other_time):

        new_time = Time()

        if (self.second + other_time.second) >= 60:
            self.minute += 1
            new_time.second = (self.second + other_time.second) - 60

        else:
            new_time.second = self.second + other_time.second

        if (self.minute + other_time.minute) >= 60:
            self.hour += 1
            new_time.minute = (self.minute + other_time.minute) - 60

        else:
            new_time.minute = self.minute + other_time.minute

        if (self.hour + other_time.hour) > 24:
            new_time.hour = (self.hour + other_time.hour) - 24

        else:
            new_time.hour = self.hour + other_time.hour

        return new_time


    def __sub__(self, other_time):

        new_time = Time()

        if self.second < other_time.second:
            self.minute -= 1
            new_time.second = 60 - (other_time.second - self.second)

        else:
            new_time.second = self.second - other_time.second


        if self.minute < other_time.minute:
            self.hour -= 1
            new_time.minute = 60 - (other_time.minute - self.minute)

        else:
            new_time.minute = self.minute - other_time.minute


        if (self.hour < other_time.hour):
            new_time.hour = (self.hour - other_time.hour) + 24
            print("New day")

        else:
            new_time.hour = self.hour - other_time.hour

        return new_time

def main():
        time1 = Time(6,10,20)

        print(time1)

        time2 = Time(4,11,21)
        print(time2)

        print(time1 + time2)
        print(time1 - time2)



main()
