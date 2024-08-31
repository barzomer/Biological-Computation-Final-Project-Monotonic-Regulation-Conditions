# Monotonic Regulation Conditions Functions Count
By Bar Zomer and Ziv Chaba
## Assignment
In this Project, we wrote a python code that finds all the monotonic regulation conditions of the reasoning engine that satisfy monotonic requirement and consider whether none, some or all of the activators / inhibitors are present, as we studied in class.

We found 18 monotonic regulation conditions, as expected in the assignment file, transported them to a csv file, transported to Excel for visualization, and compared it with Table D of the assignment.

Our results were a perfect (reordered) equivilant of the 18 conditions of table 2.

## Files
### BasicSystem.py
A file for class BasicSystem(n,m,target). represents an instance in the basic system, contains activators count (int), inhibitors count (int), and the system target (boolean for result - active or inactive).

IN, AC are static variables that represent the maximum count of activators/inhibitors in the system (as per assignment requirements it was set to 2).

The function generateAllNecessaryBasicMonotonicRegulationConditions() is used to generate the basic regulation conditions which correspond to the necessary conditions of monotonic regulation conditions for each of the basic systems.
### main.py
A main file for the project.

The function generateAllBasicSystems(IN,AC) generates every BasicSystem object within the range of activators and inhibitors in this assignment (0-2).

The code runs each BasicSystem object 

The code outputs a list of all monotonic functions it has calculated for the system.
### results.xlsx
A Table with the main.py output organized, visualized and compared to Table D of the Assignment, ordered by the numbering in Table D.

Each active cell is called TRUE and is labeled in red.

Since our code is deterministic, we can expect the outputted conditions to be of same order and numbering in each run. We have matched their numbering with the numbering Table D to show equivilance.

## Our results



## How to Run
* Download BasicSystem.py , main.py to your local computer.
* Open command line at their location
* run the command   *python main.py*

Alternatively, you can run this python project on every python IDE.
