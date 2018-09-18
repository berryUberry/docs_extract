# encoding: utf-8 
""" 
@author: wangkai 
@contact: berryberryry@gmail.com
@version: 1.0 
@license: Apache Licence 
@file: cell.py 
@time: 18-9-18 下午3:24 

这一行开始写关于本文件的说明与解释 
"""


class Cell(object):
    # def __init__(self, cell_id, left_cells_id, right_cells_id, upper_cells_id, lower_cells_id):
    #     self.cell_id = cell_id
    #     self.left_cells_id = left_cells_id
    #     self.right_cells_id = right_cells_id
    #     self.upper_cells_id = upper_cells_id
    #     self.lower_cells_id = lower_cells_id
    def __init__(self, cell_id):
        self.cell_id = cell_id

    @property
    def _left_cells_id(self):
        return self._left_cells_id
    @_left_cells_id.setter
    def _left_cells_id(self, left_cell_id):
        self._left_cells_id = left_cell_id
    @property
    def _grid_col(self):
        return self._grid_col
    @_grid_col.setter
    def _grid_col(self, grid_col):
        self._grid_col = grid_col
