### Michael Engel ### 2023-09-15 ### ProperME.py ###
from dill.source import getname
import numpy as np

class ProperME:
    def __init__(self, dependingdict, computegraphname="_computegraph", active=True):
        self.active = active
        
        self._depending = dependingdict
        
        self._has_children = self._build_has_childrendict(self._depending) # determine whether any other method depends on key-method
        self._dependent = {key:[] for key in self._depending.keys()}
        for key in self._dependent.keys():
            # recursive dependency graph calculation for key-method i.e. which methods are depending on key-method
            self._build_dependentdict(
                key = key,
                dependentlist = self._dependent[key],
                visited = {key:False for key in self._depending.keys()}
            )
            
            # make dependency graph unique
            self._dependent[key] = list(set(self._dependent[key])) 
        
        self._computegraphname = computegraphname # name of attribute which should be living in decorated class
        
    def __call__(self,fun):
        if self.active:
            funname = getname(fun) # determine name of decorated function
            mode = funname.split("_")[0] # determine if get or set mode
            varname = "_"+"_".join(funname.split("_")[1:]) # determine name of property
        
            if "get"==mode: # for getters
                def getter(*args,**kwargs):
                    _computegraph = self._build_computegraph(args[0]) # load computegraph from obj -> important for pickle
                        
                    if not hasattr(args[0], varname) or _computegraph[funname]: # check if already computed or to be computed
                        res = fun(*args,**kwargs) # compute method
                        _computegraph[funname] = False # mark method as computed
                        return res
                    else:
                        return getattr(args[0],varname) # return existing
                return getter
            
            else: # for setters
                def setter(*args,**kwargs):
                    _computegraph = self._build_computegraph(args[0]) # load computegraph from obj -> important for pickle
                    # mark all dependent methods as to-compute
                    for key in self._dependent["get"+varname]:
                        _computegraph[key] = True # mark method as to-compute
                    return fun(*args,**kwargs)
                return setter   
            
        else:
            return fun
    
    @staticmethod
    def _build_has_childrendict(dependingdict):
        has_children_dict = {}
        for key in dependingdict.keys():
            has_children_dict[key] = np.any([True if key in dependingdict[key2] else False for key2 in dependingdict.keys()])
        return has_children_dict
    
    def _build_dependentdict(self, key, dependentlist, visited):
        dependentlist.extend(list(set([key2 if key in self._depending[key2] else key for key2 in self._depending.keys()])))
        visited[key] = True
        for key_ in dependentlist:
            if self._has_children[key_] and not visited[key_]:
                self._build_dependentdict(key_, dependentlist, visited)
    
    def _build_computegraph(self, obj):
        _computegraph = getattr(obj, self._computegraphname)
        if not _computegraph:
            setattr(obj, self._computegraphname, {key:True for key in self._dependent.keys()})
            _computegraph = getattr(obj, self._computegraphname)
        return _computegraph
