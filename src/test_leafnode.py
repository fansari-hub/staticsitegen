import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode(tag="p", value="Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_b(self):
        node = LeafNode(tag="b", value="Hello, world!")
        self.assertEqual(node.to_html(), "<b>Hello, world!</b>")

    def test_leaf_to_html_h1(self):
        node = LeafNode(tag="h1", value="Hello, world!")
        self.assertEqual(node.to_html(), "<h1>Hello, world!</h1>")

