README

Programming language:
Python 3

Required libraries:
math
numpy
matplotlib

Files submitted:
Files submitted:
question0_Euler_method.py        - Main Python program for the programming task before question 1 using the Euler method
question0_RK4_method.py          - Main Python program for the programming task before question 1 using the fourth-order Runge–Kutta method
question3_plot.py                - Main Python program for Question 3, used to generate the required plots
question4_plot.py                - Main Python program for Question 4, used to generate the required plots
question5_RK4_2nd_order.py       - Main Python program for programming task after question 5, before question 6, using the second-order Runge–Kutta method
question7_plot.py                - Main Python program for Question 7, used to generate the required plots
question8_plot.py                - Main Python program for Question 8, used to generate the required plots
question8_RK4.py                 - Main Python program for Question 8 using the fourth-order Runge–Kutta method


How to run:
Each Python file can be run independently.

For files with names ending in "_plot.py", running the file will generate and display
the corresponding plots.

For the other Python files, running the file will generate numerical solution data
(points) used for analysis or for producing the plots. One can change the parameters
to answer different parts of the question.

Description:
This submission contains Python programs for solving ordinary differential equations
and analyzing the results using numerical methods.

For question 0(the programming task before question 1), the Euler method and the fourth-order Runge–Kutta (RK4) method are
implemented to compute numerical solutions. These two files are used up to question 4, so they have been run in different 
ways, with only the last attempt kept. Essentially, the functions Euler_method and EK4_method are used to generate points 
required in question 1; the En_x04 function in both files are for question 4.

For Questions 3, 4, 7, and 8, the programs with names ending in "_plot.py" generate
figures based on the computed numerical solutions.

For Questions 5 and 8, additional programs implement Runge–Kutta methods to generate
numerical solution points, which are then used for plotting and comparison.

All parameters are specified directly within the source code, and no external input
files are required.
