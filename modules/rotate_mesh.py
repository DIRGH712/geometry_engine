import numpy as np
from utils.utils import apply_precision


def rotate_mesh(mesh, angle, axis='Y', precision=2):
    # Convert input mesh to NumPy array
    mesh = np.array(mesh)

    # Convert angle from degrees to radians
    angle_rad = np.radians(angle)

    # Define rotation matrices
    if axis.upper() == 'X':
        rotation_matrix = np.array([[1, 0, 0],
                                    [0, np.cos(angle_rad), -np.sin(angle_rad)],
                                    [0, np.sin(angle_rad), np.cos(angle_rad)]])
    elif axis.upper() == 'Y':
        rotation_matrix = np.array([[np.cos(angle_rad), 0, np.sin(angle_rad)],
                                    [0, 1, 0],
                                    [-np.sin(angle_rad), 0, np.cos(angle_rad)]])
    elif axis.upper() == 'Z':
        rotation_matrix = np.array([[np.cos(angle_rad), -np.sin(angle_rad), 0],
                                    [np.sin(angle_rad), np.cos(angle_rad), 0],
                                    [0, 0, 1]])
    else:
        raise ValueError("Axis must be 'X', 'Y', or 'Z'")

    # Apply rotation to each point in the mesh
    rotated_mesh = np.dot(mesh, rotation_matrix)
    final_result = apply_precision(rotated_mesh, precision)

    return final_result.tolist()
