# CPSC 60500 Software Engineering - Assignment 1

**Title: Fermat's Near Misses**  
**Authors: Mohammed Abdulaziz & Joshua Brown**  
**Language: Python**

### Instructions
> To use this program, simply download and run the executable file *Fermat's_Near_Misses.exe*. Alternatively, you may clone the github repository to your machine and run *Fermat's_Near_Misses.py*. The libraries and external resources listed in the *requirements.txt* file should be installed prior to running the program when running the *.py* file. A virtual environment (.venv) is recommended.

> Upon starting the program, you will be prompted to enter a value for *n*, the exponent in Fermat's formula ```x^n + y^n = z^n```. The value of *n* is bounded as such: ``` 2 < n < 12```. Next, you will be prompted to enter a value for *k*, the upper bound applied to *x* and *y* in the above formula. The value of *k* is bounded as such: ```k > 10```.

> After inputting values for *n* and *k*, the program will use the values *n* and *k* to search for combinations of *x*, *y*, and *z* that nearly solve Fermat's equation ```x^n + y^n = z^n```. Each near miss is printed to the terminal, displaying the values of *x*, *y*, *z*, the *absolute miss*, and the *relative miss*. 