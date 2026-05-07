#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 23:36:33 2020

@author: rdamseh
"""

from VascGraph.Skeletonize import Skeleton
from VascGraph.GraphIO import ReadNifti, ReadStackMat, WriteGraphml
from VascGraph.GraphLab import StackPlot
from VascGraph.Tools.VisTools import visG

if __name__=='__main__':
    
    '''
    This demo explains how to graph using Skeleton module	
    '''    
    s=ReadStackMat('synth1.mat').GetOutput()
    # NIfTI input can be used instead:
    # s=ReadNifti('synth1.nii').GetOutput()

    #contraction
    speed_param=0.05 # (gamma)
    dist_param=0.5 # (alpha)
    med_param=0.5 # (beta)
    degree_threshold=5.0 # used to check if a node is a skeletal node (formula 9)
    sampling=1 # larger the number, smaller the number of nodes in the initial graph
    clustering_r=1 # merge nodes that collapse into roughly 1-voxel spatial bins; larger values allow more aggressive merging; smaller values preserve more nodes but may lead to more noisy skeletons

    #contraction
    stop_param=0.001 # controls the convergence criterion (sigma_a)
    n_free_iteration=0 #number of contraction iteration before checking for convergence
    
    #refinement
    area_param=50.0 # area of polygens to be decimated (formula 10)
    poly_param=10 # number of nodes forming a polygon (sigma_n)
    
    sk=Skeleton(label=s, 
                speed_param=speed_param,
                dist_param=dist_param,
                med_param=med_param,
                sampling=sampling,
                degree_threshold=degree_threshold,
                clustering_resolution=clustering_r,
                stop_param=stop_param,
                n_free_iteration=n_free_iteration,
                area_param=area_param,
                poly_param=poly_param)
    
    sk.Update()
    
    fullgraph=sk.GetOutput()

    # Save the output graph in SkelHub graphviz-compatible GraphML format.
    # WriteGraphml(path='', name='mygraph.graphml', graph=fullgraph)

    print('--Visualize final skeleton ...')
    splot = StackPlot(new_engine=True)    
    splot.Update((s>0).astype(int))
    visG(fullgraph)





