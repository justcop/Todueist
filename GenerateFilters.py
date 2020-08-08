#imports
import datetime  
import todoist

#Todoist API
api = todoist.TodoistAPI('')

#define today and tomorrow
today = datetime.date.today()
tomorrow =  today + datetime.timedelta(days=1)

#define 6 more days
t1 = tomorrow + datetime.timedelta(days=1)
t2 = tomorrow + datetime.timedelta(days=2)
t3 = tomorrow + datetime.timedelta(days=3)
t4 = tomorrow + datetime.timedelta(days=4)
t5 = tomorrow + datetime.timedelta(days=5)
t6 = tomorrow + datetime.timedelta(days=6)

inputlist = [today, tomorrow, t1, t2, t3, t4, t5, t6]

#Create filters based off of today, tomorrow, 6 more days
for i in inputlist:
    month = i.strftime("@%B")
    date = i.strftime("@%d")
    year = i.strftime("@%Y")
    query = "@Due" + " & " + month + " & " + date + " & " + year
    print(query)
    if i == today:
        filter = api.filters.add(name = i.strftime("Today"), query = query, color = 39, is_favorite = 1)
    else:
        filter = api.filters.add(name = i.strftime("%A"), query = query, color = 39, is_favorite = 1)

#commit changes
api.commit()
