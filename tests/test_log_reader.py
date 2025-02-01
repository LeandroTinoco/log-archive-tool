import unittest
from src.log_reader import read_log_files

class TestLogReader(unittest.TestCase):
    def test_read_log_files(self):
        log_files = read_log_files('tests/logs')
        self.assertGreater(len(log_files), 0, "Should find at least one log file")

if __name__ == '__main__':
    unittest.main()

