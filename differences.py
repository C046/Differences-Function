# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 19:14:22 2022

@author: hadaw
"""



def _ifunc_():
    def _g_():
        # Try to import cupy
        try:
            import cupy as cp
            
        except ImportError as e:
            del e
            # If cupy fails attempt to import numpy
            try:
                import numpy as cp
            
            except ImportError:
                # If all imports fail, set cp to None
                cp = None
                
        while True:
            yield cp


    for g in _g_():
        return g
    
try:
    cp = _ifunc_()
    
except ImportError:
    cp = None    
    
    del _ifunc_

    
def diff(List):
    
    # We use a generator because generators are fast
    def _g_(List):
        # We dont need to add another conditional because we instantly
        # return the finished list utilizing either cpu or gpu.
        while True:
            # Try to use imports or just do it normally
            try:
                yield [cp.subtract(y,x) for x,y in zip(List[:-1], List[1:])]
            
            except Exception:
                yield [y-x for x,y in zip(List[:-1], List[1:])]
                
    # Here we can actually automate the generator function so that it acts
    # like a normal function
    for g in _g_(List):
        # Simply return the finished list
        return g





    
    
    
    
    