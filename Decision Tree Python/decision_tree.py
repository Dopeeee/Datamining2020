from math import log
import operator
import pickle
import re

pred_list = []
column_names = ['age','workclass','fnlwgt','education','education-num','marital-status','occupation','relationship','race','sex','capital-gain','capital-loss','hours-per-week','income']

def readData(filename):
    with open(filename, 'r') as f:
        data=[]
        # f.readline() # Uncomment here when reading adult.test
        for line in f.readlines():
            data += [line.strip().split(', ')]
        data = [[int(i) if i.isdigit() else i for i in row] for row in data] # String to int with numeric data
        if (filename == 'adult.csv'):
            data = [[1 if i=='>50K' else i for i in row] for row in data]
            data = [[-1 if i=='<=50K' else i for i in row] for row in data] #deal with label
        else:
            data = [[1 if i=='>50K.' else i for i in row] for row in data]
            data = [[-1 if i=='<=50K.' else i for i in row] for row in data] #deal with label
        for row in data[:]:
            for column in row:
                if column == '?':
                    data.remove(row)
                    break
        data[:] = [i[:13]+i[14:] for i in data]
        for i in range(0,len(data)-1):
            data[i][2] = round(data[i][2]/10000) * 10000
            data[i][10] = round(data[i][10]/1000) * 1000
        del (data[-1]) #delete last row with no data
        return data

def unique(rows, col):
    return set([row[col] for row in rows])

def label_classes(data):
    counts = {1:0,-1:0}
    for row in data:
        label = row[-1]
        counts[label] += 1
    return counts

class check:   
    def __init__(self, col, val):
        self.col = col
        self.val = val
    
    def check(self, pending):
        pending_val = pending[self.col]
        if isinstance(pending_val, int):
            if pending_val > self.val:
                return True
            else:
                return False
        else:
            if pending_val == self.val:
                return True
            else:
                return False
        
    def __repr__(self):
        if isinstance(self.val, int):
            condition = ">"
        else:
            condition = '=='
        return "Is %s %s %s?" % (
            column_names[self.col], condition, str(self.val))

class leaf_node:
    def __init__(self, data):
        self.attribute = label_classes(data)

class internal_node:
    def __init__(self, check, left_branch, right_branch):
        self.check = check
        self.left_branch = left_branch
        self.right_branch = right_branch

def partition(check, data):
    true_set = []
    false_set = []
    for row in data:
        if check.check(row):
            true_set.append(row)
        else:
            false_set.append(row)
    return true_set, false_set

def gini(data):
    cnt = label_classes(data)
    gini = 1
    prob_of_1 = cnt[1] / float(len(data))
    prob_of_0 = cnt[-1] / float(len(data))
    # print(cnt[1], cnt[-1], prob_of_1, prob_of_0)
    gini = 1 - prob_of_1**2 - prob_of_0**2
#     for keys in cnt:
#         prob_of_keys = cnt[keys] / float(len(data))
#         gini -= prob_of_keys**2
    return gini

def gini_split(left, right):
    p = float(len(left)) / (len(left) + len(right))
    # print(p, len(left), len(right))
    #print(left)
    #print(gini(left))
    return p * gini(left) + (1 - p) * gini(right)

def find_best_gini(data):

    best_split = 1
    best_check = None

    for col in range(13):
        unique_values = unique(data, col)
        for values in unique_values:
            c = check(col, values)
            t, f = partition(c, data)
            if len(t) == 0 or len(f) == 0:
                continue

            gs = gini_split(t, f)
            #print(gs)

            if gs <= best_split:
                best_split = gs
                best_check = c

    return best_split, best_check

def build_tree(data):
    gini_split, c = find_best_gini(data)

    if gini_split == 1:
        return leaf_node(data)

    t_set, f_set = partition(c, data)

    left_branch = build_tree(t_set)
    right_branch = build_tree(f_set)
    
    return internal_node(c, left_branch, right_branch)

def classifier(data, node):

    if isinstance(node, leaf_node):
        return node.attribute

    if node.check.check(data):
        return classifier(data, node.left_branch)
    else:
        return classifier(data, node.right_branch)


def print_tree(f, node, sept=""):
        if isinstance(node, leaf_node):
            print (sept + "Leaf node, # of classes:", node.attribute, file=f)
            return

        print (sept + str(node.check), file=f)

        print (sept + 'True:', file=f)
        print_tree(f, node.left_branch, sept + "  ")

        print (sept + 'False:', file=f)
        print_tree(f, node.right_branch, sept + "  ")



def print_result(test, tree):
    with open('classification_result', 'w') as f:
        correct = 0
        for row in test:
            probs = {}
            pred = 0
            attr = classifier(row, tree)
            if(len(attr.keys())==2):
                num_1 = attr[1]
                num_0 = attr[-1]
                if(num_1 >= num_0):
                    pred = 1
                else:
                    pred = -1
            else:
                pred = list(attr.keys())[0]
            pred_list.append(pred)
            total = (attr[1]+attr[-1]) * 1.0
            for key in attr.keys():
                probs[key] = str(int(attr[key] / total * 100)) + "%"
            if row[-1] == pred:
                correct += 1
            print ("Predicted: %d , Actual: %s , Probs of node: %s " %
                (pred, row[-1], probs), file=f)
        accuracy = correct / len(test)
        print("Correct: %d, Wrong: %d, Accuracy: %f" % (correct, len(test)-correct, accuracy), file=f)

X = readData('adult.csv')
print("Loaded training set successfully.")
print("Now building the decision tree.")
dtree = build_tree(X)
with open('tree.txt', 'a') as f:
    print_tree(f, dtree)
print("Decision tree built with training set.")
test = readData('adult_test.csv')
print("Loaded test set successfully.")
print("Doing classification on the test set.")
print_result(test, dtree)