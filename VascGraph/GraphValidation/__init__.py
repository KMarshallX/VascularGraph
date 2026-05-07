#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Lazy graph validation exports.
"""

import importlib


_EXPORTS = {
    'ValidateDiadem': ('VascGraph.GraphValidation.ValidateDiadem', 'ValidateDiadem'),
    'ValidateNetMets': ('VascGraph.GraphValidation.ValidateNetMets', 'ValidateNetMets'),
    'ValidateRadius': ('VascGraph.GraphValidation.ValidateRadius', 'ValidateRadius'),
}

__all__ = list(_EXPORTS.keys())


def __getattr__(name):

    if name in _EXPORTS:
        module_name, attr_name = _EXPORTS[name]
        attr = getattr(importlib.import_module(module_name), attr_name)
        globals()[name] = attr
        return attr

    raise AttributeError(name)
