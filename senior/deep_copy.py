# -*- coding: utf-8 -*-
# File  : deep_copy.py
# Author: water
# Date  : 2019/12/22
# Desc  : 深拷贝、浅拷贝
#         深拷贝 copy.deepcopy：拷贝全部层级的列表，但对元组不起作用，因为元组不可变，相当于等号赋值。
#         浅拷贝 copy.copy：只拷贝外层列表，不拷贝二、三级以内的列表，但对元组不起作用，因为元组不可变，相当于等号赋值。
#         如果元组里面有列表，此时用deepcopy则会进行拷贝。
#         列表l切片 l[:] 的作用与copy.copy(l)效果是一样的
#         字典d1  d2 = d1.copy() 生成d2的id与d1不同，但是d2、d1的value指向相同。

import copy





if __name__ == "__main__":
    main()
