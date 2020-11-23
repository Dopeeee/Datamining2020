import math
import argparse

# intput data
parser = argparse.ArgumentParser()
parser.add_argument('--dataset', type=str)
args = parser.parse_args()

dataset = args.dataset
num_point = 0
num_dim = 0


def read_data(dataset):
    f_tmp = open(dataset, "r")
    data_format = f_tmp.readline()
    # Read Data Format
    data_format = data_format.split(' ')
    global num_point
    global num_dim
    num_point = int(data_format[0])
    num_dim = int(data_format[1])
    # Build Empty Dataset
    points_list = []
    # Build Dataset
    points = f_tmp.readlines()
    for i in points:
        points_list.append(i.split())
    return points_list

# String to int function
def list_str_to_int(points_list):
    for i in range(len(points_list)):
        for j in range(len(points_list[0])):
            points_list[i][j] = int(points_list[i][j])

# Dot multiply
def point_multiply(point1,w):
    counts = 0
    for index in range(num_dim):
        counts = counts + point1[index]* w[index]
    return counts

# Violationg return true,else return false
def check_violation(point1,w):
    sum_result = point_multiply(point1,w)
    # label == 1
    if point1[num_dim] == 1:
        if sum_result <= 0:
            return True
        else:
            return False
    # label == 0
    else:
        if sum_result >= 0:
            return True
        else:
            return False

# Normal perceptron
def perceptron(point_list,w):
    global violation_times
    is_violation = False
    for point_index in range(len(point_list)):
        is_violation = check_violation(point_list[point_index],w)
        if (is_violation == True ):
            if (point_list[point_index][num_dim] == 1):
                for update_index in range(len(w)):
                    w[update_index] = w[update_index] + point_list[point_index][update_index]
            else:
                for update_index in range(len(w)):
                    w[update_index] = w[update_index] - point_list[point_index][update_index]
            print("Violation time # {},The violation happens at # {} point".format(violation_times+1,point_index+1))
            print("The w is adjusted to {}".format(w))
            violation_times = violation_times + 1
            return False
    print("No violation happens ".format(w))
    return True

# point^2
def point_square(point):
    R = 0
    for i in range(num_dim):
        R = R + point[i] * point[i]
    return R

# Find Radius
def find_R(points_list):
    tmp_R = 0
    for i in range(num_point):
        this_R = point_square(points_list[i])
        if(this_R > tmp_R):
            tmp_R = this_R
    return tmp_R

# Calculate distance from a point to a plane
def dis_pt_to_plane(points,w):
    distance = 0
    w_denominator = point_square(w)
    w_denominator = w_denominator ** 0.5
    for i in range(num_dim):
        distance = distance + points[i]*w[i]
    #absolute
    result = abs(distance / w_denominator)
    # round set to 3
    result = round(result,3)
    return result

# Check whether the distance < r_guess/2
def check_violation_distance(point,w,r_guess):
    r_guess_half = r_guess / 2
    dist_to_plane = dis_pt_to_plane(point,w)
    if dist_to_plane < r_guess_half :
        return True
    else:
        return False

# Check all the points that whether they have distance violation
def perceptron_distance(points_list,w,r_guess):
    global violation_times
    for i in range(num_point):
        # define a flag
        is_distance_violation = check_violation_distance(points_list[i],w,r_guess)
        # if violation happens
        if(is_distance_violation):
            if (points_list[i][num_dim] == 1):
                for update_index in range(len(w)):
                    w[update_index] = w[update_index] + points_list[i][update_index]
            else:
                for update_index in range(len(w)):
                    w[update_index] = w[update_index] - points_list[i][update_index]
            print("Violation time # {},The distance violation happens at # {} point".format(violation_times+1,i+1))
            print("The w is adjusted to {}".format(w))
            print("Redoing the normal perceptron")
            violation_times = violation_times + 1
            global is_finish_stage1
            is_finish_stage1 = False
            return False
    if(is_finish_stage1 == True):
        print("No distance violation happens".format(w))
        return True
    else:
        return False

# Initiate w
def Initiate_w():
    global w
    w = [0]
    for i in range(num_dim-1):
        w.append(0)
# Calculate 12R^2 / r^2
def cal_terminate_time(points_list,r_guess):
    R = find_R(points_list)
    r_guess_tmp = r_guess * r_guess
    return (12*R/r_guess_tmp)

# Check wheter violation times > 12R^2 / r^2
def Break_perceptron(points_list):
    global is_finish_stage1
    global is_finish_stage2
    global violation_times
    global r_guess
    termi_time = cal_terminate_time(points_list,r_guess)
    print('Now we have {} times violation'.format(violation_times) )
    # violation times > 12R^2 / r^2
    if(termi_time < violation_times):
        # Initiate，Next round
        is_finish_stage1 = False
        is_finish_stage2 = False
        r_guess = r_guess / 2
        violation_times = 0
        Initiate_w()
        print('Violation times exceed limits，r_guess = r_guess/2')
    else:
        pass
    # Threshold
    if(r_guess < 0.0000001):
        print('r_guess is too small, this dataset might be linearly non-separable')
        is_finish_stage1 = True
        is_finish_stage2 = True

if __name__ == '__main__':
    points_list = read_data(dataset)
    list_str_to_int(points_list)
    w = [0]
    for i in range(num_dim - 1):
        w.append(0)
    is_finish_stage1 = False
    is_finish_stage2 = False
    r_guess = find_R(points_list)
    r_guess = round(r_guess ** 0.5)
    violation_times = 0
    while (is_finish_stage1 == False or is_finish_stage2 == False):
        if (is_finish_stage1 == False and is_finish_stage2 == False):
            is_finish_stage1 = perceptron(points_list, w)
        elif (is_finish_stage1 == True and is_finish_stage2 == False):
            is_finish_stage2 = perceptron_distance(points_list, w, r_guess)
        elif (is_finish_stage1 == False and is_finish_stage2 == True):
            is_finish_stage1 = perceptron(points_list, w)
        # check whether it needs terminate
        Break_perceptron(points_list)
        print(r_guess)
    print("The final w is {}".format(w))
    print("We guarantee the margin to be at least {}".format(r_guess / 2))
    print("Total violation time is {}".format(violation_times))
