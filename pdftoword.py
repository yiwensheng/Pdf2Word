import os
from pdf2docx import Converter

def pdf_docx():
    file_path=os.getcwd()
    
    for file in os.listdir(file_path):
        suffname=os.path.splitext(file)[1]
        
        if suffname !='.pdf':
            continue
        filename=os.path.splitext(file)[0]
        pdfname=os.getcwd()+'\\'+file
        docxname=os.getcwd()+'\\'+filename+'.docx'
        cv=Converter(pdfname)
        cv.convert(docxname)
        cv.close()
        print(filename)
        print(docxname)

print('将PDF文档转换为Word文档\n------------------------\n易文胜制作')       
pdf_docx()
        
            