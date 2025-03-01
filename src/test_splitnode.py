import unittest

from splitnode import split_nodes_delimiter
from textnode import *

class TestSpliteNode(unittest.TestCase):
    def test_single_delimiter_middle(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = \
            [TextNode("This is text with a ", TextType.TEXT), 
            TextNode("code block", TextType.CODE), 
            TextNode(" word", TextType.TEXT)]
        self.assertEqual(result, expected)

    def test_single_delimiter_start(self):
        node = TextNode("`This is text with a code block` word", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = \
            [TextNode("This is text with a code block", TextType.CODE), 
            TextNode(" word", TextType.TEXT)]
        self.assertEqual(result, expected)

    def test_single_delimiter_end(self):
        node = TextNode("This is text `with a code block word`", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = \
            [TextNode("This is text ", TextType.TEXT), 
            TextNode("with a code block word", TextType.CODE)]
        self.assertEqual(result, expected)

    def test_multi_delimiter_middle(self):
        node = TextNode("This is `text` with a `code block` word", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = \
            [TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.CODE),
            TextNode(" with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT)]
        self.assertEqual(result, expected)
    
    def test_multi_delimiter_start_middle(self):
        node = TextNode("`This is text` with a `code block` word", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = \
            [TextNode("This is text", TextType.CODE),
            TextNode(" with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT)]
        self.assertEqual(result, expected)

    def test_multi_delimiter_start_end(self):
        node = TextNode("`This is text` with a `code block word`", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = \
            [TextNode("This is text", TextType.CODE),
            TextNode(" with a ", TextType.TEXT),
            TextNode("code block word", TextType.CODE)]
        self.assertEqual(result, expected)

    def test_multi_delimiter_middle_end(self):
        node = TextNode("This is `text` with a `code block word`", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = \
            [TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.CODE),
            TextNode(" with a ", TextType.TEXT),
            TextNode("code block word", TextType.CODE),]
        self.assertEqual(result, expected)

    def test_multi_delimiter_consecutive(self):
        node = TextNode("`This is text`` with a ``code block word`", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = \
            [TextNode("This is text", TextType.CODE),
            TextNode(" with a ", TextType.CODE),
            TextNode("code block word", TextType.CODE),]
        self.assertEqual(result, expected)        
        
    def test_no_delimiters(self):
        node = TextNode("This is text with a code block word", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = \
            [TextNode("This is text with a code block word", TextType.TEXT)]
        self.assertEqual(result, expected)        
        
    def test_no_close_delimiter(self):
        node = TextNode("This is `text with a code block word", TextType.TEXT)
        with self.assertRaises(Exception) as context:
            split_nodes_delimiter([node], "`", TextType.CODE)
            self.assertEqual(str(context.exception), "Invalid Markdown: No closing delimiter found.")



if __name__ == "__main__":
    unittest.main()
