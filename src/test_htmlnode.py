import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_a(self):
        node = HTMLNode(tag="a", value="my website", prop={"href" : "https://www.google.com", "target" : "_blank"} )
        result = node.props_to_html()
        expected_result = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(result, expected_result)

    def test_props_to_html_b(self):
        node = HTMLNode(tag="a", value="my website", prop={} )
        result = node.props_to_html()
        expected_result = ''
        self.assertEqual(result, expected_result)

    def test_props_to_html_c(self):
        node = HTMLNode(tag="a", value="my website", prop={"href" : "https://www.google.com", "target" : "_blank", "style" : "red"}  )
        result = node.props_to_html()
        expected_result = ' href="https://www.google.com" target="_blank" style="red"'
        self.assertEqual(result, expected_result)




if __name__ == "__main__":
    unittest.main()