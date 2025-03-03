from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    
    def __init__(self, tag=None, children=None, prop=None):
        self.tag = tag
        self.children=children
        self.prop = prop
        super().__init__(tag=self.tag, value=None, children=self.children, prop=self.prop)
    
    def to_html(self):
        if self.tag == None:
            raise ValueError("All Parent nodes must have a tag")
        if self.children == None:
            raise ValueError("All Parent nodes must have children")

        # Start with the opening tag of the parent
        if self.prop != None:
            prop_string = self.props_to_html()
            html_content = f"<{self.tag}{prop_string}>"
        else:
            html_content = f"<{self.tag}>"
        
        
        
        # Iterate over the children (recursive)
        for child in self.children:
            html_content += child.to_html()

        # Add the closing tag of the parent
        html_content += f"</{self.tag}>"

        return html_content