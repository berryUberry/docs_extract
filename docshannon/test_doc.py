# encoding: utf-8 
""" 
@author: wangkai 
@contact: berryberryry@gmail.com
@version: 1.0 
@license: Apache Licence 
@file: test_doc.py 
@time: 18-9-18 下午2:49 

这一行开始写关于本文件的说明与解释 
"""

from docshannon.doc import DOCDocument
import mammoth
def run():
    doc = DOCDocument("/home/berryberry/doc/3.docx", "/home/berryberry/doc")
    doc.get_doc_text()
    doc.get_doc_images()
    # doc.get_doc_tables()
if __name__ == '__main__':
    run()
