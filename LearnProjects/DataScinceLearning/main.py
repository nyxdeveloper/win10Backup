import os
import matplotlib.pyplot as plt
import random
import numpy as np


# def save(name='', fmt='png'):
#     pwd = os.getcwd()
#     iPath = './pictures/{}'.format(fmt)
#     if not os.path.exists(iPath):
#         os.mkdir(iPath)
#     os.chdir(iPath)
#     plt.savefig('{}.{}'.format(name, fmt), fmt='png')
#     os.chdir(pwd)
#     # plt.close()


fig = plt.figure()
for i in range(1000):
    plt.scatter(random.randint(1, 1000), random.randint(1, 1000), edgecolors='red')

plt.show()