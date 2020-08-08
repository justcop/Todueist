#imports
import datetime
import todoist

#Todoist API -> Find and place your API Below
api = todoist.TodoistAPI('')

#define today, tomorrow
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

#When the GenerateFilter script runs, you will need to identify the iD of the first filter created. This will be your x below. y will remain 0, it is just a counter.
x = 0
y = 0

for i in inputlist:
    filter = api.filters.get_by_id(x + y)
    #today's filter will be updated and have "(Today)" beside it.
    if i == today:
        filter.update(name= "(Today) " + i.strftime("%a, %B %d"))
        filter.update(color= 36)
    else:
        filter.update(name= i.strftime("%a, %B %d"))
        filter.update(color= 42)
        
    #Filter query is updated with new arguments
    filter.update(query= "@Due" + " & " + i.strftime("@%B") + " & " + i.strftime("@%d") + " & " + i.strftime("@%Y"))
    filter.update(item_order= 1)
    y = y+1
    
#commit filters
api.commit()
