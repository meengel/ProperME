### Michael Engel ### 2023-09-15 ### TEST_ProperME.py ###
import numpy as np
from ProperME import ProperME

class Circle:
    properme = ProperME(
        dependingdict = {
            "get_radius": [],
            "get_diameter": ["get_radius"],
            "get_perimeter": ["get_diameter"],
            "get_area": ["get_radius"],
            "get_color": ["get_perimeter","get_area"]
        },
        computegraphname = "_computegraph",
        active = True
    )
    
    def __init__(self, radius=1):
        self._computegraph = None
        self._radius = radius
    
    # radius
    @properme
    def get_radius(self):
        return self._radius
    
    @properme
    def set_radius(self, value):
        self._radius = value
    
    # diameter
    @properme
    def get_diameter(self):
        self._diameter = 2*self.get_radius()
        return self._diameter
        
    # perimeter
    @properme
    def get_perimeter(self):
        self._perimeter = self.get_diameter()*np.pi
        return self._perimeter
    
    # area
    @properme
    def get_area(self):
        self._area = self.get_radius()**2*np.pi
        return self._area
    
    # color
    @properme
    def get_color(self):
        self._color = self.get_perimeter()+np.random.randn()*self.get_area()
        return self._color

if __name__=="__main__":
    circle = Circle(radius=1.5)
    print("Dependency Graph")
    print(circle.properme._dependent)
    print()
    
    print("Getting the radius!")
    print(circle.get_radius())
    print(circle._computegraph)
    print()
    
    print("Getting the radius a second time!")
    print(circle.get_radius())
    print(circle._computegraph)
    print()
    
    print("Getting the perimeter!")
    print(circle.get_perimeter())
    print(circle._computegraph)
    print()
    
    print("Getting the diameter which does not involve any new calculation now!")
    print(circle.get_diameter())
    print(circle._computegraph)
    print()
    
    print("Getting the area which has not been computed yet!")
    print(circle.get_area())
    print(circle._computegraph)
    print()
    
    print("Setting the radius which affects all calculations!")
    print(circle.set_radius(2))
    print(circle._computegraph)
    print()
    
    print("Getting the area!")
    print(circle.get_area())
    print(circle._computegraph)
    print()
    
    print("Getting the color!")
    print(circle.get_color())
    print(circle._computegraph)
    print()
