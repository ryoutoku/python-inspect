# -*- coding: utf-8 -*-
from types import FunctionType


class Delegator:
    """
    Delegate functions

    usage example:
    # declare class
    dg = Delegator()

    # declare function
    def func_1(sender):
        ...
    def func_2(sender):
        ...

    # add callback
    dg.add_callback(func_1)
    dg = dg + func_2
    dg += func_1

    # do callbacks(called func_1, func_2, func_1)
    dg.do_callback(data)

    # remove last input func_1
    dg.remove_callbakc(func_1)

    # do callbacks(called func_1, func_2)
    dg.do_callback(data)

    # clear all callbacks
    dg.clear_all()
    """

    def __init__(self):
        self._callbacks = []

    def add(self, func):
        """add callback

        Args:
            func : delegate function
        """
        if isinstance(func, FunctionType):
            self._callbacks.append(func)
        else:
            raise TypeError('func is not FunctionType')

    def remove(self, func):
        """remove callback

        Args:
            func : remove function if func is added
        """
        if func in self._callbacks:
            tmp = self._callbacks[::-1]
            tmp.remove(func)
            self._callbacks = tmp[::-1]

    def do(self, arg=None):
        """do callback

        Args:
            arg : callback arg
        """
        if arg is None:
            for func in self._callbacks:
                func()
        else:
            for func in self._callbacks:
                func(arg)

    def do_return(self, arg=None):
        """do callback and return value

        Args:
            arg : callback arg

        Return:
            yield func result
        """
        if arg is None:
            for func in self._callbacks:
                yield func()
        else:
            for func in self._callbacks:
                yield func(arg)

    def clear(self):
        """clear added callback"""
        self._callbacks.clear()

    def __add__(self, func):
        """add callback using +

        Args:
            func : add function

        Return:
            new Delegator
        """
        tmp = self.copy()
        tmp.add(func)
        return tmp

    def __iadd__(self, func):
        """add callback using +=

        Args:
            func : add function

        Return:
            self
        """
        self.add(func)
        return self

    def __sub__(self, func):
        """remove callback using -

        Args:
            func : remove function

        Return:
            new Delegator
        """
        tmp = self.copy()
        tmp.remove(func)
        return tmp

    def __isub__(self, func):
        """remove callback using -=

        Args:
            func : remove function

        Return:
            self
        """
        self.remove(func)
        return self

    def copy(self):
        """copy"""
        tmp = Delegator()
        for f in self._callbacks:
            tmp.add(f)
        return tmp
