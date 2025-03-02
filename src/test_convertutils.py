import unittest
from convertutils import *
import pprint


class TestConvertUtils(unittest.TestCase):
    def test_paragraphs(self):
        md = """This is **bolded** paragraph
text in a p
tag here

# This is another paragraph with _italic_ text and `code` here"""
        node = markdown_to_html_node(md)

    def test_codeblock(self):
        md = """``` This is text that _should_ remain 
the **same** even with inline stuff ```"""
        node = markdown_to_html_node(md)

    def test_heading1(self):
        md = """### This is a Level3 Header
with multi-line"""
        node = markdown_to_html_node(md)

    def test_heading6(self):
        md = """###### This is a Level6 Header
with multi-line"""
        node = markdown_to_html_node(md)

    def test_quoteblock(self):
        md = """>Quote Line 1 
>Quote Line 2
>Quote Line 3"""
        node = markdown_to_html_node(md)

    def test_ul(self):
        md = """- Line A 
- Line B
- Line C"""
        node = markdown_to_html_node(md)

    def test_ol(self):
        md = """1.Line 1 
2.Line 2
3.Line 3"""
        node = markdown_to_html_node(md)                