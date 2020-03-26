# -*- coding: utf-8 -*-
# @Date : 2020-01-22
# @Author : water
# @Version : v1.0
# @Desc :

#log = "oplog:[INFO] [2020-02-20 18:00:00] [Sogou-Observer,wml=1,ctime=15,sourcetype=1,vrid=300802,cache=null,javaruntime=0,cost=20,ip=10.134.79.131]"


def main():
    ctimes = list()
    costs = list()
    with open("log", 'r') as f:
        log = f.readline()
        while 1:
            print(log)
            log_each = log.split("Sogou-Observer")[1]
            log_each = log_each.split(",")
            print(log_each)
            log_dict = dict()
            for l in log_each:
                if 'ctime' in l:
                    ctimes.append(int(l.split("=")[1]))
                if 'cost' in l:
                    costs.append(int(l.split("=")[1]))
            log = f.readline()
            if log =="":
                break
    print(ctimes)
    print(costs)



if __name__ == "__main__":
    main()

