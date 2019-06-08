import sys
sys.path.append("..")
import argparse

import numpy as np
import robopy
# from packages.rotations import *
# from packages.transformations import *

L1, L2, L3 = 4, 3, 2

def main():
    parser = argparse.ArgumentParser(description='Exercise 3 algorithms')

    parser.add_argument('-n', dest='exercise_num', default='b',
                        type=str, nargs='?',
                        help='Exercise Number')
                    
    parser.add_argument('-q', dest='matrix_num', default='a',
                        type=str, nargs='?',
                        help='T^0_H matrix selector for section b')

    args = parser.parse_args()

    # inverse kinematics of the 3R planar manipulator
    dic = {
      'a': np.array([[1, 0, 0, 9], [0, 1, 0, 0],
                    [0, 0, 1, 0], [0, 0, 0, 1]]),
      'b': np.array([[0.5, -0.866, 0, 7.5373],
                    [0.866, 0.6, 0, 3.9266],
                    [0, 0, 1, 0], [0, 0, 0, 1]]),
      'c': np.array([[0, 1, 0, -3], [-1, 0, 0, 2],
                    [0, 0, 1, 0], [0, 0, 0, 1]]),
      'd': np.array([[0.866, 0.5, 0, -3.1245], 
                    [-0.5, 0.866, 0, 9.1674],
                    [0 ,0 ,1 ,0], [0 ,0 ,0 ,1]])
    }
    tool_frame = dic[args.matrix_num]

    l1=4; l2=3; l3=2;
    wrist_frame_transform = np.array([[1, 0, 0, l3], [0, 1, 0, 0],
                                      [0, 0, 1, 0], [0, 0, 0, 1]])
    wrist_frame = np.linalg.lstsq(tool_frame.T, wrist_frame_transform.T)[0].T
    c_phi = wrist_frame[0][0]
    s_phi = wrist_frame[1][0]
    x = wrist_frame[0][3]
    y = wrist_frame[1][3]
    c2 = (x**2 + y**2 - l1**2 - l2**2)/(2*l1*l2)
    print('c2 ', c2)
    # Checking if solution exist or not
    
    if args.exercise_num == 'b':
      tol = 4*np.spacing(1)
      if (abs(c2)-1) < tol:
          s2 = np.sqrt(1-c2**2);
          theta2 = [np.arctan2(s2, c2), np.arctan2(-s2, c2)]; # "elbow-up" or the "elbow-down" solution.
          
          k1 = l1 + l2*c2;
          k2 = l2*s2;
          theta1 = [(np.arctan2(y,x) - np.arctan2(k2,k1)), (np.arctan2(y,x) - np.arctan2(-k2,k1))];
          
          phi = np.arctan2(s_phi, c_phi);
          theta3 = phi - theta1 - theta2;
          
          print('Theta1 = {}\n'.format(np.rad2deg(theta1)));
          print('Theta2 = {}\n'.format(np.rad2deg(theta2)));
          print('Theta3 = {}\n'.format(np.rad2deg(theta3)));
      else:
          print('The goal is out of reach (outside the reachable workspace) - no solution exists\n');
    elif args.exercise_num == 'c':
        pass

if __name__ == '__main__':
    main()
