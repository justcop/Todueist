# Todoist-Date-Labels inspired by u/DinoPunch in r/Todoist

## Ver. 2.0
### 08/08/2020

### Updates
#### GenerateLabels.py
- Filename was updated to reflect new naming standard.
- NEW! A label for the current year is now created.
- Labels 1-9 will now be created with a leading 0. 

#### NEW! GenerateFilters.py
- This code snippet creates 8 new filters based off on the current day and 7 upcoming days.
- Filters are favorited by default.

#### NEW! UpdateFilters.py
- This code snippet updates the 8 filters from the GenerateFilters script to reflect the current day and 7 upcoming days. This script is designed to be run daily. If running Windows 10, it is recommended to use TaskScheduler to run this script each morning.
- Currently you will need to identify the iD of the first filter created from the GenerateFilters script and reuse this iD. This allows the filters to be updated. I have not yet found an easy way to delete filters by name which would make this step obselete.

### Roadmap
Currently, I am working to transition this project from 8 separate filters (1 for each of the next 7 upcoming days and today) to a single filter that identifies tasks with Due Dates from the current day out to the next 7 days.

___

## Ver. 1.0
### 04/28/2020

### General Usage Notes
- You will need to identify and substitute your own API Token into the program.
- This script simply adds Due, Month, and Day labels to your todoist.
- Please refer to u/DinoPunch on how to use the newly created labels.
  - https://www.reddit.com/r/todoist/comments/fdlb6l/i_use_labels_to_set_deadlines_so_i_can_move_the/
