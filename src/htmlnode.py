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
        
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        if self.value==None:
            raise ValueError
        if self.tag==None:
            return str(self.value)
        if self.props != None:
            prop_str=""
            for key in self.props:
                prop_str+=f'{key}="{self.props[key]}" '
            if prop_str[-1]==" ":
                prop_str = prop_str[:-1]
            beg_tag=f'<{self.tag} {prop_str}>' 
            end_tag=f'</{self.tag}>'
            return f"{beg_tag}{self.value}{end_tag}"
        beg_tag=f'<{self.tag}>' 
        end_tag=f'</{self.tag}>'
        return beg_tag+self.value+end_tag

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError ("Tag Required for Parent Node")
        if self.children == None:
            raise ValueError ("Children Required for Parent Node")
        par_str=""
        beg_tag=f'<{self.tag}>'
        end_tag=f'</{self.tag}>'
        if self.props != None:
            prop_str=""
            for key in self.props:
                prop_str+=f'{key}="{self.props[key]}" '
            if prop_str[-1]==" ":
                prop_str = prop_str[:-1]
            beg_tag=f'<{self.tag} {prop_str}>'
            return beg_tag
        par_str = par_str + beg_tag
        for child in self.children:
            child_str = ""
            if isinstance(child, LeafNode):
                child_str = LeafNode.to_html(child)
                par_str = par_str + child_str
            else:
                child_str = ParentNode.to_html(child)
                par_str = par_str + child_str
        return par_str + end_tag






