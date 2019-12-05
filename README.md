# Grad-Rate-Predictor



Description: The Grad Rate Predictor is a systems dynamics model of higher education policy impacts on the graduation rates of first-generation college students in the United States. Its purpose is to explore the impacts that public policies interact with first-generation graduation rates in order to help guide policymakers in the creation of of feasible, beneficial policies that increase access to a Bachelor's-level education amongst students whose parents did not attain a 4-year degree. 

How does it work?
The Grad Rate Predictor implements a systems dynamics model for simulating college degree outcomes based on potential policies that can be implemented. Because of the vast complexities associated with college persistence amongst different demographics, the model does not provide specific graduation rates that represent a definitive conclusion. Instead, the modeled graduation rate has a base value for a given demographic (which comes from [1]) that can be changed in three ways:

1. If a policy is known to be beneficial to a specific demographic, then the line shown will be raised up by a factor of 1% of the display height.
2. If a policy is known to be detrimental to a specific demographic, then the line shown will be lowered by a factor of 1% of the display height.
3. If a policy is not known to be beneficial or detrimental to a given demographic or is known to be neutral to that demographic, then the line shown will be raised by a factor of 0.5% of the display height.

With the buttons at the bottom of the GUI, you can choose to activate or deactivate combinations of policies. You can also cycle between demographics within the same category (e.g. financial status) using the buttons in the top right or use the menu to change to a new demographic. This allows you to see how policies interact with independent demographics in different ways and can be combined in ways that benefit as many first-generation students as possible.

How was it made?
All of the simulation was coded in Python. The GUI specifically was made using the Tkinter Python library and it implements an Event-Listener model for handling user interactions with the simulation.

How to run the simulation?


Creators: Matt Boisvert, Deborah Gould, Nailea Castillo, and Jamie Veasley