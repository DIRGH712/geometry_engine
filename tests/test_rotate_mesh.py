import unittest
import numpy as np
from modules.rotate_mesh import rotate_mesh


class TestRotateMesh(unittest.TestCase):
    def setUp(self):
        # A simple cube mesh for testing rotations
        self.mesh = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1], [-1, 0, 0], [0, -1, 0], [0, 0, -1]])

    def test_rotate_mesh_90_degrees_x_axis(self):
        angle = 90
        axis = 'X'
        expected_mesh = np.array([
            [1, 0, 0], [0, 0, -1], [0, 1, 0],
            [-1, 0, 0], [0, 0, 1], [0, -1, 0]
        ])
        rotated_mesh = rotate_mesh(self.mesh, angle, axis)
        np.testing.assert_almost_equal(rotated_mesh, expected_mesh.tolist(), decimal=2)

    def test_rotate_mesh_90_degrees_y_axis(self):
        angle = 90
        axis = 'Y'
        expected_mesh = np.array(
            [[0., 0., 1.], [0., 1., 0.], [-1., 0., 0.], [0., 0., -1.], [0., -1., 0.], [1., 0., 0.]])
        rotated_mesh = rotate_mesh(self.mesh, angle, axis)
        np.testing.assert_almost_equal(rotated_mesh, expected_mesh.tolist(), decimal=2)

    def test_rotate_mesh_90_degrees_z_axis(self):
        angle = 90
        axis = 'Z'
        expected_mesh = np.array(
            [[0., -1., 0.], [1., 0., 0.], [0., 0., 1.], [0., 1., 0.], [-1., 0., 0.], [0., 0., -1.]])
        rotated_mesh = rotate_mesh(self.mesh, angle, axis)
        np.testing.assert_almost_equal(rotated_mesh, expected_mesh.tolist(), decimal=2)

    def test_rotate_mesh_180_degrees_x_axis(self):
        angle = 180
        axis = 'X'
        expected_mesh = np.array([
            [1, 0, 0], [0, -1, 0], [0, 0, -1],
            [-1, 0, 0], [0, 1, 0], [0, 0, 1]
        ])
        rotated_mesh = rotate_mesh(self.mesh, angle, axis)
        np.testing.assert_almost_equal(rotated_mesh, expected_mesh.tolist(), decimal=2)

    def test_rotate_mesh_270_degrees_y_axis(self):
        angle = 270  # Equivalent to -90 degrees
        axis = 'Y'
        expected_mesh = np.array([
            [0, 0, -1], [0, 1, 0], [1, 0, 0],
            [0, 0, 1], [0, -1, 0], [-1, 0, 0]
        ])
        rotated_mesh = rotate_mesh(self.mesh, angle, axis)
        np.testing.assert_almost_equal(rotated_mesh, expected_mesh.tolist(), decimal=2)

    def test_rotate_mesh_invalid_angle(self):
        angle = "90"  # Angle should be an integer or float, not string
        axis = 'Z'
        with self.assertRaises(TypeError):
            rotate_mesh(self.mesh, angle, axis)

    def test_rotate_mesh_non_standard_axis(self):
        angle = 90  # Rotate Mesh with Non-Standard Axis (Should Fail)
        axis = 'non_standard'
        with self.assertRaises(ValueError):
            rotate_mesh(self.mesh, angle, axis)

    def test_rotate_mesh_invalid_axis(self):
        angle = 90
        axis = 'invalid_axis'
        with self.assertRaises(ValueError):
            rotate_mesh(self.mesh, angle, axis)


if __name__ == '__main__':
    unittest.main()
