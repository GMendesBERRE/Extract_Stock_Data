from Elements.Element import Element

class InputElement(Element):

    def type(self, text):
        self.web_element.send_keys(text)
        return None
