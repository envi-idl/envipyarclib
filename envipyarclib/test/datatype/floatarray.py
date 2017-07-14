"""
"""
import unittest

import arcpy

class TestDataTypeFloatArray(unittest.TestCase):
    """Tests the float array task datatype"""

    config = None

    @classmethod
    def setUpClass(cls):
        cls.config.setup_toolbox('IDL', 'qa_idltaskengine_datatype_floatarray',
                                 'test_datatype_floatarray')

    @classmethod
    def tearDownClass(cls):
        pass

    def test_datatype_floatarray_one_dimension(self):
        """Verify a one dimensional array of floats returns a semicolon separated string list."""
        input = [0, 5.64777, -254.3]
        expect_dims = [len(input)]
        result = arcpy.QA_IDLTaskEngine_DataType_FloatArray_TEST(input, expect_dims)
        print(result)
        resultArr = result.getOutput(0).split(';')
        for index in range(len(input)):
            self.assertAlmostEqual(input[index],float(resultArr[index]),places=5)