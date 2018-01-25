### Euclidean algorithm
An algorithm which meant to calculate square's maximum size which will fit in a rectangle<br>
While trying to solve this algorithm I straight away thought about common dividers<br>
And I've said to my self that I must test it...<br>
I took a 48x20 rectangle and started thinking
<div align="center">
    <p><img src="https://image.prntscr.com/image/tH1KPqnxSs6OgP0c4-wn6g.png"></p>
</div>
The maximum divider for both numbers is 4, right? 20 / 4 = 5, 48 / 4 = 12<br>
I started filling up my rectangle with many 4x4 squares.
<div align="center">
    <p><img src="https://image.prntscr.com/image/uKcj95xzQGGsfqAk-QItRg.png"></p>
</div>
Woah! They're perfect!

### Reverse engineering the algorithm
So it's very simple:<br>
<div align="center">
    <ul>
        <li>Finding both, width and height dividers</li>
        <li>Picking the dividers and comparing them between the two</li>
        <li>Filtering the 2 lists into 1 list with common dividers</li>
        <li>Picking up the heighest divider</li>
        <li><b>PROFIT!</b></li>
    </ul>
</div>

### Flow graph

<div align="center">
    <p><img src="https://image.prntscr.com/image/CQ09x8PASz6hvN55tBtgGA.png"></p>
</div>
#### The End.
Code can be viewed in [here](https://github.com/TheOnlyArtz/Computer-Science-Alogrithms/blob/master/src/Euclidean/Euclidean.py)

### Examples for different rectangles
<div align="center">
    <p><img src="https://image.prntscr.com/image/LgeL1GN7SP_xVGFaHQVfHQ.png"></p>
</div>