import unittest
from modules.get_centroid import calculate_centroid


class TestCalculateCentroid(unittest.TestCase):
    def test_calculate_centroid_valid_input(self):
        vertices = [[0, 0, 0], [2, 0, 0], [0, 2, 0], [0, 0, 2]]
        expected_centroid = [0.5, 0.5, 0.5]
        centroid = calculate_centroid(vertices)
        self.assertEqual(centroid, expected_centroid, "The calculated centroid does not match the expected value.")

    def test_calculate_centroid_precision(self):
        vertices = [[0.333, 0.333, 0.333], [2.333, 0.333, 0.333], [0.333, 2.333, 0.333], [0.333, 0.333, 2.333]]
        expected_centroid = [0.83, 0.83, 0.83]  # Precision set to 2
        centroid = calculate_centroid(vertices, precision=2)
        self.assertEqual(centroid, expected_centroid,
                         "The calculated centroid with precision does not match the expected value.")

    def test_calculate_centroid_empty_input(self):
        vertices = []
        with self.assertRaises(ValueError):
            calculate_centroid(vertices)

    def test_calculate_centroid_with_negative_coordinates(self):
        vertices = [[-1, -1, -1], [1, 0, 0], [0, 1, 0], [0, 0, 1]]
        expected_centroid = [0, 0, 0]
        centroid = calculate_centroid(vertices)
        self.assertEqual(centroid, expected_centroid,
                         "The calculated centroid with negative coordinates does not match the expected value.")

    def test_calculate_centroid_large_numbers(self):
        vertices = [[10000, 10000, 10000], [20000, 10000, 10000], [10000, 20000, 10000], [10000, 10000, 20000]]
        expected_centroid = [12500.0, 12500.0, 12500.0]
        centroid = calculate_centroid(vertices, precision=0)  # Set precision to 0 for this case, if it helps
        self.assertEqual(centroid, expected_centroid,
                         "The calculated centroid with large numbers does not match the expected value.")

    def test_calculate_centroid_complex_shape(self):
        vertices = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [-1, -2, -3], [-4, -5, -6], [-7, -8, -9]]
        expected_centroid = [0, 0, 0]
        centroid = calculate_centroid(vertices)
        self.assertEqual(centroid, expected_centroid,
                         "The calculated centroid of a complex shape does not match the expected value.")

    def test_calculate_centroid_high_precision(self):
        vertices = [[0.111, 0.222, 0.333], [2.444, 0.555, 0.666], [0.777, 2.888, 0.999], [0.101, 0.202, 0.303]]
        expected_centroid = [0.86, 0.97, 0.58]  # Assuming precision of 2
        centroid = calculate_centroid(vertices, precision=2)
        self.assertEqual(centroid, expected_centroid,
                         "The calculated centroid with high precision does not match the expected value.")

    def test_calculate_centroid_single_vertex(self):
        vertices = [[5, 5, 5]]
        expected_centroid = [5, 5, 5]
        centroid = calculate_centroid(vertices)
        self.assertEqual(centroid, expected_centroid,
                         "The calculated centroid of a single vertex does not match the expected value.")

    def test_calculate_centroid_non_3d_input(self):
        vertices = [[1, 2], [3, 4]]  # 2D points instead of 3D
        with self.assertRaises(ValueError):
            calculate_centroid(vertices)


if __name__ == '__main__':
    unittest.main()
