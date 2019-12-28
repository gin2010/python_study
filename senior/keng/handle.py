# -*- coding: utf-8 -*-
# File  : handle.py
# Author: water
# Date  : 2019/12/28
# Desc  :

# 这种方式导入的只是FLAG变量的值的引用，这个模块里的FLAG指向的是common里FLAG值的内存地址，二者ID不同
# 因此在其他模块FLAG=True只会将值的指向变为True的内存地址
from common import FLAG
# 这种方式是将整个模块导入，导入是common的FLAG变量
import common


def modify_flag():
    # FLAG = True
    common.FLAG = True

    print("modify_flag",common.FLAG)


if __name__ == "__main__":
    main()
