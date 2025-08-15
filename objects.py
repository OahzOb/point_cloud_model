from abc import ABC, abstractmethod
import numpy as np


class Shape2d(ABC):

    @property
    @abstractmethod
    def area(self):
        pass


class Square(Shape2d):
    def __init__(self, edges: list):
        lene = len(edges)
        if lene < 1:
            raise ValueError("Can't create a square with 0 edges!")
        else:
            edges = edges[0] * 4
        self.edges = edges
        self._area = self.edges[0] * self.edges[2]
    
    @property
    def area(self):
        return self._area

    @classmethod
    def from_edges(cls, edge):
        edges = [edge] * 4
        return Square(edges=edges)


class Rectangle(Shape2d):
    def __init__(self, edges: list):
        self.edges = edges
        self._area = self.edge[1] * self.edge[2]

    @property
    def area(self):
        return self._area


class Triangle(Shape2d):
    def __init__(self, edges: list, radians: list, angles: list):
        self.edges = edges
        self.radians = radians
        self.angles = angles
        self._area = self.edges[0] * np.sin(self.radians[0]) * self.edges[1] / 2

    @property
    def area(self):
        return self._area


class Circle(Shape2d):
    def __init__(self, radius: float):
        self.radius = radius
        self._area = np.pi * (self.radius ** 2)


    @property
    def area(self):
        return self._area


class Shape3d(ABC):

    @property
    @abstractmethod
    def volume(self):
        pass

    @property
    @abstractmethod
    def area(self):
        pass
