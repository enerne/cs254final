# cs254final

This is the repository for the final project in CS 254 (Machine Learning) for Ethan Nerney and Garrett Landen.

It is a computer vision project that will be able to distinguish between 5 different animals:
- Elephant
- Squirrel
- Goat
- Cow
- Butterfly



##Files
At the moment, there are 5 .py files:   
- constants.py:
    - holds all the constants to be referred to (should probably be updated)
- compression.py:
    - when run, the output/data folder will populate with a duplicate of the data folder, but with every image being 64x64 pixels.
    
- analysis.py: 
    - intended to plot image data as well as model success data in the future
  
- get_data.py:
    - takes all the images from the output/data/train folder and turns each of them into 1 dimensional arrays to be 
    given to the algorithm
      
- rough_learning.py:
    - learns