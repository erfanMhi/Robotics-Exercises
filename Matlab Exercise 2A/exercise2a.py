import sys
sys.path.append("..")
import argparse

import numpy as np
from robopy import *
from numpy.linalg import inv
from packages.rotations import *

def rotation_calc(alpha, beta, gama):
  rot_alpha = rotationz(alpha)
  rot_beta = rotationy(beta)
  rot_gama = rotationx(gama)
  return np.dot(np.dot(rot_alpha, rot_beta), rot_gama)

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
    print('solution i: ', rotation_calc(10, 20, 30))
    print('solution ii: ', rotation_calc(30, 90, -55))
    st = np.allclose(inv(rotation_calc(10, 20, 30)),rotation_calc(10, 20, 30).T)
    print('Are Rba == Rab-1 == Rab.T : ', str(st))

  elif args.exercise_num == 'b':
    print('10_20_30(alpha,beta,gama) angle rotated then reversed: ', reverse_euler_calc(rotation_calc(10, 20, 30)))
    print('30_90_-55(alpha,beta,gama) angle rotated then reversed: ', reverse_euler_calc(rotation_calc(30, 90, -55)))
  elif args.exercise_num == 'c':
    p = [1, 0, 1]
    print('P_A', np.dot(rotationy(20), p))
  elif args.exercise_num == 'd':
    print('Is my implemented rotationx calculation correct: ',
          str(np.allclose(rotationx(10), rotx(10, "deg"))))
    print('Is my implemented rotationy calculation correct: ',
          str(np.allclose(rotationy(20), roty(20, "deg"))))
    print('Is my implemented rotationz calculation correct: ',
          str(np.allclose(rotationz(30), rotz(30, "deg"))))
    print('Is my implemented homogeneouse transformation matrix calculation correct: ',
          str(np.allclose(rotation_calc(10, 20, 30), rpy2tr([30, 20, 10], unit='deg')[:3,:3])))
    print('Is my implemented reverse euler matrix calculation correct: ',
          str(np.allclose(reverse_euler_calc(rotation_calc(10, 20, 30)), tr2rpy(rotation_calc(10, 20, 30), 'deg')[0, ::-1])))

if __name__ == '__main__':
  main()
  