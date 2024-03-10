import unittest
import numpy as np

from modules.check_convexity import is_convex_polygon


class TestConvexity(unittest.TestCase):

    def test_convex_polygon(self):
        # Convex polygon
        vertices = [[0, 0, 0], [2, 0, 0], [2, 2, 0], [0, 2, 0]]
        self.assertEqual(is_convex_polygon(vertices), "The polygon is convex.")

    def test_collinear_points(self):
        # Collinear points
        vertices = [[0, 0, 0], [1, 1, 1], [2, 2, 2]]
        self.assertEqual(is_convex_polygon(vertices), "Vertices are collinear, thus not forming a convex polygon.")

    def test_insufficient_vertices(self):
        # Insufficient vertices to form a polygon
        vertices = [[0, 0, 0], [1, 1, 1]]
        self.assertEqual(is_convex_polygon(vertices), "Not a polygon or not enough vertices to determine convexity.")

    def test_regular_convex_polygon(self):
        # Regular convex polygon (hexagon)
        vertices = [[1, 0, 0], [0.5, np.sqrt(3) / 2, 0], [-0.5, np.sqrt(3) / 2, 0],
                    [-1, 0, 0], [-0.5, -np.sqrt(3) / 2, 0], [0.5, -np.sqrt(3) / 2, 0]]
        self.assertEqual(is_convex_polygon(vertices), "The polygon is convex.")

    def test_polygon_with_repeated_vertices(self):
        # Polygon with repeated vertices (should handle as error or specific case)
        vertices = [[0, 0, 0], [2, 0, 0], [2, 2, 0], [0, 2, 0], [0, 2, 0]]
        self.assertEqual(is_convex_polygon(vertices), "Polygon has repeated vertices, which is not valid.")

    def test_non_planar_polygon(self):
        # Non-planar polygon (should return an error or specific message)
        vertices = [[0, 0, 0], [1, 1, 1], [2, 2, 0], [3, 3, -1]]
        self.assertEqual(is_convex_polygon(vertices), "The polygon is non-planar and cannot be checked for convexity.")


if __name__ == '__main__':
    unittest.main()
