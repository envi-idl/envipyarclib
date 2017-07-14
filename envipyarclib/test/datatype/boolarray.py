import unittest

import arcpy


class TestDataTypeBoolArray(unittest.TestCase):
    """Tests the bool array task datatype"""
    config = None

    @classmethod
    def setUpClass(cls):
        cls.config.setup_toolbox('ENVI', 'qa_envitaskengine_datatype_boolarray',
                                 'test_datatype_boolarray')

    @classmethod
    def tearDownClass(cls):
        pass

    def test_boolarray_one_dimension(self):
        """Verify a one dimensional array of bools returns a semicolon separated string list."""
        input = [True, True, False, True]
        expect_dims = [len(input)]
        result = arcpy.QA_ENVITaskEngine_DataType_BoolArray_TEST(input, expect_dims)
        self.assertEqual(str(result.getOutput(0)), 'true;true;false;true')