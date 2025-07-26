# Version Date 27.07.25
Finished Aim Trainer (unless we want other variables) + added comments for everything.
Can't seem to find the issue with the wrong distractor in multiple target MT task.
Found the issue that Si mentioned. Looking for a fix...
The issue: When we have an MT Task, the participant can technically hold the circle button and then leave while holding it. What happens first of all is that we can cheat the movement time. The other more major issue is that we "highlight" the circle divs blue, since we are dragging with the mouse. This has somehow the effect that when we release our mouse, it doesn't register our "mouseup" which results in reaction time not being measured.
