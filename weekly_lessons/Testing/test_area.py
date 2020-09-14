from unittest import TestCase
import area


'''
tests work by making an assertion with data that should pass the test. If the test fails it means that either
either the test logic is flawed or the function is incorrect.
'''
class TestShapeAreas(TestCase):

    def test_triangle_area(self):
        # A triangle with height 4 and base 5 should have area 10
        # argument: expected, actual value generated from call.
        self.assertEqual(10, area.triangle_area(4, 5))


    def test_triangle_base_height_zero(self):
        self.assertEqual(0, area.triangle_area(0, 5))
        self.assertEqual(0, area.triangle_area(5, 0))
        self.assertEqual(0, area.triangle_area(0, 0))


    # test names must be different or the last test will overwrite any test with the same name
    def test_triangle_area_floating_point(self):
        #assertAlmostEqual for long floating point values
        self.assertAlmostEqual(17.79875, area.triangle_area(7.25,4.91))


    def test_triangle_negative_height_base_raises_value_exception(self):

        with self.assertRaises(ValueError):
            area.triangle_area(9, -10)

        with self.assertRaises(ValueError):
            area.triangle_area(-9, 10)

        with self.assertRaises(ValueError):
            area.triangle_area(-9, -10)