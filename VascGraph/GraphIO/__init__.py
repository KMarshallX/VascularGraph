#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Lazy GraphIO exports.
"""

import importlib


_EXPORTS = {
    'ReadMRIGraph': ('VascGraph.GraphIO.ReadMRIGraph', 'ReadMRIGraph'),
    'ReadStackMat': ('VascGraph.GraphIO.ReadStackMat', 'ReadStackMat'),
    'ReadNifti': ('VascGraph.GraphIO.ReadNifti', 'ReadNifti'),
    'ReadPajek': ('VascGraph.GraphIO.ReadPajek', 'ReadPajek'),
    'ReadCenterlineCSV': ('VascGraph.GraphIO.ReadCenterlineCSV', 'ReadCenterlineCSV'),
    'ReadSWC': ('VascGraph.GraphIO.ReadSWC', 'ReadSWC'),
    'WriteSWC': ('VascGraph.GraphIO.WriteSWC', 'WriteSWC'),
    'WritePajek': ('VascGraph.GraphIO.WritePajek', 'WritePajek'),
    'WriteGraphml': ('VascGraph.GraphIO.WriteGraphml', 'WriteGraphml'),
    'ReadCGAL': ('VascGraph.GraphIO.ReadCGAL', 'ReadCGAL'),
    'ReadGraphFromXLSX': ('VascGraph.GraphIO.ReadGraphFromXLSX', 'ReadGraphFromXLSX'),
    'ReadSOAX': ('VascGraph.GraphIO.ReadSOAX', 'ReadSOAX'),
    'ReadVTrails': ('VascGraph.GraphIO.ReadVTrails', 'ReadVTrails'),
    'ReadCASX': ('VascGraph.GraphIO.ReadCASX', 'ReadCASX'),
    'ReadNWKCS31': ('VascGraph.GraphIO.ReadNWKCS31', 'ReadNWKCS31'),
}

__all__ = list(_EXPORTS.keys())


def __getattr__(name):

    if name in _EXPORTS:
        module_name, attr_name = _EXPORTS[name]
        attr = getattr(importlib.import_module(module_name), attr_name)
        globals()[name] = attr
        return attr

    raise AttributeError(name)
