import unittest
import pprint

from nodeutils import split_nodes_delimiter, extract_markdown_links, extract_markdown_images, split_nodes_link, split_nodes_image, text_to_textnodes
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

    def test_image_middle_multi(self):
        node = TextNode("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)", TextType.TEXT)
        result = split_nodes_image([node])
        expected = \
            [TextNode("This is text with an ", TextType.TEXT), 
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and another ", TextType.TEXT),
            TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png")]
        self.assertEqual(result, expected)

    def test_image_start_end_multi(self):
        node = TextNode("![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)", TextType.TEXT)
        result = split_nodes_image([node])
        expected = \
            [TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and another ", TextType.TEXT),
            TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png")]
        self.assertEqual(result, expected)

    def test_image_single_full(self):
        node = TextNode("![image](https://i.imgur.com/zjjcJKZ.png)", TextType.TEXT)
        result = split_nodes_image([node])
        expected = \
            [TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png")]
        self.assertEqual(result, expected)

    def test_image_noimage(self):
        node = TextNode("image https://i.imgur.com/zjjcJKZ.png", TextType.TEXT)
        result = split_nodes_image([node])
        expected = \
            [TextNode("image https://i.imgur.com/zjjcJKZ.png", TextType.TEXT)]
        self.assertEqual(result, expected)

    def test_link_middle_multi(self):
        node = TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)", TextType.TEXT)
        result = split_nodes_link([node])
        expected = \
            [TextNode("This is text with a link ", TextType.TEXT), 
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" and ", TextType.TEXT),
            TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev")]
        self.assertEqual(result, expected)

    def test_link_start_end_multi(self):
        node = TextNode("[to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)", TextType.TEXT)
        result = split_nodes_link([node])
        expected = \
            [TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" and ", TextType.TEXT),
            TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev")]
        self.assertEqual(result, expected)

    def test_link_single_full(self):
        node = TextNode("[to boot dev](https://www.boot.dev)", TextType.TEXT)
        result = split_nodes_link([node])
        expected = \
            [TextNode("to boot dev", TextType.LINK, "https://www.boot.dev")]
        self.assertEqual(result, expected)

    def test_link_nolink(self):
        node = TextNode("This is text with a link https://www.boot.dev", TextType.TEXT)
        result = split_nodes_link([node])
        expected = \
            [TextNode("This is text with a link https://www.boot.dev", TextType.TEXT)]
        self.assertEqual(result, expected)

    def test_text_to_textnodes_happypath(self):
        result = text_to_textnodes("This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)")
        expected = \
        [TextNode("This is ", TextType.TEXT, url=None),
        TextNode("text", TextType.BOLD, url=None),
        TextNode(" with an ", TextType.TEXT, url=None),
        TextNode("italic", TextType.ITALIC, url=None),
        TextNode(" word and a ", TextType.TEXT, url=None),
        TextNode("code block", TextType.CODE, url=None),
        TextNode(" and an ", TextType.TEXT, url=None),
        TextNode("obi wan image", TextType.IMAGE, url="https://i.imgur.com/fJRm4Vk.jpeg"),
        TextNode(" and a ", TextType.TEXT, url=None),
        TextNode("link", TextType.LINK, url="https://boot.dev")]
        #pprint.pp(result)
        self.assertEqual(result, expected)

    def test_text_to_textnodes_nomarkdown(self):
        result = text_to_textnodes("This is text with an italic word and a code block and an image at https://i.imgur.com/fJRm4Vk.jpeg and a link at https://boot.dev")
        expected = \
        [TextNode("This is text with an italic word and a code block and an image at https://i.imgur.com/fJRm4Vk.jpeg and a link at https://boot.dev", TextType.TEXT, url=None)]
        #pprint.pp(result)
        self.assertEqual(result, expected)

    def test_text_to_textnodes_emptytext(self):
        result = text_to_textnodes("")
        expected = []
        #pprint.pp(result)
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
