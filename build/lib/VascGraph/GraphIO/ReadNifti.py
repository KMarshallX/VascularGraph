#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
NIfTI stack reader for VascGraph.
"""

import nibabel as nib
import numpy as np


class ReadNifti:

    def __init__(self, filename=None):

        self.filename = filename
        self.__Image = None
        self.__Stack = None

    def __ReadFile(self):

        self.__Image = nib.load(self.filename)
        self.__Stack = np.asarray(self.__Image.dataobj)
        return self.__Stack

    def GetOutput(self):

        try:
            if self.__Stack is None:
                return self.__ReadFile()
            return self.__Stack
        except:
            print('Cannot read nifti file!')

    def GetAffine(self):

        try:
            if self.__Image is None:
                self.__ReadFile()
            return self.__Image.affine.copy()
        except:
            print('Cannot read nifti affine!')

    def GetHeader(self):

        try:
            if self.__Image is None:
                self.__ReadFile()
            return self.__Image.header.copy()
        except:
            print('Cannot read nifti header!')
