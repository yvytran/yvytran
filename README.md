# About this repository

Topic: Multi-period price optimization problem for omnichannel retailers
accounting for customer heterogeneity.  
Group 10 - Course: E-Logistics in Supply Chain Management.  
The algorithm was an implementation of [this publication](https://www.sciencedirect.com/science/article/abs/pii/S0925527319300799).

## Requirement & Installation
This program was tested in Python 3.11  
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install numpy.
```bash
pip install numpy
```
or alternatively, install in accordance to the requirements.txt file included to ensure the program's reproducibility
```bash
cd [repository directory]
pip install -r requirements.txt
```  
## Usage
To run the program, simply open the terminal of your choice and run
```bash
python Elogfinal2512.py
```
The program will print out it's sample input data and output.

## Define notation 
Use 'discrete_neighborhood' notation to define the term to store the set of neighborhood of sorted x_values after conducting six following lines
```python
discrete_neighborhood(yk, delta)
```

Use 'zag' notation to define the algorithm 2 to return a set of solutions that dominate sorted x_values
```python
zag(xi, calculate_f1, calculate_f2, sorted_x_list, delta)
```

Use 'process_sorted_x_list' notation to define the algorithm 1 to append yList to xList as the final solutions
```python
process_sorted_x_list(sorted_x_list, calculate_f1, calculate_f2, delta)
```

## Functions Usage
Use sum to do sum all the term in the objective function 2 in this type sum() and will return a total value of objective function 2 
```python
# return sum(terms)
sum(terms)
```

Use this function sorted in this type sorted() and will return the list of x based on the value of the function f1 in ascending
```python
# returns value of x
sorted_x_list = sorted(x_values, key=lambda x: calculate_f1(*x)))
```

Use this function len in this type len () and will return the length of set yk 
```python
# finding the length of yk 
len(yk)
```

Use this function tuple in this type tuple () and will return the set neighborhood of yk
```python
# returns the set of neighborhood corresponding to the order of x 
tuple(y_neighbor)
```

Use this function tuple in this type min () and will find the value in y list that minimize the function f1
```python
# finding the minimum value in yList of the function f1 
 min(y_values_tuples, key=lambda ykj: calculate_f1(*ykj))
```

## Contributing

## License

[MIT](https://choosealicense.com/licenses/mit/)
