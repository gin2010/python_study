# -*- coding: utf-8 -*-
# @Date : 2020-01-22
# @Author : water
# @Version  : v1.0
# @Desc  :

def format_txt():
    f = open("basketball_english",'r')
    result = open("basketball_english_result",'a')
    for content in f.readlines():
        content = content.strip()
        if content == "":
            continue
        else:
            content = content.replace("．",".").split('.')
            if len(content) == 2:
                index = content[1].rfind(' ')
                format_content = content[1][:index].strip() + '##' + content[1][index+1:] + '\n'
                result.write(format_content)
            else:
                print(f"***********error**********:{content}")
                break
    print("-----------finish---------")
    f.close()
    result.close()


def main():
    format_txt()


if __name__ == "__main__":
    main()

