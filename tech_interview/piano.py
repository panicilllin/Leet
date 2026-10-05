from typing import *

"""
You are given a list of data entries that represent entries and exits
of groups of people into a building. An entry looks like this:
 
{"timestamp": 1526579928, count: 3, "type": "enter"}
 
This means 3 people entered the building. An exit looks like this:
 
{"timestamp": 1526580382, count: 2, "type": "exit"}
 
This means that 2 people exited the building. timestamp is in Unix time.
 
Find the busiest period in the building, that is, the time with the
most people in the building. Return it as a pair of (start, end)
timestamps. You can assume the building always starts off and ends up
empty, i.e. with 0 people inside.
"""

class Demo:
    def __init__(self):
        pass

    def demo(self,records:list=[]):
        if not records:
            return None
        records.sort(key=lambda x: x['timestamp'])
        max_people = 0
        current_people = 0
        time_begin = None
        time_end = None
        
        for record in records:
            time = record.get('timestamp',None)
            in_out = record.get('type',None)
            people = record.get('count',None)
            if time is None:
                raise
            if in_out not in ['enter', 'exit']:
                raise
            if people is None:
                raise
                
            if in_out == 'enter':
                current_people += people
                if max_people < max(max_people, current_people):
                    time_begin = time
                    time_end = time
                    max_people = current_people
                elif max_people == current_people:
                    time_end = time
            else:
                if current_people == max_people:
                    time_end = time
                current_people -= people
                
        return time_begin, time_end

if __name__ == "__main__":
    d = Demo()
    res = d.demo([
	{"timestamp": 1526579928, "count": 3, "type": "enter"},
	{"timestamp": 1526579912, "count": 3, "type": "enter"},
  	{"timestamp": 1526579909, "count": 3, "type": "enter"},
  	{"timestamp": 1526579930, "count": 2, "type": "exit"},
  	{"timestamp": 1526579932, "count": 4, "type": "enter"},
  	{"timestamp": 1526579950, "count": 1, "type": "enter"},
  	{"timestamp": 1526579940, "count": 1, "type": "enter"},
  	{"timestamp": 1526579938, "count": 1, "type": "enter"},
  	{"timestamp": 1526579931, "count": 4, "type": "exit"},
  	{"timestamp": 1526579951, "count": 0, "type": "exit"},
])
    print(res)
    
