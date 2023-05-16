
# import required libraries
from pydub import AudioSegment
from pydub.playback import play
import time
import datetime

class Alarm():
    # it is not necessary to do this project with a class, but I wanted to practice using classes
    def __init__(self):
        self.alarmHour = 0 
        self.alarmMin = 0
        
    # look is you want am or pm
    def AMchecker(self):
        alarmTime = str(input("AM or PM: ")).lower()
        if alarmTime == "pm":
            self.alarmHour += 12

    def alarmChecker(self):
        # conditions setters
        self.alarmHour = int(input("Enter hour (0-12): "))
        self.alarmMin = int(input("Enter minute (0-59): "))

        if self.alarmHour > 23 or self.alarmMin > 59:
            print("Invalid time")
            return
        
        self.AMchecker()
        
        print("Alarm set for: ", self.alarmHour, ":", self.alarmMin)

        while True: # main loop
            now = datetime.datetime.now()
            if self.alarmHour == now.hour and self.alarmMin == now.minute:
                print("Wake up!")
                alarm1 = AudioSegment.from_file(file = "alarm/alarm.wav", format = "wav")
                play(alarm1)
                break

    def countDown(self):
        input_time = int(input("Enter time in seconds: "))
        while input_time >= 0:
            minutes_remaining, seconds_remaining = divmod(input_time, 60)
            timer = '{:02d}:{:02d}'.format(minutes_remaining, seconds_remaining)
            print(timer, end="\r")
            time.sleep(1)
            input_time -= 1
        alarm2 = AudioSegment.from_file(file = "alarm/alarm2.wav", format = "wav")
        play(alarm2)

    # where the alarm or countDown is setted
    def initialize(self):
        repeat = True
        while repeat:
            input_to_do = int(input("What do you want to do? \n1. Set alarm \n2. Set timer \n3. Exit \n"))
            if input_to_do == 1:
                self.alarmChecker()
            elif input_to_do == 2:
                self.countDown()
            else:
                repeat = False
                print("Exiting...")

myAlarm = Alarm()
myAlarm.initialize()
