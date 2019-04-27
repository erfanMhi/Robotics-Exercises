
import numpy as np


def sin(degree):
  return np.sin(np.deg2rad(degree))

def cos(degree):
  return np.cos(np.deg2rad(degree))

def arccos(degree):
  return np.rad2deg(np.arccos(degree))

def arcsin(degree):
  return np.rad2deg(np.arcsin(degree))
  
def rotationx(degree):
  s = sin(degree)
  c = cos(degree)
  r = [[1, 0, 0],
       [0, c, -s],
       [0, s, c]]
  return np.array(r)

def rotationz(degree):
  s = sin(degree)
  c = cos(degree)
  r = [[c, -s, 0],
       [s, c, 0],
       [0, 0, 1]]
  return np.array(r)


def rotationy(degree):
  s = sin(degree)
  c = cos(degree)
  r = [[c, 0, s],
       [0, 1, 0],
       [-s, 0, c]]
  return np.array(r)


def inverse(A):
    detA = np.linalg.det(A)

    b00 = A[1,1]*A[2,2]*A[3,3] + A[1,2]*A[2,3]*A[3,1] + A[1,3]*A[2,1]*A[3,2] - A[1,1]*A[2,3]*A[3,2] - A[1,2]*A[2,1]*A[3,3] - A[1,3]*A[2,2]*A[3,1]
    b01 = A[0,1]*A[2,3]*A[3,2] + A[0,2]*A[2,1]*A[3,3] + A[0,3]*A[2,2]*A[3,1] - A[0,1]*A[2,2]*A[3,3] - A[0,2]*A[2,3]*A[3,1] - A[0,3]*A[2,1]*A[3,2]
    b02 = A[0,1]*A[1,2]*A[3,3] + A[0,2]*A[1,3]*A[3,1] + A[0,3]*A[1,1]*A[3,2] - A[0,1]*A[1,3]*A[3,2] - A[0,2]*A[1,1]*A[3,3] - A[0,3]*A[1,2]*A[3,1]
    b03 = A[0,1]*A[1,3]*A[2,2] + A[0,2]*A[1,1]*A[2,3] + A[0,3]*A[1,2]*A[2,1] - A[0,1]*A[1,2]*A[2,3] - A[0,2]*A[1,3]*A[2,1] - A[0,3]*A[1,1]*A[2,2]

    b10 = A[1,0]*A[2,3]*A[3,2] + A[1,2]*A[2,0]*A[3,3] + A[1,3]*A[2,2]*A[3,0] - A[1,0]*A[2,2]*A[3,3] - A[1,2]*A[2,3]*A[3,0] - A[1,3]*A[2,0]*A[3,2]
    b11 = A[0,0]*A[2,2]*A[3,3] + A[0,2]*A[2,3]*A[3,0] + A[0,3]*A[2,0]*A[3,2] - A[0,0]*A[2,3]*A[3,2] - A[0,2]*A[2,0]*A[3,3] - A[0,3]*A[2,2]*A[3,0]
    b12 = A[0,0]*A[1,3]*A[3,2] + A[0,2]*A[1,0]*A[3,3] + A[0,3]*A[1,2]*A[3,0] - A[0,0]*A[1,2]*A[3,3] - A[0,2]*A[1,3]*A[3,0] - A[0,3]*A[1,0]*A[3,2]
    b13 = A[0,0]*A[1,2]*A[2,3] + A[0,2]*A[1,3]*A[2,0] + A[0,3]*A[1,0]*A[2,2] - A[0,0]*A[1,3]*A[2,2] - A[0,2]*A[1,0]*A[2,3] - A[0,3]*A[1,2]*A[2,0]

    b20 = A[1,0]*A[2,1]*A[3,3] + A[1,1]*A[2,3]*A[3,0] + A[1,3]*A[2,0]*A[3,1] - A[1,0]*A[2,3]*A[3,1] - A[1,1]*A[2,0]*A[3,3] - A[1,3]*A[2,1]*A[3,0]
    b21 = A[0,0]*A[2,3]*A[3,1] + A[0,1]*A[2,0]*A[3,3] + A[0,3]*A[2,1]*A[3,0] - A[0,0]*A[2,1]*A[3,3] - A[0,1]*A[2,3]*A[3,0] - A[0,3]*A[2,0]*A[3,1]
    b22 = A[0,0]*A[1,1]*A[3,3] + A[0,1]*A[1,3]*A[3,0] + A[0,3]*A[1,0]*A[3,1] - A[0,0]*A[1,3]*A[3,1] - A[0,1]*A[1,0]*A[3,3] - A[0,3]*A[1,1]*A[3,0]
    b23 = A[0,0]*A[1,3]*A[2,1] + A[0,1]*A[1,0]*A[2,3] + A[0,3]*A[1,1]*A[2,0] - A[0,0]*A[1,1]*A[2,3] - A[0,1]*A[1,3]*A[2,0] - A[0,3]*A[1,0]*A[2,1]

    b30 = A[1,0]*A[2,2]*A[3,1] + A[1,1]*A[2,0]*A[3,2] + A[1,2]*A[2,1]*A[3,0] - A[1,0]*A[2,1]*A[3,2] - A[1,1]*A[2,2]*A[3,0] - A[1,2]*A[2,0]*A[3,1]
    b31 = A[0,0]*A[2,1]*A[3,2] + A[0,1]*A[2,2]*A[3,0] + A[0,2]*A[2,0]*A[3,1] - A[0,0]*A[2,2]*A[3,1] - A[0,1]*A[2,0]*A[3,2] - A[0,2]*A[2,1]*A[3,0]
    b32 = A[0,0]*A[1,2]*A[3,1] + A[0,1]*A[1,0]*A[3,2] + A[0,2]*A[1,1]*A[3,0] - A[0,0]*A[1,1]*A[3,2] - A[0,1]*A[1,2]*A[3,0] - A[0,2]*A[1,0]*A[3,1]
    b33 = A[0,0]*A[1,1]*A[2,2] + A[0,1]*A[1,2]*A[2,0] + A[0,2]*A[1,0]*A[2,1] - A[0,0]*A[1,2]*A[2,1] - A[0,1]*A[1,0]*A[2,2] - A[0,2]*A[1,1]*A[2,0]

    inv = np.array([[b00, b01, b02, b03], [b10, b11, b12, b13], [b20, b21, b22, b23], [b30, b31, b32, b33]]) / detA

    return inv