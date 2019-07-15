#Backend code for travel scheduler.

import googlemaps
import gmaps.datasets
import datetime

class event:

    #Initializations
    def __init__(self,myEventName,myEventStartTime,myEventEndTime,myEventAddress):
        self.eventName = myEventName
        self.eventStartTime = myEventStartTime
        self.eventEndTime = myEventEndTime
        self.eventAddress = myEventAddress

    #Sets and Gets for Data
    def getEventName(self):
        return self.eventName
    def getEventStartTime(self):
        return self.eventStartTime
    def getEventEndTime(self):
        return self.eventEndTime
    def getEventAddress(self):
        return self.eventAddress
    def setEventName(self, myEventName):
        eventName = myEventName
    def setEventStartTime(self, myEventStartTime):
        eventStartTime = myEventStartTime
    def setEventEndTime(self, myEventEndTime):
        eventEndTime = myEventEndTime
    def setEventAddress(self, myEventAddress):
        eventAddress = myEventAddress

class calendar:

    #Initializations
    def __init__(self):
        self.eventList = []
    def __init__(self, myEventList):
        self.eventList = myEventList

    #Sets and Gets for Data
    def getEventList(self):
        return self.eventList
    def getEvent(self, position):
        return self.eventList[position]
    def setEventList(self,myEventList):
        self.eventList = myEventList
    def setEvent(self, position, myEvent):
        self.eventList[position]=myEvent

    #Functions
    def addEvent(self, myEvent):
        self.eventList.append(myEvent)
    def removeEvent(self, myEvent):
        self.eventList.remove(myEvent)
    def removeEventPos(self, position):
        self.eventList.pop(position)

class user:
    #Initialization
    def __init__(self, myUserName, myUserLocation, myUserCalendar, myTimeOffset):
        self.userName = myUserName
        self.userLocation = myUserLocation
        self.userCalendar = myUserCalendar
        self.timeOffset = myTimeOffset
        self.api_key='AIzaSyAAh17kTnOqfm-HlAJmi42tU4l6slYmhYE'

    #Sets and Gets for Data
    def getAPI(self):
        return self.api_key
    def getUserName(self):
        return self.userName
    def getUserLocation(self):
        return self.userLocation
    def getUserCalendar(self):
        return self.userCalendar
    def getTimeoffset(self):
        return self.timeOffset
    def setAPI(self, myAPI):
        self.api_key = myAPI
    def setUserName(self, myUserName):
        self.userName = myUserName
    def setUserLocation(self, myUserLocation):
        self.userLocation = myUserLocation
    def setUserCalendar(self, myUserCalendar):
        self.userCalendar = myUserCalendar
    def setTimeoffset(self, myTimeOffset):
        self.timeOffset = myTimeOffset

    #Functions
    def getTTL(self,eventPosition):
        myEvent = self.userCalendar.getEvent(eventPosition)
        gmaps = googlemaps.Client(key=self.api_key)
        now = datetime.datetime.now()
        results = gmaps.directions(self.userLocation, myEvent.getEventAddress(), mode="driving", departure_time=now)
        return myEvent.eventStartTime - datetime.timedelta(seconds=results[0]['legs'][0]['duration']['value']) - self.timeOffset

#Example Usage
myEvent = event("Dinner at Chipotle", datetime.datetime(2018, 7, 16, 17), datetime.datetime(2018, 7, 16, 18), "258 Stetson St, Cincinnati, OH 45219")
myOtherEvent = event("Dinner at Chipotle 2", datetime.datetime(2018, 7, 21, 17), datetime.datetime(2018, 7, 21, 18), "258 Stetson St, Cincinnati, OH 45219")
myEventList = [myEvent]
myCalendar = calendar(myEventList)
myCalendar.addEvent(myOtherEvent)
myUser = user("Mathew", "237 Calhoun St, Cincinnati, OH 45219", myCalendar, datetime.timedelta(minutes=15))
print("You should leave at " + myUser.getTTL(0))

#To do list/in other code (I will handle these):
# - Try Catch Error Handling
# - Pulling from and pushing to database
# - Better Event Handling
