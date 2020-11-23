# Margin Perceptron Python Version 
The group project of CMSC5724 2020fall

## Table of Contents

- [Usage](#usage)
- [Dataset](#dataset)
- [Contributors](#contributors)

## Usage
### How to run the code:

```sh
$ python margin_per.py --dataset d5.txt
```
Result: This program will return a number bigger than 1/4 margin*  
  
Note: We guarantee the dataset must be linearly separable by using the [data generator](https://github.com/Dopeeee/Datamining2020/tree/main/data) we develop.  
  
But when the dataset is linearly non-separable , we set the threshold to be 1*e-8 , when the w is smaller than the threshold, we terminate this whole program. 
  
This can not guarantee to prove the dataset is non-separable, but it do improve the robust.

## Dataset

### We prepare several dataset with 10000 points in different dimensions to test our program
  
d2.txt: 10000 linearly separable points in 2 dimensions.
  
d4.txt: 10000 linearly separable points in 4 dimensions.
  
d9.txt: 10000 linearly separable points in 9 dimensions.
  
## Contributors

> ​	[@Sun Pengliang](https://github.com/sunpengliang)  1155148009
> 
> ​	[@Yang Zekun](https://github.com/Dopeeee)          1155145496
> 
> ​	[@Liu Jiarong](https://github.com/laukawing)      1155148282
>


