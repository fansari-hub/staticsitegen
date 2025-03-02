import unittest
from blockutils import markdown_to_blocks, block_to_block_type, BlockType


class TestBlockUtils(unittest.TestCase):
        def test_markdown_to_blocks_happypath(self):
                md =  """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
""" 

                result = markdown_to_blocks(md)
                expected = \
                        ["This is **bolded** paragraph",
                        "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                        "- This is a list\n- with items"]
                self.assertEqual(result, expected)

        def test_markdown_to_blocks_happypath_emptyblocks(self):
        
                md =  """
This is **bolded** paragraph


This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line



- This is a list
- with items
""" 

                result = markdown_to_blocks(md)
                expected = \
                        ["This is **bolded** paragraph",
                        "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                        "- This is a list\n- with items"]
                self.assertEqual(result, expected)     

        def test_block_to_block_type_heading(self):
               md = "### THIS IS A NICE HEADING"
               result = block_to_block_type(md)
               expected = BlockType.HEADING
               self.assertEqual(result, expected)
               
        def test_block_to_block_type_code(self):
               md = """``` THIS IS A NICE 
BLOCK OF PYTHONIC CODE CODE ```"""
               result = block_to_block_type(md)
               expected = BlockType.CODE_BLOCK
               self.assertEqual(result, expected)
        
        def test_block_to_block_type_quote(self):
               md = """>This is a quote
>I like Quotes
>No more Quotes"""
               result = block_to_block_type(md)
               expected = BlockType.QUOTE_BLOCK
               self.assertEqual(result, expected)   

        def test_block_to_block_type_UL(self):
               md = """- This is a unordered
- List
- And more List!"""
               result = block_to_block_type(md)
               expected = BlockType.UL
               self.assertEqual(result, expected)                   

        def test_block_to_block_type_OL(self):
               md = """1.This is an ordred
2.List
3.And more List!"""
               result = block_to_block_type(md)
               expected = BlockType.OL
               self.assertEqual(result, expected)

        def test_block_to_block_type_P(self):
               md = """
This is just a random
paragraph text block.
"""
               result = block_to_block_type(md)
               expected = BlockType.P
               self.assertEqual(result, expected)                   



if __name__ == "__main__":
    unittest.main()
