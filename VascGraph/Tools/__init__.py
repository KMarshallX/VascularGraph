#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Lazy tools exports.
"""

import importlib


__all__ = ['VisTools', 'CalcTools', 'ExtraTools']


def __getattr__(name):

    if name in __all__:
        module = importlib.import_module('VascGraph.Tools.' + name)
        globals()[name] = module
        return module

    raise AttributeError(name)
