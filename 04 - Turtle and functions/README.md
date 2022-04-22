# Turtle and functions
Start by:
- reading this short [turtle tutorial](https://docs.python.org/3/library/turtle.html).
- Then study [this code](http://interactivepython.org/runestone/static/pythonds/Recursion/pythondsSierpinskiTriangle.html).
- Watch [this youtube video](https://www.youtube.com/watch?v=qhbuKbxJsk8) and write code that generates the graphics (as shown in the video).

The result should be a circle and lines that connect points based on the multiplier.
Write the code using a function with return values.

As a second step, read about [generators](https://www.youtube.com/watch?v=bD05uGo_sVI) and the yield keyword and write a new function that uses generators:

## Results
I didn't quite know where to start with this problem, the hardest part was figuring out how to find the coordinates of each point along the circle.
After scrolling through the documentation i figured i could split the circle into the same amount of sections as the amount of points i want, then, while drawing the circle, store the turtle's position. Doing this and setting the circle radius and points to 200, with a multiplier of 2 gave this result:

<p align="center">
  <img src="./images/attempt1.gif" width="40%"/>
</p>

This drawing is rather slow and not very interesting so i decide to spice it up a little bit.  I realized i could turn off automatic refreshes and only refresh the model when i wanted,
this means the computer doesn't have to render as much which makes the animation snappier. With these adjustments and putting the drawing in a loop with different multipliers i ended up with this:

<p align="center">
  <img src="./images/attempt2.gif" width="40%"/>
</p>

I wasn't feeling quite satisfied yet as wanted to achieve [this](https://youtu.be/qhbuKbxJsk8?t=737) animation. For this i changed
the multiplier to be floats, but since the points only are integers i am rounding the (pointnr * multiplier) value to the nearest point. Additionally I made it so the colors themselves are either rotating around after each drawing (notice how the rad part of the circle isn't always at the bottom anymore). I also made a version where it only changes color for each multiplier instead of each line, just like in the animation i wanted to achieve.


In the end i ended up with these fancy animations (I apologize for the compression):

<p align="center">
  <img src="./images/final_1.gif" width="40%"/>
  <img src="./images/final_2.gif" width="40%"/>
</p>
