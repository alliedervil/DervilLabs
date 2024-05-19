from Displays import LCDDisplay
from Button import * 
from Clock import * 


months = { 1: "Jan", 2: "Feb", 3: "Mar", 4: "Apr", 5: "May", 6: "Jun", 7: "Jul", 8: "Aug", 9: "Sep", 10: "Oct", 11: "Nov", 12: "Dec"}


class ClockController:
    # our implementation of the Clock Controller 
    # 4 buttons for setting month, data, hour, min 
    # LCD Display to show time 

    def __init__(self):
        self._clock = Clock()
        self._display = LCDDisplay(sda=0, scl=1, i2cid=0)
        self._buttons = [Button(10,'white',buttonhandler=self),
                        Button(11,'red',buttonhandler=self),
                        Button(12,'yellow',buttonhandler=self),
                        Button(13,'blue',buttonhandler=self)]

    def showTime(self):
        # show the time on the display  
        #(year, month, date, hour, minute, sec, wd, yd) = self._clock.getTime()

        (year, month, date, hour, minute, sec, wd, yd) = self._clock.getTime()
        
        month_name = months.get(month)

        self._display.showText(f'{month_name} {date:02} {hour:02}:{minute:02}:{sec:02} \nHave a great day')
         

    def buttonpressed(self, name):
        if name == 'yellow': 
            #get the current hour 
            now = Clock.now()
            #set the hour to 1 + the current hour
            self._clock.setHour(hour + 1)

        if name == 'white':
            now = Clock.now()
            self._clock.setMonth(month +1)

        if name == 'red':
            now = Clock.now()
            #Date of the month
            self._clock.setDom(Dom +1)

        if name == 'blue':
            now = Clock.now()
            self._clock.setMinute(Minute +1)

    def buttonReleased(self,name):
        return (self._lowActive and self._pin.value() ==0) or (not self._lowActive and self._pin.value() == 1)


