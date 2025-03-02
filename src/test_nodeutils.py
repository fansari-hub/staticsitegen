import unittest

from nodeutils import split_nodes_delimiter, extract_markdown_links, extract_markdown_images
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

    def test_extract_markdown_images(self):
        result = extract_markdown_images("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)")
        self.assertEqual(result, [('rick roll', 'https://i.imgur.com/aKaOqIh.gif'), ('obi wan', 'https://i.imgur.com/fJRm4Vk.jpeg')])

    def test_extract_markdown_images_one_bad(self):
        result = extract_markdown_images("This is text with a [rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)")
        self.assertEqual(result, [('obi wan', 'https://i.imgur.com/fJRm4Vk.jpeg')])

    def test_extract_markdown_images_all_bad(self):
        result = extract_markdown_images("This is text with a [rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan]https://i.imgur.com/fJRm4Vk.jpeg)")
        self.assertEqual(result, [])    

    def test_extract_markdown_link(self):
        result = extract_markdown_links("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)")
        self.assertEqual(result, [('to boot dev', 'https://www.boot.dev'), ('to youtube', 'https://www.youtube.com/@bootdotdev')])

    def test_extract_markdown_link_one_bad(self):
        result = extract_markdown_links("This is text with a link to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)")
        self.assertEqual(result, [('to youtube', 'https://www.youtube.com/@bootdotdev')])

    def test_extract_markdown_link_all_bad(self):
        result = extract_markdown_links("This is text with a link to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev")
        self.assertEqual(result, [])

if __name__ == "__main__":
    unittest.main()
