import sys
sys.path.append("..")
import argparse

import numpy as np
from robopy import *
from numpy.linalg import inv
from packages.rotations import *

def homogen_calc(alpha, beta, gama, p):
  homogen = np.zeros((4, 4))
  rot_alpha = rotationz(alpha)
  rot_beta = rotationy(beta)
  rot_gama = rotationx(gama)
  homogen[:3,:3] = np.dot(np.dot(rot_alpha, rot_beta), rot_gama)
  homogen[:3,3] = p
  homogen[3,3] = 1
  return homogen

def reverse_euler_calc(r):
  beta = arcsin(-r[2, 0])
  alpha = arccos(r[0,0]/cos(beta))
  gama = arccos(r[2,2]/cos(beta))
  return alpha, beta, gama


def main():
  parser = argparse.ArgumentParser(description='Exercise 2A algorithms')

  parser.add_argument('-n', dest='exercise_num', default='a',
                      type=str, nargs='?',
                      help='Exercise Number')

  args = parser.parse_args()

  assert args.exercise_num in ['a', 'b', 'c', 'd'], 'exercise number is not valid'
  if args.exercise_num == 'a':
    print('solution i: ', homogen_calc(10, 20, 30, [1, 2, 3]))
    print('solution ii: ', homogen_calc(0, 20, 0, [3, 0, 1]))
  elif args.exercise_num == 'b':
    p = [1, 0, 1, 1]
    print('P_A', np.dot(homogen_calc(0, 20, 0, [3, 0, 1]), p)[:3])
  elif args.exercise_num == 'c':
    t_a_b = homogen_calc(10, 20, 30, [1, 2, 3])
    t_b_c = homogen_calc(0, 20, 0, [3, 0, 1])
    st = np.allclose(inv(t_a_b), inverse(t_a_b))
    print('Is implemented inverse calculation function correct for the a_i: ', st)
    print('Dot product of a_i with its inverse: ', np.dot(t_a_b, inverse(t_a_b)))
    st = np.allclose(inv(t_b_c), inverse(t_b_c))
    print('Is implemented inverse calculation function correct for the a_ii: ', st)
    print('Dot product of a_ii with its inverse: ', np.dot(t_b_c, inverse(t_b_c)))
    
  elif args.exercise_num == 'd':

    t_a_b = homogen_calc(10, 20, 30, [1, 2, 3])
    t_b_c = homogen_calc(0, 20, 0, [3, 0, 1])

    print('Solution i: ')
    t_a_c = np.dot(t_a_b, t_b_c)
    print('T_a_c : \n', t_a_c)
    t_c_a = inverse(t_a_c)
    print('T_c_a : \n', t_c_a)

    print('Solution ii: ')
    print ('Initial T_a_b: \n', t_a_b)

    t_a_b = np.dot(t_a_c, inverse(t_b_c))
    print ('Calculated T_a_b: \n', t_a_b)

    print('Solution iii: ')

    print ('Initial T_b_c: \n', t_b_c)
    t_b_c = np.dot(inverse(t_a_b), t_a_c)
    print ('Calculated T_b_c: \n', t_b_c)

  elif args.exercise_num == 'e':
    print('They are ok!!')


if __name__ == '__main__':
  main()
  