import unittest

from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_multi_children(self):
        child_node_a = LeafNode("span", "span_content")
        child_node_b = LeafNode("p", "paragraph_content")
        child_node_c = LeafNode("button", "submit")
        parent_node = ParentNode("div", [child_node_a, child_node_b, child_node_c])
        self.assertEqual(parent_node.to_html(), "<div><span>span_content</span><p>paragraph_content</p><button>submit</button></div>")
    
    def test_to_html_with_multi_children_and_normal_text(self):
        child_node_a = LeafNode("b", "Bold Text")
        child_node_b = LeafNode(None, "Normal Text")
        child_node_c = LeafNode("i", "Italic Text")
        child_node_d = LeafNode(None, "More Normal Text")
        parent_node = ParentNode("p", [child_node_a, child_node_b, child_node_c, child_node_d])
        self.assertEqual(parent_node.to_html(), "<p><b>Bold Text</b>Normal Text<i>Italic Text</i>More Normal Text</p>")

        
    def test_to_html_with_multi_grandchildren(self):
        child_node_a = LeafNode("span", "span_content")
        grandchild_node_b1 = LeafNode("i", "italic_text")
        grandchild_node_b2 = LeafNode("b", "bold_text")
        child_node_b = ParentNode("p", [grandchild_node_b1, grandchild_node_b2])
        child_node_c = LeafNode("button", "submit")
        parent_node = ParentNode("div", [child_node_a, child_node_b, child_node_c])
        self.assertEqual(parent_node.to_html(), "<div><span>span_content</span><p><i>italic_text</i><b>bold_text</b></p><button>submit</button></div>")

    def test_to_html_without_children(self):
        with self.assertRaises(ValueError) as context:
            parent_node = ParentNode("div", children=None)
            parent_node.to_html()
            self.assertEqual(str(context.exception), "All Parent nodes must have children")
