import scipy.io as spio
import numpy as np
import os

print('Loading movie ratings dataset.\n\n')

mat = spio.loadmat('ex8_movies.mat', squeeze_me=True)

Y = mat['Y']
R = mat['R']

n = sum(R[0,])
pom = sum(np.multiply(Y[0,],R[0,]))

print('Average rating for movie 1 (Toy Story): {:f} / 5\n\n').format(pom/float(n))

mat = spio.loadmat('ex8_movieParams.mat', squeeze_me=True)

X = mat['X']
Theta = mat['Theta']
num_users = mat['num_users']
num_movies = mat['num_movies']
num_features = mat['num_features']

# Reduce the data set size so that this runs faster
num_users = 4
num_movies = 5
num_features = 3

###
pomX = np.zeros((num_movies, num_features))

for i in range(num_movies):
    for j in range(num_features):
        pomX[i,j] = X[i,j]
    
X = pomX
###
pomTheta = np.zeros((num_users, num_features))

for i in range(num_users):
    for j in range(num_features):
        pomTheta[i,j] = Theta[i,j]
    
Theta = pomTheta
###
pomY = np.zeros((num_movies, num_users))

for i in range(num_movies):
    for j in range(num_users):
        pomY[i,j] = Y[i,j]
    
Y = pomY
###
pomR = np.zeros((num_movies, num_users))

for i in range(num_movies):
    for j in range(num_users):
        pomR[i,j] = R[i,j]
    
R = pomR
###

