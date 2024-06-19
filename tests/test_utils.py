import unittest
from src.utils import read_speeds_from_file

class TestUtils(unittest.TestCase):
    def test_read_speeds_from_file(self):
        test_file_path = 'tests/test_velocita.txt'
        with open(test_file_path, 'w') as f:
            f.write('12,34\n15,42\n')
        
        expected = [12.34, 15.42]
        result = read_speeds_from_file(test_file_path)
        
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
