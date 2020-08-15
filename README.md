# Todueist
## Todoist Date Labels and Upcoming Due Tasks Filters inspired by u/DinoPunch from r/Todoist

## Ver. 1.0
### 08/11/2020

This is a python script that creates due date labels and a filter for upcoming due tasks. This script is designed to be run frequently (ideally daily) as the filter will have to be updated for the new query each day.

#### Getting Started
- You will need the following to get started:
  - Python 3 installed
  - The following packages:
    - todoist-python
    - DateTime
    - python-dateutil
  - Your Todoist API Token
  
1. Open the python script using either a text editor or an IDE. 
2. Copy your API Token into line 11 between the quotations:
        
        api = todoist.TodoistAPI('')
        
3. Optional: If you want, you can change the following settings:
    - **Number of days to preview ahead.** The default is 5 days, but this number can be adjusted on line 140.
    - **Number of year labels created.** The default is 2 (current year and next year) and the minimum is 1 (current year). You can change this on line 79 with the years_ahead variable.
    - **Color of labels and filter.** The default color for all the labels is Sky Blue (39) and for the filter is Grape. Using the color codes from Todoist (https://developer.todoist.com/sync/v8/#colors) you can change the color of the labels and filter. The color of the month labels is on line 45, day of the month on line 75, year on line 108, and the filter on line 134.
4. Using the command line or terminal, navigate to the folder containing the script and run it using 

        python Todueist.py

5. **Recommended:** I recommend running this script daily using Task Scheduler if you are windows. This allows the filter to update on a daily basis and always show you the upcoming days. Otherwise, the filter will not be updated and the days previewed will remain stagnant. 

General Usage
- Adds Due, Month, Day, and Year labels to Todoist. 
- Adds 'Upcoming Due Tasks' Filter to Todoist with the query based on the identification of the aforementioned labels. (Note: This filter relies on the presence of one label from each category e.g. Due August 11 2020
- If on Windows 10, use Windows Task Scheduler to run this task daily.
  - Refer to this guide (https://towardsdatascience.com/automate-your-python-scripts-with-task-scheduler-661d0a40b279) for setting up the daily task. The heading that is most helpful is "Configure Task in Windows Task Scheduler."
- Please refer to u/DinoPunch on how to use the newly created labels.
  - https://www.reddit.com/r/todoist/comments/fdlb6l/i_use_labels_to_set_deadlines_so_i_can_move_the/
