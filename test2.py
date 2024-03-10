import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import ConvexHull

def minimum_bounding_box(points):
    points_array = np.array(points)
    hull = ConvexHull(points_array)

    min_area = float('inf')
    min_box = None

    for simplex in hull.simplices:
        edge = points_array[simplex]

        orientation = np.arctan2(edge[1, 1] - edge[0, 1], edge[1, 0] - edge[0, 0])

        rotation_matrix = np.array([[np.cos(orientation), -np.sin(orientation), 0],
                                    [np.sin(orientation), np.cos(orientation), 0],
                                    [0, 0, 1]])

        rotated_points = np.dot(points_array - points_array[simplex[0]], rotation_matrix.T)

        min_values = np.min(rotated_points, axis=0)
        max_values = np.max(rotated_points, axis=0)

        area = np.prod(max_values - min_values)

        if area < min_area:
            min_area = area
            min_box = {
                'min_point': min_values,
                'max_point': max_values,
                'orientation': orientation,
                'area': min_area
            }

    return min_box, hull

def visualize_3d_bounding_box(points_array, min_box, hull):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Plot the original points
    ax.scatter(points_array[:, 0], points_array[:, 1], points_array[:, 2], c='b', marker='o', label='Points')

    # Plot the convex hull
    for simplex in hull.simplices:
        edge = points_array[simplex]
        ax.plot(edge[:, 0], edge[:, 1], edge[:, 2], 'r-')

    # Plot the minimum bounding box
    rect_points = np.array([
        [min_box['min_point'][0], min_box['min_point'][1], min_box['min_point'][2]],
        [min_box['min_point'][0], min_box['max_point'][1], min_box['max_point'][2]],
        [min_box['max_point'][0], min_box['min_point'][1], min_box['min_point'][2]],
        [min_box['max_point'][0], min_box['max_point'][1], min_box['min_point'][2]],
        [min_box['min_point'][0], min_box['max_point'][1], min_box['min_point'][2]],
        [min_box['min_point'][0], min_box['min_point'][1], min_box['max_point'][2]],
        [min_box['max_point'][0], min_box['min_point'][1], min_box['max_point'][2]],
        [min_box['max_point'][0], min_box['max_point'][1], min_box['max_point'][2]],

    ])

    rect_points = np.vstack([rect_points, rect_points[0]])  # Close the loop

    ax.plot(rect_points[:, 0], rect_points[:, 1], rect_points[:, 2], 'g-', linewidth=2, label='Bounding Box')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.legend()

    plt.show()

# Example usage:
num_points = 200

points = np.random.rand(num_points, 3)
result, hull = minimum_bounding_box(points)
print(result)

# Visualize the 3D bounding box
visualize_3d_bounding_box(np.array(points), result, hull)
