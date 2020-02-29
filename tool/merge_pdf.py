# -*- coding: utf-8 -*-
# @Date : 2020-01-22
# @Author : water
# @Version  : v1.0
# @Desc  :

import os
from PyPDF2 import PdfFileReader, PdfFileWriter


def merge_pdf(pdf_files, outfn):
    pdf_output = PdfFileWriter()
    for infn in pdf_files:
        pdf_input = PdfFileReader(open(infn, 'rb'))
        # 获取 pdf 共用多少页
        page_count = pdf_input.getNumPages()
        print(page_count)
        for i in range(page_count):
            pdf_output.addPage(pdf_input.getPage(i))
    pdf_output.write(open(outfn, 'wb'))

def main():
    pdf_files = list()
    dir_file = os.path.dirname(os.path.abspath(__file__))
    result_pdf = os.path.join(dir_file,'pdfs','result1.pdf')
    for i in range(2,4):
        pdf_files.append(os.path.join(dir_file,'pdfs',str(i)+".pdf"))
    merge_pdf(pdf_files,result_pdf)




if __name__ == "__main__":
    main()

