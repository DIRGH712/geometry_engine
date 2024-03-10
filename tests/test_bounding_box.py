import unittest
import numpy as np
from modules.bounding_box import compute_bounding_box


class TestBoundingBox(unittest.TestCase):

    def test_with_valid_points(self):
        points = np.array([[0, 0, 0], [2, 2, 2], [1, 1, 1], [-1, -1, -1]])
        expected_min_point = np.array([-1, -1, -1])
        expected_max_point = np.array([2, 2, 2])
        min_point, max_point = compute_bounding_box(points)
        np.testing.assert_array_equal(min_point, expected_min_point, "The min point does not match the expected value.")
        np.testing.assert_array_equal(max_point, expected_max_point, "The max point does not match the expected value.")

    def test_with_empty_list(self):
        points = np.array([])
        with self.assertRaises(ValueError):
            compute_bounding_box(points)

    def test_with_single_point(self):
        points = np.array([[1, 1, 1]])
        expected_min_point = np.array([1, 1, 1])
        expected_max_point = np.array([1, 1, 1])
        min_point, max_point = compute_bounding_box(points)
        np.testing.assert_array_equal(min_point, expected_min_point,
                                      "The min point should be equal to the single point for a single-point input.")
        np.testing.assert_array_equal(max_point, expected_max_point,
                                      "The max point should be equal to the single point for a single-point input.")

    def test_with_collinear_points(self):
        points = np.array([[0, 0, 0], [1, 1, 1], [2, 2, 2]])
        expected_min_point = np.array([0, 0, 0])
        expected_max_point = np.array([2, 2, 2])
        min_point, max_point = compute_bounding_box(points)
        np.testing.assert_array_equal(min_point, expected_min_point,
                                      "The min point does not match the expected value for collinear points.")
        np.testing.assert_array_equal(max_point, expected_max_point,
                                      "The max point does not match the expected value for collinear points.")

    def test_with_large_number_of_points(self):
        points = np.random.randint(-1000, 1000, (1000, 3))
        expected_min_point = np.min(points, axis=0)
        expected_max_point = np.max(points, axis=0)
        min_point, max_point = compute_bounding_box(points)
        np.testing.assert_array_equal(min_point, expected_min_point,
                                      "Min point incorrect for a large number of points.")
        np.testing.assert_array_equal(max_point, expected_max_point,
                                      "Max point incorrect for a large number of points.")

    def test_with_points_in_one_quadrant(self):
        points = np.array([[5, 5, 5], [6, 7, 6], [7, 5, 7]])
        expected_min_point = np.array([5, 5, 5])
        expected_max_point = np.array([7, 7, 7])
        min_point, max_point = compute_bounding_box(points)
        np.testing.assert_array_equal(min_point, expected_min_point, "Min point incorrect for points in one quadrant.")
        np.testing.assert_array_equal(max_point, expected_max_point, "Max point incorrect for points in one quadrant.")

    def test_with_negative_and_positive_coordinates(self):
        points = np.array([[-1, -2, -3], [1, 2, 3], [-4, 5, -6], [7, -8, 9]])
        expected_min_point = np.array([-4, -8, -6])
        expected_max_point = np.array([7, 5, 9])
        min_point, max_point = compute_bounding_box(points)
        np.testing.assert_array_equal(min_point, expected_min_point,
                                      "Min point incorrect for mixed negative and positive coordinates.")
        np.testing.assert_array_equal(max_point, expected_max_point,
                                      "Max point incorrect for mixed negative and positive coordinates.")

    def test_with_decimal_values(self):
        points = np.array([[0.5, 0.7, -0.2], [1.5, 2.3, 2.1], [-1.1, -2.2, -3.3]])
        expected_min_point = np.array([-1.1, -2.2, -3.3])
        expected_max_point = np.array([1.5, 2.3, 2.1])
        min_point, max_point = compute_bounding_box(points)
        np.testing.assert_array_almost_equal(min_point, expected_min_point, decimal=5,
                                             err_msg="Min point incorrect for decimal values.")
        np.testing.assert_array_almost_equal(max_point, expected_max_point, decimal=5,
                                             err_msg="Max point incorrect for decimal values.")


if __name__ == '__main__':
    unittest.main()
