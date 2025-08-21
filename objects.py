from abc import ABC, abstractmethod
import numpy as np


class Shape2d(ABC):

    @property
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def get_2d_obbx(self):
        pass

    @abstractmethod
    def get_2d_aabbx(self):
        pass


class Polygon(Shape2d):
    def __init__(self, vertices):
        self.vertices = vertices


def random_polygon(num_vertices: int = 3):
    radians = (np.random.rand(num_vertices)) * (2 * np.pi)
    radians = np.sort(radians)
    dists = np.random.rand(num_vertices)
    vertices_x = np.cos(radians) * dists
    vertices_y = np.sin(radians) * dists

    return


class Shape3d(ABC):

    @property
    @abstractmethod
    def volume(self):
        pass

    @property
    @abstractmethod
    def surface_area(self):
        pass

    @abstractmethod
    def get_3d_obbx(self):
        pass

    @abstractmethod
    def get_3d_aabbx(self):
        pass


class Cube(Shape3d):
    def __init__(self):
        pass


class Cuboid(Shape3d):
    def __init__(self):
        pass