# Decision Tree
The group project of CMSC5724 2020fall

## Table of Contents

- [Usage](#usage)
- [Dataset](#dataset)
- [Data Preprocessing](#data-preprocessing)
- [Structure](#structure)
- [Requirement](#requirement)
- [Contributors](#contributors)

## Usage
### How to run the code:

```sh
python3 decision_tree.py
```
  
### Result: 
The program will return the following in the console:
```sh
Loaded training set successfully.
Now building the decision tree.
Decision tree built with training set.
Loaded test set successfully.
Doing classification on the test set.
```

The decision tree will be printed and saved in this folder with the file `tree.txt`
The classification result on the test set will be saved in the file `classification_result.txt`
  
Note: 

  
## Dataset

### [Adult Dataset](http://archive.ics.uci.edu/ml/datasets/Adult)
  
adult.data: Trainning Set.
  
adult.test: Evaluation Set.

## Data Preprocessing

According the requirements of the project, we have preprocessed the dataset in the following steps:
- remove all the records containing '?'
- remove the attribute "native-country"
- for the labels, we convert '>50K' to 1, while '<=50K' to -1
- rounding-off column `fnlwgt` and column `capital gain` to simplify these contiunous data

### What's More:

等待被补充，写不写都行，可以删掉

## Structure 
  
```
Main.java (The entry of the program)等待被补充

FileReader.java (Read the file)

Point.java (Define the Point object)

W.java (Define the w object)

Perceptron.java (Margin perceptron algorithm)
```

  
## Requirement
```
jdk > 1.6
Operation System: Window,Linux
等待被补充
```
  
## Contributors

> ​	[@Sun Pengliang](https://github.com/sunpengliang)  1155148009
> 
> ​	[@Yang Zekun](https://github.com/Dopeeee)          1155145496
> 
> ​	[@Liu Jiarong](https://github.com/laukawing)      1155148282
>

