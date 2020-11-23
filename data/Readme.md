# Dataset Generator
The dateset generator of margin perceptron in our course project of CMSC5724 2020fall

## Table of Contents

- [Usage](#usage)
- [Requirement](#requirement)
- [Contributors](#contributors)

## Usage
### How to run the code:

```sh
python data_produce.py --dimension 3
```

Result: This program will return a test.txt file with 10000 linearly separable points in n(default to 3) dimention 
  
- Note1:  --dimension could follow a number , the number is the dimension you want to generate.(do not count the label dimension, eg (1,1,0) is a point in 2 dimensions with label 0)

- Note2:  We generate the points and make sure they are far from origin , this can reduce the running time without loss of generality


## Requirement
```
python
Operation System: Window,Linux
```

## Contributors

> ​	[@Sun Pengliang](https://github.com/sunpengliang)  1155148009
> 
> ​	[@Yang Zekun](https://github.com/Dopeeee)          1155145496
> 
> ​	[@Liu Jiarong](https://github.com/laukawing)      1155148282
>

