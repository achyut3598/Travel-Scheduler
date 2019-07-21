#Backend code for travel scheduler.

import googlemaps
import gmaps.datasets
import datetime
import pyodbc

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

class database:
    #Initialization
    def __init__(self, myServer, myDatabase, myUsername, myPassword):
        self.server = myServer
        self.database = myDatabase
        self.username = myUsername
        self.password = myPassword
        self.driver= '{ODBC Driver 17 for SQL Server}'
        self.cnxn = pyodbc.connect('DRIVER='+self.driver+';SERVER='+self.server+';PORT=1433;DATABASE='+self.database+';UID='+self.username+';PWD='+ self.password)
        self.cursor = self.cnxn.cursor()

    def getEventList(self,myUsername):
        self.cursor.execute("select EventID, EventName, Username, ToAddress, FromAddress, StartTime, EndTime FROM Event WHERE Username = ?", myUsername)
        rows = self.cursor.fetchall()
        #Print out statement for testing only
        for row in rows:
            print(row.EventID, row.EventName, row.Username, row.ToAddress, row.FromAddress, row.StartTime, row.EndTime)
        #Print out statement for testing only
        return rows

    def addEvent(self, myEventName, myUsername, myToAddress, myFromAddress, myStartTime, myEndTime):

        #Grabbing Event ID Field
        self.cursor.execute("select TOP 1 EventID FROM Event ORDER BY EventID DESC")
        row = self.cursor.fetchone()
        myEventID = row.EventID + 1

        #Input Check
        addCheck = True
        if(len(myEventName) > 50):
            addCheck = False
        if(len(myUsername) > 20):
            addCheck = False
        if(len(myToAddress) > 100):
            addCheck = False
        if(len(myFromAddress) > 100):
            addCheck = False
        if(len(str(myStartTime)) != 19):
            addCheck = False
        if(len(str(myEndTime)) != 19):
            addCheck = False
        if(addCheck == True):
            self.cursor.execute("INSERT INTO Event(EventID, EventName, Username, ToAddress, FromAddress, StartTime, EndTime) values (?,?,?,?,?,?,?) ",myEventID,myEventName,myUsername,myToAddress,myFromAddress,myStartTime,myEndTime)
            self.cnxn.commit()

    #Returns hashed/salted password
    def getPassword(self, myUsername):
        self.cursor.execute("select Password FROM Login WHERE Username = ?",myUsername)
        row = self.cursor.fetchone()
        print(row.Password) #Testing Only
        return row.Password

    def getUserInfo(self, myUsername):
        self.cursor.execute("select Address, Email, FullName, TimeOffSet FROM UserInfo WHERE Username = ?",myUsername)
        row = self.cursor.fetchone()
        return row

    #Adds user, password is hashed and salted as input
    def addUser(self, myUsername, myPassword, myAddress, myEmail, myFullName, myTimeOffSet):
        addCheck = True

        if(len(myUsername) > 20):
            addCheck = False
        if(len(myPassword) != 64):
            addCheck = False
        if(len(myAddress) > 100):
            addCheck = False
        if(len(str(myEmail)) > 50):
            addCheck = False
        if(len(str(myFullName)) > 50):
            addCheck = False

        if(addCheck == True):
            self.cursor.execute("INSERT INTO Login(Username, Password) values (?,?) ",myUsername,myPassword)
            self.cursor.execute("INSERT INTO UserInfo(Username, Address, Email, Fullname, TimeOffSet) values (?,?,?,?,?) ",myUsername,myAddress,myEmail,myFullName,myTimeOffSet)
            self.cnxn.commit()

#Example Usage
myEvent = event("Dinner at Chipotle", datetime.datetime(2018, 7, 16, 17), datetime.datetime(2018, 7, 16, 18), "258 Stetson St, Cincinnati, OH 45219")
myOtherEvent = event("Dinner at Chipotle 2", datetime.datetime(2018, 7, 21, 17), datetime.datetime(2018, 7, 21, 18), "258 Stetson St, Cincinnati, OH 45219")
myEventList = [myEvent]
myCalendar = calendar(myEventList)
myCalendar.addEvent(myOtherEvent)
myUser = user("Mathew", "237 Calhoun St, Cincinnati, OH 45219", myCalendar, datetime.timedelta(minutes=15))
print("You should leave at")
print(myUser.getTTL(0))

#Database User Example (Password is not here)
myDatabase = database('travelschedulerserver.database.windows.net','TravelScheduler','TravelSchedulerServer',INSERTPASSWORDHERE)
myDatabase.getEventList('FakeUser')
myDatabase.getPassword('FakeUser')
#myDatabase.addEvent("Dinner at Chipotle", "FakeUser", "123 Fake Street", "456 Fake Road", datetime.datetime(2018, 7, 16, 17), datetime.datetime(2018, 7, 16, 18))
#myDatabase.addUser('FakeUser','e7cf3ef4f17c3999a94f2c6f612e8a888e5b1026878e4e19398b23bd38ec221a','123 Fake Street','fake@fakemail.com','Fake Name', 15)


#To do list/in other code (I will handle these):
# - Try Catch Error Handling
# - Pulling from and pushing to database
# - Better Event Handling
