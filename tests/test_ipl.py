"""
Unit tests for IPL analysis package.
"""

import unittest
import sys
import os

# Add src to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from ipl import __version__


class TestIPLPackage(unittest.TestCase):
    """Test cases for IPL package."""
    
    def test_version(self):
        """Test package version."""
        self.assertEqual(__version__, '0.1.0')


class TestDataLoader(unittest.TestCase):
    """Test cases for data loader module."""
    
    def test_load_match_data_file_not_found(self):
        """Test that load_match_data raises FileNotFoundError for non-existent file."""
        try:
            from ipl.data_loader import load_match_data
            with self.assertRaises(FileNotFoundError):
                load_match_data('/non/existent/file.csv')
        except ImportError:
            self.skipTest("pandas not installed")
    
    def test_load_player_data_file_not_found(self):
        """Test that load_player_data raises FileNotFoundError for non-existent file."""
        try:
            from ipl.data_loader import load_player_data
            with self.assertRaises(FileNotFoundError):
                load_player_data('/non/existent/file.csv')
        except ImportError:
            self.skipTest("pandas not installed")


if __name__ == '__main__':
    unittest.main()
