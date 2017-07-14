"""
"""
import unittest
import arcpy
from numpy import pi


class TestDatatypeFloat(unittest.TestCase):
    """Tests the float task datatype"""
    config = None

    @classmethod
    def setUpClass(cls):
        """Class setup creates a toolbox file wrapper"""
        cls.config.setup_toolbox('IDL', 'qa_idltaskengine_datatype_float',
                                 'test_datatype_float')

    @classmethod
    def tearDownClass(cls):
        pass

    def test_datatype_float_positive(self):
        """Tests the float datatype with a positive value."""
        input = pi
        result = arcpy.QA_IDLTaskEngine_DataType_Float_TEST(input)

        self.assertAlmostEqual(float(result.getOutput(0)), input, places=6)

    def test_datatype_float_negative(self):
        """Tests the float datatype with a negative value."""
        input = -pi
        result = arcpy.QA_IDLTaskEngine_DataType_Float_TEST(input)

        self.assertAlmostEqual(float(result.getOutput(0)), input, places=6)