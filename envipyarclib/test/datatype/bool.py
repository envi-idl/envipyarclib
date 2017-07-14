
import unittest
import arcpy

class TestDataTypeBool(unittest.TestCase):
    """Tests the the envi data type bool"""
    config = None

    @classmethod
    def setUpClass(cls):
        """Class setup creates a toolbox file wrapper"""
        cls.tbx_file = cls.config.setup_toolbox('ENVI', 'QA_ENVITaskEngine_DataType_Bool',
                                                        'test_datatype_bool')

    @classmethod
    def tearDownClass(cls):
        pass

    def test_datatype_bool_true(self):
        """Tests the bool datatype."""
        input_bool = True
        result = arcpy.QA_ENVITaskEngine_DataType_Bool_TEST(input_bool)
        self.assertEqual(result.getOutput(0), 'true')

    def test_datatype_bool_false(self):
        """Tests the bool datatype."""
        input_bool = False
        result = arcpy.QA_ENVITaskEngine_DataType_Bool_TEST(input_bool)
        self.assertEqual(result.getOutput(0), 'false')
