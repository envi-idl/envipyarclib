"""

"""
import unittest
import arcpy
from numpy import pi

class TestDataTypeDouble(unittest.TestCase):
    """Tests the double task datatype"""
    config = None

    @classmethod
    def setUpClass(cls):
        """Class setup creates a toolbox file wrapper"""
        cls.config.setup_toolbox('IDL', 'qa_idltaskengine_datatype_double',
                                 'test_datatype_double')

    @classmethod
    def tearDownClass(cls):
        pass

    def test_datatype_double_positive(self):
        """Tests the double datatype with a positive value."""
        input = pi
        result = arcpy.QA_IDLTaskEngine_DataType_Double_TEST(input)

        self.assertAlmostEqual(float(result.getOutput(0)), input, places=14)

    def test_datatype_double_negative(self):
        """Tests the double datatype with a negative value."""
        input = -pi
        result = arcpy.QA_IDLTaskEngine_DataType_Double_TEST(input)

        self.assertAlmostEqual(float(result.getOutput(0)), input, places=14)