"""
Unit tests for IPL analysis package.
"""

import unittest
from src.ipl import __version__


class TestIPLPackage(unittest.TestCase):
    """Test cases for IPL package."""
    
    def test_version(self):
        """Test package version."""
        self.assertEqual(__version__, '0.1.0')


if __name__ == '__main__':
    unittest.main()
