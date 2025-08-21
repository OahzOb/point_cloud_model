import numpy as np


class Shape2d:
    def __init__(self, vertices: list, connections: list):
        self.vertices = vertices
        self.connections = connections


def random_polygon(num_vertices: int = 3, num_curves: int = 0):
    radians = (np.random.rand(num_vertices)) * (2 * np.pi)
    radians = np.sort(radians)
    dists = np.random.rand(num_vertices)
    vertices_x = np.cos(radians) * dists
    vertices_y = np.sin(radians) * dists
    vertices = np.append(vertices_x, vertices_y, axis=1).tolist()
    connections = ['line'] * num_vertices
    curve_indices = np.random.choice(np.arange(0, num_vertices), num_curves)
    for idx in curve_indices:
        connections[idx] = 'curve'
    return Shape2d(vertices=vertices, connections=connections)


def show_shapes(shape: Shape2d):
    vertices = shape.vertices
    pass
