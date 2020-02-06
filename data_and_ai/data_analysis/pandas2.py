# -*- coding: utf-8 -*-
# @Date : 2020-01-22
# @Author : water
# @Version  : v1.0
# @Desc  :
import pandas as pd
import numpy as np

coffee_data = [
    {'country':'US','state':'LA','num':11},
    {'country':'US','state':'OKC','num':1},
    {'country':'US','state':'NW','num':103},
    {'country':'US','state':'ST','num':20},
    {'country':'US','state':'FL','num':2},
    {'country':'US','state':'DE','num':50},
    {'country':'CN','state':'BJ','num':50},
    {'country':'CN','state':'SH','num':70},
    {'country':'CN','state':'SD','num':11},
    {'country':'CN','state':'WH','num':21},
    {'country':'CN','state':'GZ','num':35},
    {'country':'CN','state':'TJ','num':15},
    {'country':'CN','state':'SZ','num':33},
    {'country':'CN','state':'CD','num':24},
    {'country':'CN','state':'NJ','num':14},
    {'country':'CN','state':'SC','num':16},
    {'country':'CN','state':'DL','num':5},
    {'country':'CN','state':'JL','num':2},
    {'country':'CN','state':'HLJ','num':2},
    {'country':'CN','state':'HN','num':3},
    {'country':'CN','state':'BJ','num':100},


]

def main():
    data = pd.DataFrame(coffee_data)
    # print(data)
    country_desc = data.groupby('country').sum()
    # print(country_desc)
    country_state = data.groupby(by=[data['country'],data['state']]).sum()
    print(country_state)
    print("----------------------------------")
    print(country_state.loc['CN'].loc['BJ'])


if __name__ == "__main__":
    main()

