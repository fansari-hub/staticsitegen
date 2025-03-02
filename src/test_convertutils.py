import unittest
from convertutils import *


class TestConvertUtils(unittest.TestCase):
    def test_paragraphs(self):
        md = """This is **bolded** paragraph
text in a p
tag here

# This is another paragraph with _italic_ text and `code` here"""
        node = markdown_to_html_node(md)
        result = node.to_html()
        expected = "<div><p>This is <b>bolded</b> paragraph<BR/>text in a p<BR/>tag here</p><h1> This is another paragraph with <i>italic</i> text and <code>code</code> here</h1></div>"
        self.assertEqual(result, expected)

    def test_codeblock(self):
        md = """``` This is text that _should_ remain 
the **same** even with inline stuff ```"""
        node = markdown_to_html_node(md)
        result = node.to_html()
        expected = """<div><pre><code> This is text that _should_ remain 
the **same** even with inline stuff </code></pre></div>"""
        self.assertEqual(result, expected)

    def test_heading1(self):
        md = """### This is a Level3 Header
with multi-line"""
        node = markdown_to_html_node(md)
        result = node.to_html()
        expected = "<div><h3> This is a Level3 Header<BR/>with multi-line</h3></div>"
        self.assertEqual(result, expected)        

    def test_heading6(self):
        md = """###### This is a Level6 Header
with multi-line"""
        node = markdown_to_html_node(md)
        result = node.to_html()
        expected = "<div><h6> This is a Level6 Header<BR/>with multi-line</h6></div>"
        self.assertEqual(result, expected)

    def test_quoteblock(self):
        md = """>Quote Line 1 
>Quote Line 2
>Quote Line 3"""
        node = markdown_to_html_node(md)
        result = node.to_html()
        expected = "<div><blockquote>Quote Line 1 <BR/>Quote Line 2<BR/>Quote Line 3</blockquote></div>"
        self.assertEqual(result, expected)        

    def test_ul(self):
        md = """- Line A 
- Line B
- Line C"""
        node = markdown_to_html_node(md)
        result = node.to_html()
        expected = "<div><ul><li>Line A </li><li>Line B</li><li>Line C</li></ul></div>"
        self.assertEqual(result, expected)        

    def test_ol(self):
        md = """1.Line 1 
2.Line 2
3.Line 3"""
        node = markdown_to_html_node(md)
        result = node.to_html()
        expected = "<div><ol><li>Line 1 </li><li>Line 2</li><li>Line 3</li></ol></div>"
        self.assertEqual(result, expected)                        