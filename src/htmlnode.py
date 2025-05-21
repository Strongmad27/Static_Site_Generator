class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        props_str=""
        if self.props:
            for prop in self.props:
                props_str = props_str + f' {prop}="{self.props[prop]}"'
        return props_str
    
    def __repr__(self):
        return f"details on called HTMLNode:\n'TAG': {self.tag}\n'VALUE': {self.value}\n'CHILDREN': {self.children}\n'PROPS': {self.props}\n\nany values not given default to None"
        
