import numpy as np


def compute_bounding_box(input_points):
    """
    Compute the Axis-Aligned Bounding Box for a set of 3D points.

    Parameters:
    - points: A NumPy array of shape (N, 3) representing N points in 3D space.

    Returns:
    - A tuple containing two NumPy arrays:
        - min_point: The minimum x, y, z coordinates of the bounding box.
        - max_point: The maximum x, y, z coordinates of the bounding box.
    """
    points = np.array(input_points)
    min_point = np.min(points, axis=0)
    max_point = np.max(points, axis=0)

    return min_point, max_point
