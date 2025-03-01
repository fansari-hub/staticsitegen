class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, prop=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.prop = prop
    def to_html(self):
        raise NotImplementedError()
    def props_to_html(self):
        prop_list = self.prop.items()
        string = ""
        for prop in prop_list:
            string += " " + prop[0] + "="
            string += '"' + prop[1] + '"'
        return string
    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, prop={self.prop})"
    