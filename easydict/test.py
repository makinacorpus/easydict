import unittest
from easydict import EasyDict

class CustomList(list):
    pass

class CustomTuple(tuple):
    pass

class CustomDict(dict):
    pass

class EasyDictTest(unittest.TestCase):
    def test_no_auto_conversion_for_custom_list(self):
        d = EasyDict()
        custom_list = CustomList([1, 2, 3])
        d.custom = custom_list
        self.assertIsInstance(d.custom, CustomList)
        self.assertEqual(d.custom, custom_list)

    def test_no_auto_conversion_for_custom_tuple(self):
        d = EasyDict()
        custom_tuple = CustomTuple((1, 2, 3))
        d.custom = custom_tuple
        self.assertIsInstance(d.custom, CustomTuple)
        self.assertEqual(d.custom, custom_tuple)

    def test_no_auto_conversion_for_custom_dict(self):
        d = EasyDict()
        custom_dict = CustomDict({'key': 'value'})
        d.custom = custom_dict
        self.assertIsInstance(d.custom, CustomDict)
        self.assertEqual(d.custom, custom_dict)

    def test_auto_conversion_for_list(self):
        d = EasyDict()
        d.lst = [{'a': 1}, {'b': 2}]
        self.assertIsInstance(d.lst, list)
        self.assertIsInstance(d.lst[0], EasyDict)
        self.assertIsInstance(d.lst[1], EasyDict)
        self.assertEqual(d.lst[0].a, 1)
        self.assertEqual(d.lst[1].b, 2)
    
    def test_auto_conversion_for_tuple(self):
        d = EasyDict()
        d.tpl = ({'a': 1}, {'b': 2})
        self.assertIsInstance(d.tpl, tuple)
        self.assertIsInstance(d.tpl[0], EasyDict)
        self.assertIsInstance(d.tpl[1], EasyDict)
        self.assertEqual(d.tpl[0].a, 1)
        self.assertEqual(d.tpl[1].b, 2)
    
    def test_auto_conversion_for_dict(self):
        d = EasyDict()
        d.inner_dict = {'a': 1, 'b': 2}
        self.assertIsInstance(d.inner_dict, EasyDict)
        self.assertEqual(d.inner_dict.a, 1)
        self.assertEqual(d.inner_dict.b, 2)
    
    def test_setattr_with_non_dict(self):
        d = EasyDict()
        d.num = 5
        self.assertEqual(d.num, 5)
        d.text = "hello"
        self.assertEqual(d.text, "hello")

if __name__ == "__main__":
    unittest.main()
