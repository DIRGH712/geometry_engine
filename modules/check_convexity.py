import numpy as np


def are_points_collinear(points):
    if len(points) < 3:
        return True  # Trivially collinear or not enough points to determine otherwise

    p0, p1 = np.array(points[0]), np.array(points[1])
    for point in points[2:]:
        p2 = np.array(point)
        if np.linalg.norm(np.cross(p1 - p0, p2 - p0)) != 0:
            return False  # Found three points that do not lie on a single line
    return True


def is_convex_polygon(vertices):
    # Convert vertices list to a set of tuples to check for duplicates
    if len(vertices) != len(set(tuple(v) for v in vertices)):
        return "Polygon has repeated vertices, which is not valid."

    if len(vertices) < 3:
        return "Not a polygon or not enough vertices to determine convexity."

    if are_points_collinear(vertices):
        return "Vertices are collinear, thus not forming a convex polygon."

    # Check for non-planarity by ensuring all cross products are parallel
    normals = []
    for i in range(len(vertices)):
        p0, p1, p2 = np.array(vertices[i]), np.array(vertices[(i + 1) % len(vertices)]), np.array(
            vertices[(i + 2) % len(vertices)])
        normal = np.cross(p1 - p0, p2 - p1)
        normals.append(normal / np.linalg.norm(normal) if np.linalg.norm(normal) else normal)

    # If normals are not all the same, the polygon is non-planar
    if any(not np.allclose(normals[0], n) for n in normals[1:]):
        return "The polygon is non-planar and cannot be checked for convexity."

    positive = None
    for i in range(len(vertices)):
        A, B, C = vertices[i], vertices[(i + 1) % len(vertices)], vertices[(i + 2) % len(vertices)]
        AB = np.array(B) - np.array(A)
        BC = np.array(C) - np.array(B)
        cross_prod = np.cross(AB, BC)
        if i == 0:
            ref_cross_prod = cross_prod
            continue
        if np.dot(ref_cross_prod, cross_prod) < 0:
            return "The polygon is not convex"

    return "The polygon is convex."
