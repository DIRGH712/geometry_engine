import numpy as np
from utils.utils import apply_precision


def calculate_centroid(vertices, precision=2):
    """
    Calculate the centroid of a 3D object based on its vertices.

    Parameters:
    - vertices: a list of vertices where each vertex is represented by [x, y, z].
    - precision: the number of decimal places to round the centroid coordinates.

    Returns:
    - The centroid of the 3D object as a list [x, y, z], rounded to the specified precision.
    """
    if not vertices:
        raise ValueError("Vertex list is empty")

    vertices_array = np.array(vertices)
    if vertices_array.shape[1] != 3:
        raise ValueError("Vertices must be 3-dimensional")

    centroid = np.mean(vertices_array, axis=0)
    return apply_precision(centroid.tolist(), precision)
