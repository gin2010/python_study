# -*- coding: utf-8 -*-
# @Date : 2020-01-22
# @Author : water
# @Version  : v1.0
# @Desc  :
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

def sigmoid(z):
    return 1/(1+np.exp(-z))

def main():
    nums = np.arange(-10,10,step=1)
    fig ,ax = plt.subplots(figsize=(10,6))
    ax.plot(nums,sigmoid(nums),'r')
    plt.show()

if __name__ == "__main__":
    main()

