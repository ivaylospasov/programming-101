import unittest

from reduce_file_path import reduce_file_path


class ReducePathTest(unittest.TestCase):

    def test_if_the_path_has_double_points_in_it(self):
        self.assertEqual("/home/radorado/tasks", reduce_file_path("/home//radorado/code/../tasks/"))

    def test_if_the_path_has_point_in_it(self):
        self.assertEqual("/home/radorado/tasks", reduce_file_path("/home/./radorado/tasks"))

    def test_if_the_path_has_double_slash_in_it(self):
        self.assertEqual("/home/radorado/tasks", reduce_file_path("/home//radorado//tasks"))

    def test_removal_the_last_slash(self):
        self.assertEqual("/home/radorado/tasks", reduce_file_path("/home/radorado/tasks/"))


if __name__ == '__main__':
    unittest.main()
