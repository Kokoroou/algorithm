import unittest

from find_hamiltonian_path import find_hamiltonian_path


class TestHamiltonianPath(unittest.TestCase):
    def test_hamiltonian_path_exists(self):
        graph = [
            [0, 1, 0, 1],
            [1, 0, 1, 0],
            [0, 1, 0, 1],
            [1, 0, 1, 0]
        ]
        expected = [0, 1, 2, 3]
        result = find_hamiltonian_path(graph)
        self.assertEqual(result, expected)

    def test_hamiltonian_path_does_not_exist(self):
        graph = [
            [0, 0, 0, 1],
            [0, 0, 1, 0],
            [0, 1, 0, 0],
            [1, 0, 0, 0]
        ]
        expected = None
        result = find_hamiltonian_path(graph)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
