# test_singularitynet.py
"""
Tests for SingularityNet module.
"""

import unittest
from singularitynet import SingularityNet

class TestSingularityNet(unittest.TestCase):
    """Test cases for SingularityNet class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = SingularityNet()
        self.assertIsInstance(instance, SingularityNet)
        
    def test_run_method(self):
        """Test the run method."""
        instance = SingularityNet()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
