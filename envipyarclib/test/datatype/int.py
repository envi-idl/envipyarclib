"""

"""
import unittest
import arcpy
from numpy import pi


class TestDataTypeInt(unittest.TestCase):
    """Tests the int task datatype"""

    config = None

    @classmethod
    def setUpClass(cls):
        """Class setup creates a toolbox file wrapper"""
        cls.config.setup_toolbox('IDL', 'qa_idltaskengine_datatype_int',
                                 'test_datatype_int')
        cls.config.setup_toolbox('ENVI', 'qa_envitaskengine_datatype_int',
                                 'test_datatype_int_choicelist')

    @classmethod
    def tearDownClass(cls):
        pass

    def test_datatype_int_max(self):
        """Tests the int datatype maximum value."""
        input = 32767
        result = arcpy.QA_IDLTaskEngine_DataType_Int_TEST(input)

        self.assertEqual(int(result.getOutput(0)), input)

    def test_datatype_int_default(self):
        """Tests the int datatype with a default."""
        result = arcpy.QA_IDLTaskEngine_DataType_Int_TEST()

        self.assertEqual(int(result.getOutput(0)), 42)

    def test_datatype_int_choicelist(self):
        """Tests the int datatype with a choicelist."""
        input = 5
        result = arcpy.QA_ENVITaskEngine_DataType_Int_TEST()

        self.assertEqual(int(result.getOutput(0)), input)

    def test_datatype_int_min(self):
        """Tests the int datatype minimum value."""
        input = -32768
        result = arcpy.QA_IDLTaskEngine_DataType_Int_TEST(input)

        self.assertEqual(int(result.getOutput(0)), int(input))

    def test_datatype_int_demote(self):
        """Tests the int datatype with a floating point value."""
        input = pi
        result = arcpy.QA_IDLTaskEngine_DataType_Int_TEST(input)

        self.assertAlmostEqual(int(result.getOutput(0)), int(input))