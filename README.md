# Grad Rate Predictor

The Grad Rate Predictor is a systems dynamics model of higher education policy impacts on the graduation rates of first-generation college students in the United States. Its purpose is to explore the impacts that public policies interact with first-generation graduation rates in order to help guide policymakers in the creation of feasible, beneficial policies that increase access to a Bachelor's-level education amongst students whose parents did not attain a 4-year degree. 

## Installation

1. Commit [this](https://github.com/matthew-boisvert/Grad-Rate-Predictor) repository to a local repository using Git or download the files from GitHub
2. Install [Python 3.6 or above](https://www.python.org/downloads/) and add 
3. On Windows and MacOs/Linux, run the following command to change the current directory to the folder where the downloaded files were stored
```bash
cd "C:\[full path of file]"
```
4. On MacOS/Linux, you may need to change the permissions of the file to make it executable by running the command:
```bash
chmod +x DisplayRunner.py
```

## Usage
On Windows and MacOS/Linux, use the following command to run the simulation
```python
python DisplayRunner.py
```
Note that if you do not have Python.exe added to the PATH environmental variable on Windows, you will have to instead use the command:
```
C:\[path to folder where Python.exe is stored]\python.exe DisplayRunner.py
```

## How does it work?

The Grad Rate Predictor implements a systems dynamics model for simulating college degree outcomes based on potential policies that can be implemented. Because of the vast complexities associated with college persistence amongst different demographics, the model does not provide specific graduation rates that represent a definitive conclusion. Instead, the modeled graduation rate has a base value for a given demographic (which comes from [1]) that can be changed in three ways:

1. If a policy is known to be beneficial to a specific demographic, then the line shown will be raised up by a factor of 1% of the display height.
2. If a policy is known to be detrimental to a specific demographic, then the line shown will be lowered by a factor of 1% of the display height.
3. If a policy is not known to be beneficial or detrimental to a given demographic or is known to be neutral to that demographic, then the line shown will be raised by a factor of 0.5% of the display height.

With the buttons at the bottom of the GUI, you can choose to activate or deactivate combinations of policies. You can also cycle between demographics within the same category (e.g. financial status) using the buttons in the top right or use the menu to change to a new demographic. This allows you to see how policies interact with independent demographics in different ways and can be combined in ways that benefit as many first-generation students as possible.

Note that the demographics and policies themselves are not fixed. You can add or remove new demographics and categories using the "DemographicsData.csv" file as well as policies using the "PolicyData.csv" file. This makes the simulation dynamic for future researchers and policymakers to test new policies and see how they impact a greater variety of demographics. Additionally, the simulation can be easily adapted to display quantitative graduation rate predictions through a few changes to the GUI. This would allow researchers to have even more insight into potential policy impacts using the results provided by the simulation.

## How was the simulation made?
All of the simulation was coded in Python. The GUI specifically was made using the [Tkinter](https://docs.python.org/3/library/tkinter.html) Python library and it implements an Event-Listener model for handling user interactions with the simulation.

## Sources
[1] [Beginning Postsecondary Students: 2004/2009](https://nces.ed.gov/surveys/bps/)

## Contributors
Matt Boisvert, Deborah Gould, Nailea Castillo, and Jamie Veasley