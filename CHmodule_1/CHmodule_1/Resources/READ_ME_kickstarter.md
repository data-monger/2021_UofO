# Kickstarting with Excel

## Overview of Project

### Purpose
To assist Louise in planning her kickstarter campaign to raise money for a thearter production she's attempting to get off the ground

## Analysis and Challenges
- What are some limitations of this dataset?
    More granular regions would be helpful, demographics of contributors, geo-coding of proposed locations as it relates to theartre performances (for example) , whether or not the were privately funded or funded by larger organizations. Also, we don't really know when and from where those contributions were made.

### Analysis of Outcomes Based on Launch Date
- What are two conclusions you can draw about the Outcomes based on Launch Date?
    May is the best time of year to launch theatre campaign with december being the worst.

### Analysis of Outcomes Based on Goals
- What can you conclude about the Outcomes based on Goals?
    It would seem, campaigns attempting to raise below 10k and above 35k tend to fair better- specifically for the the theartre category. I haven't evaluated other categories.

### Challenges and Difficulties Encountered
The instructions aren't leveraging the true capabilities of excel. I'm actually quite dissapointed to see a distinct lacking in tables, named ranges, and general "best practice" when managing and dealing with data. I've found what appears to be errors in the instruction set provided- which frankly could have been avoided if the material covered basic data hygiene.

2nd- i found it quite challenging so calculate upper and lower quartile, median and IQR dynamically. I resolved this eventually- as there is no way to use these functions within a pivot or a table- and power pivot creates a new-data subset which can't be linked to existing pivot's for dynamic filtering- 

In todays analytics world, there is little to no value in creating an analytical solution utilizing a static data set. when pulling data from repositories, data-warehouses, SQL, the cloud, or csv/txt files- the process proposed here would require a new set of analytics to be created for each variation of each ask. 

The instructions here, simply would not hold up in any real world exercise, where and when a live presentation is concerned and where managers, directors, or c-level executives are asking questions. A dynamically created report means data can be updated with new analytics produced at the drop of a hat. Questions can be answered.

Futhermore- a static resource looses its value long before the analysis is complete. Static values loose the transparency required for validating KPI's, and as a result the management team has significantly fewer resources with which to test assertions, or make sense of proposed initiatives as it relates to resource management.

Consider upgrading the excel portion of this exercise.
also- vlookups are garbage- they are brittle things that lure individuals in a false sense of security- and if not handled with the utmost of care- will cause false positives.
This takes us back to data hygiene. It's neither mentioned, nor mitigated by any of the procedures outlined in the lesson.

## Results
- What are some other possible tables and/or graphs that we could create?
    none really.
    i created everything to be dynamic- so zooming in, out, per country(s), by category(ies), sub-category(ies), outcome(s), year(s) - absolutely any combination of any potential possibility is available. clear filters and start again.

    The 2ndary date range (for deadline) wasn't included - and might not actually be relevant. Campaign length (start to finish) with dollars raised and an average daily contribution could be interesting- especially if pivoted against actual contribution amounts and the dates those contributions were made... 