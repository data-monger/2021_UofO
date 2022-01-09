# PyPoll

## Overview of Election Audit
3 counties with elections for 3 candidates require vote tabulation for the purpose of determining top county and winning candidate

## Results
The election results are as follows, taken directly from script output, with annotations:
### Date ran
Results Tabulated on: 2022-01-09


### Election Results
-------------------------
Total Votes: 369,711
-------------------------

### County Votes:
Jefferson: 10.5% (38,855)
Denver: 82.8% (306,055)
Arapahoe: 6.7% (24,801)
-------------------------
Winner: Denver
Winning Vote Count: 306,055
Winning Percentage: 82.8%
-------------------------

### Candidate Votes:
Charles Casper Stockham: 23.0% (85,213)
Diana DeGette: 73.8% (272,892)
Raymon Anthony Doane: 3.1% (11,606)
-------------------------
Winner: Diana DeGette
Winning Vote Count: 272,892
Winning Percentage: 73.8%
-------------------------


## Summary
The provided script can be used for other elections where required data-fields are present:
County
Candidate

We've already included a run date, where we can run the script daily to track election results real-time, or more frequently if we include a time stamp. The data output can also be formatted in a grid suitable for additional analysis and insertion into a structered data repository.

Should we choose to include additional layers of granularity, for instance city level mayoral race's we can modify the script to dynamicaly recognize regional district races to adjust our assertions and outputs accordingly. In addition, the script could also be modified for state level, or other regional level races. These would be functional additions inclusive to the modifications listed above.