import sys
sys.path.append("..")
import argparse

import numpy as np
import robopy
from packages.rotations import *
from packages.transformations import *

L1, L2, L3 = 4, 3, 2

def three_dof_r(theta1, theta2, theta3):
    t1 = transformation_calc(theta1, 0, 0, 0)
    t2 = transformation_calc(theta2,0, 0, L1)
    t3 = transformation_calc(theta3, 0, 0, L2)
    return np.dot(np.dot(t1, t2), t3)

def three_dof_r_gripper(theta1, theta2, theta3):
    return np.dot(three_dof_r(theta1, theta2, theta3),
                  transformation_calc(0, 0, 0, L3))

def main():
    parser = argparse.ArgumentParser(description='Exercise 3 algorithms')

    parser.add_argument('-n', dest='exercise_num', default='c',
                        type=str, nargs='?',
                        help='Exercise Number')

    args = parser.parse_args()
    if args.exercise_num == 'c':
        print('a) T^0_3: ', three_dof_r(0, 0, 0))
        print('a) T^0_H: ', three_dof_r_gripper(0, 0, 0))
        print('b) T^0_3: ', three_dof_r(10, 20, 30))
        print('b) T^0_H: ', three_dof_r_gripper(10, 20, 30))
        print('c) T^0_3: ', three_dof_r(90, 90, 90))
        print('c) T^0_H: ', three_dof_r_gripper(90, 90, 90))
    elif args.exercise_num == 'd':
       # robopy.
        pass

if __name__ == '__main__':
    main()
