import unittest
from modules.move_mesh import move_mesh


class TestMoveMesh(unittest.TestCase):
    def setUp(self):
        # Define a basic mesh for testing
        self.mesh = [[0, 0, 0], [1, 1, 1], [2, 2, 2]]

    def test_move_mesh_positive_values(self):
        # Move the mesh by positive values
        x, y, z = 1, 2, 3
        expected_result = [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
        result = move_mesh(self.mesh, x, y, z)
        self.assertEqual(result, expected_result, "Mesh not moved correctly by positive values.")

    def test_move_mesh_negative_values(self):
        # Move the mesh by negative values
        x, y, z = -1, -2, -3
        expected_result = [[-1, -2, -3], [0, -1, -2], [1, 0, -1]]
        result = move_mesh(self.mesh, x, y, z)
        self.assertEqual(result, expected_result, "Mesh not moved correctly by negative values.")

    def test_move_mesh_zero_values(self):
        # Move the mesh by zero values, expecting the same mesh
        x, y, z = 0, 0, 0
        expected_result = self.mesh
        result = move_mesh(self.mesh, x, y, z)
        self.assertEqual(result, expected_result, "Mesh not remained static on moving by zero values.")

    def test_move_mesh_empty_mesh(self):
        # Attempt to move an empty mesh
        x, y, z = 1, 2, 3
        expected_result = []  # Expecting an empty mesh in return
        result = move_mesh([], x, y, z)
        self.assertEqual(result, expected_result, "Empty mesh handling failed.")

    def test_move_mesh_large_values(self):
        # Move the mesh by large values
        x, y, z = 1000, 2000, 3000
        expected_result = [[1000, 2000, 3000], [1001, 2001, 3001], [1002, 2002, 3002]]
        result = move_mesh(self.mesh, x, y, z)
        self.assertEqual(result, expected_result, "Mesh not moved correctly by large values.")

    def test_move_mesh_mixed_values(self):
        # Move the mesh by mixed positive and negative values
        x, y, z = -100, 200, -300
        expected_result = [[-100, 200, -300], [-99, 201, -299], [-98, 202, -298]]
        result = move_mesh(self.mesh, x, y, z)
        self.assertEqual(result, expected_result, "Mesh not moved correctly by mixed values.")

    def test_move_mesh_floating_point_values(self):
        # Move the mesh by floating point values
        x, y, z = 0.5, 1.5, -0.5
        expected_result = [[0.5, 1.5, -0.5], [1.5, 2.5, 0.5], [2.5, 3.5, 1.5]]
        result = move_mesh(self.mesh, x, y, z)
        self.assertEqual(result, expected_result, "Mesh not moved correctly by floating point values.")

    def test_move_mesh_very_small_values(self):
        # Move the mesh by very small values
        x, y, z = 0.001, 0.002, 0.003
        expected_result = [[0.001, 0.002, 0.003], [1.001, 1.002, 1.003], [2.001, 2.002, 2.003]]
        result = move_mesh(self.mesh, x, y, z)
        self.assertEqual(result, expected_result, "Mesh not moved correctly by very small values.")


if __name__ == '__main__':
    unittest.main()
