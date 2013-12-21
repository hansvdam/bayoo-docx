# encoding: utf-8

"""
Test data builders for text XML elements
"""

from ...unitdata import BaseBuilder


class CT_RowBuilder(BaseBuilder):
    __tag__ = 'w:tr'
    __nspfxs__ = ('w',)
    __attrs__ = ('w:w',)


class CT_TblBuilder(BaseBuilder):
    __tag__ = 'w:tbl'
    __nspfxs__ = ('w',)
    __attrs__ = ()


class CT_TblGridBuilder(BaseBuilder):
    __tag__ = 'w:tblGrid'
    __nspfxs__ = ('w',)
    __attrs__ = ('w:w',)


class CT_TblGridColBuilder(BaseBuilder):
    __tag__ = 'w:gridCol'
    __nspfxs__ = ('w',)
    __attrs__ = ('w:w',)


class CT_TcBuilder(BaseBuilder):
    __tag__ = 'w:tc'
    __nspfxs__ = ('w',)
    __attrs__ = ('w:id',)


def a_gridCol():
    return CT_TblGridColBuilder()


def a_tbl():
    return CT_TblBuilder()


def a_tblGrid():
    return CT_TblGridBuilder()


def a_tc():
    return CT_TcBuilder()


def a_tr():
    return CT_RowBuilder()