# Kickstarting with Excel

## Overview of Project

### Purpose
To assist in determining the best stock portfolio

## Analysis and Challenges
2017 stocks did much better than 2018. A larger dataset would have been more insightful as far as the stock trends go- in addition other contributing factors to stock performance need to be considered, as this is a wholly inadaquate process to determine stock performance.


### Challenges and Difficulties Encountered
Refactoring code is a waste of time. Best to do it right the first time; proper planning prevents piss poor perfance- no where else is that made more evident than poorly written code.

the increase in performance i'd say is somewhat minimal for a few hundred lines of code; the other disadvantage, or negative aspect of refactoring code is it doesn't allow for "outside the box thinking". it forces us down a solution path that won't differ greatly from the original in the end. i noticed this with my work; i tried to use the xlm architecture and access table objects, along with header row and column list objects- when refactoring the code i noticed some steps were included in other steps later, or sooner- particularly those that involved the table objects and counting the rows in a given table object.

because the table object expands and contracts based on user input (be in automation, or human) there is no real need to determine the end of the range- as the range is already a part of the table object. all we really need to do is cycle through the object for each i. or in my case, for each x1 and x2.

the beauty of working with an already defined object, is that you can call it again and again, despite the fact that the table may grow or shrink.

## Results
