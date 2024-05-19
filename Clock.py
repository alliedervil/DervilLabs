from Counters import Time

# Our implementation of the Clock class 
class Clock: 

    def getTime(self):
        return Time.getTime()

    def setTime(self, timetuple):
        Time.setTime(timetuple)

    #return the current hour as an INT
    def getHour(self):
        timetuple = Time.getTime()
        return timetuple[3]

    # sets the RTC hour to the hour parameter 
    def setHour(self, hour):
        # first get the current time from the system
        timetuple = Time.getTime()
        # then convert the tuple into a list
        timelist = list(timetuple)
        # change the hour to the new hour 
        timelist[3] = hour 
        # save it back to the system 
        Time.setTime(timelist)

    def getMinute(self):
        timetuple = Time.getTime()
        return timetuple[4]

    def setMinute(self, minute):
        timetuple = Time.getTime()
        timelist = list(timetuple)
        timelist[4] = minute
        Time.setTime(timelist) 