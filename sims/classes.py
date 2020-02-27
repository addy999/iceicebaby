from free import *

class Rock:
    
    ''' Units in SI, size -> mm, mass -> kg'''
    
    def __init__(self, x,y,z, ice_ratio, basalt_type='avg'):
        
        self.x = x
        self.y = y
        self.z = z
        self.ice_ratio = ice_ratio
        self.basalt_type = basalt_type

    def get_radius(self):
        ''' Norm of x,y,z '''
        return (self.x**2+self.y**2+self.z**2)**0.5
    
    # def create_fem_part(self, shape = 'sphere'):
        
        