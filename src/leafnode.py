from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, prop=None):
        self.tag = tag
        self.value = value
        self.prop = prop
        super().__init__(tag=self.tag, value=self.value, children=None, prop=self.prop)
    def to_html(self):
        if self.value == None:
            raise ValueError("All leaf nodes must have a value")
        if self.tag == None:
            return self.value
        return f"<{self.tag}>{self.value}</{self.tag}>" 