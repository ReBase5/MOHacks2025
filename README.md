We used Gemini to come up with our program.
Patrick will learn how to create a GUI using Python
Alex will learn how to create a prediction model using python

Here's a link to the data set we used (11/15/2025):
https://data.gov.ie/dataset/-gauge-network-intgn-gloss-station-union-hall-harbour-gloss-tide-gauges-co-cork-ireland-2020-present

Here's what Gemini said:

🌊 Simple Tide Prediction in Python
The easiest way to calculate tide levels in Python is to think of it like playing a specific tune on a piano, where each key represents a different astronomical force.

1. The Core Idea: The "Tide Recipe"
Ocean tides are mainly caused by the gravity of the Moon and the Sun. Scientists have figured out that you can model the tide by adding up the effects of about 60 different, consistent forces. These forces are called harmonic constituents (don't worry about the big name).

Think of the tide level at any moment as the result of a recipe:

Tide Level = (Average Sea Height) + (Effect of the Moon's main pull) + (Effect of the Sun's main pull) + (Effect of Moon's position changes) + ...

2. How the Python Program Works (Simplified)
Instead of making you write the complex math from scratch, we use a specialized Python library (like pytides) that already knows the math.

Step A: Get the Constants (The Recipe Ingredients)

For any specific harbor (like Miami or Boston), scientists have already calculated the size (amplitude) and timing (phase) of the 60 or so main forces.

You need to get these Harmonic Constants for your chosen location. This is just a simple table of numbers you plug into your program.

Step B: Use the Library (The Magic Calculator)

You give the pytides library three things:

The Constants (your table of numbers from Step A).

A Time Range (e.g., "Predict the tide every hour for the next 7 days").

The Library then uses its built-in physics engine to calculate the resulting water level for every time you specified.

Step C: Plot the Results (Make a Graph)

You use another library called Matplotlib to draw a line graph showing the predicted water level (the height) over your chosen time range. This gives you a clear visual of when high tide and low tide will occur.
