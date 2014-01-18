import unittest

from list import List


class ListTestCase(unittest.TestCase):

    def test_append(self):
        list = List()
        list.append(10)
        self.assertEqual(1, list.size)
        self.assertEqual(10, list.head.content)
        self.assertEqual(10, list.tail.content)

    def test_append_two_items(self):
        list = List()
        list.append(10)
        list.append(5)
        self.assertEqual(2, list.size)
        self.assertEqual(10, list.head.content)
        self.assertEqual(5, list.tail.content)
        self.assertEqual(list.tail, list.head.next)

    def test_append_three_items(self):
        list = List()
        list.append(10)
        list.append(5)
        list.append(15)
        self.assertEqual(3, list.size)
        self.assertEqual(10, list.head.content)
        self.assertEqual(15, list.tail.content)
        self.assertEqual(5, list.head.next.content)

    def test_insert(self):
        list = List()
        list.insert(20)
        list.insert(12)
        self.assertEqual(2, list.size)
        self.assertEqual(12, list.head.content)
        self.assertEqual(20, list.tail.content)
        self.assertEqual(list.tail, list.head.next)

    def test_remove(self):
        list = List()
        list.append(10)
        list.append(5)
        list.append(15)
        list.remove(1)
        self.assertEqual(2, list.size)
        self.assertEqual(10, list.head.content)
        self.assertEqual(15, list.tail.content)
        self.assertEqual(list.tail, list.head.next)

    def test_remove_with_negative_index(self):
        list = List()
        list.append(10)
        with self.assertRaises(ValueError):
            list.remove(-1)

    def test_remove_index_too_big(self):
        list = List()
        list.append(10)
        with self.assertRaises(ValueError):
            list.remove(1)

    def test_remove_first_item(self):
        list = List()
        list.append(10)
        list.append(5)
        list.append(3)
        list.remove(0)
        self.assertEqual(5, list.head.content)

    def test_remove_last_item(self):
        list = List()
        list.append(10)
        list.append(5)
        list.append(3)
        list.remove(2)
        self.assertEqual(5, list.tail.content)

    def test_remove_unique_item(self):
        list = List()
        list.append(10)
        list.remove(0)
        self.assertIsNone(list.head)
        self.assertIsNone(list.tail)

    def test_list_is_iterable(self):
        list = List()
        list.append(10)
        list.append(15)
        list.append(13)
        list.append(12)
        array = []
        map(array.append, list)
        self.assertEqual([10, 15, 13, 12], array)

unittest.main()
