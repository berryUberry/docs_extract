# encoding: utf-8 
""" 
@author: wangkai 
@contact: berryberryry@gmail.com
@version: 1.0 
@license: Apache Licence 
@file: table.py 
@time: 18-9-18 下午3:23 

这一行开始写关于本文件的说明与解释 
"""

from docshannon.table.cell import Cell
class Table(object):
    def __init__(self, table_id, rows, cols):
        self.table_id = table_id
        self.rows = rows
        self.cols = cols

    @property
    def cells(self):
        return self.cells


    def add_cell(self,cell):
        self.cells.append(cell)
