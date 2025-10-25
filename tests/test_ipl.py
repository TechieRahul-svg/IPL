"""
Unit tests for IPL analysis package.

Note: Run tests after installing the package in editable mode:
    pip install -e .
"""

import unittest

try:
    from ipl import __version__
    from ipl.data_loader import load_match_data, load_player_data
    IMPORTS_AVAILABLE = True
except ImportError:
    IMPORTS_AVAILABLE = False


class TestIPLPackage(unittest.TestCase):
    """Test cases for IPL package."""
    
    @unittest.skipUnless(IMPORTS_AVAILABLE, "Package not installed")
    def test_version(self):
        """Test package version."""
        self.assertEqual(__version__, '0.1.0')


class TestDataLoader(unittest.TestCase):
    """Test cases for data loader module."""
    
    @unittest.skipUnless(IMPORTS_AVAILABLE, "Package not installed")
    def test_load_match_data_file_not_found(self):
        """Test that load_match_data raises FileNotFoundError for non-existent file."""
        with self.assertRaises(FileNotFoundError):
            load_match_data('/non/existent/file.csv')
    
    @unittest.skipUnless(IMPORTS_AVAILABLE, "Package not installed")
    def test_load_player_data_file_not_found(self):
        """Test that load_player_data raises FileNotFoundError for non-existent file."""
        with self.assertRaises(FileNotFoundError):
            load_player_data('/non/existent/file.csv')


if __name__ == '__main__':
    unittest.main()
