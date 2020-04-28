# Author: Martin Green, Date: 04/28/2020
# Based off of u/DinoPunch's reddit post: https://www.reddit.com/r/todoist/comments/fdlb6l/i_use_labels_to_set_deadlines_so_i_can_move_the/
from todoist.api import TodoistAPI

#Set api token below.
api = TodoistAPI('')

"""
To changes colors of labels, add ", color = XX" after x and str(y). Refer to Todoist RestAPI for color codes.
https://developer.todoist.com/rest/v1/#colors
"""
#add label for 'Due'
label = api.label.add('Due')

#add labels for months
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
for x in months:
    label = api.labels.add(x)

#add labels for dates
for y in range(1,32):
    label = api.labels.add(str(y))

#commit changes
api.commit()
