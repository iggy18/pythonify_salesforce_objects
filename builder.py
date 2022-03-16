class Builder:

    def __init__(self, name, fields):
        self.name = name
        self.fields = fields
        self.fields_strings = []
        self.indent = "    "
        self.code_lines = []
        self.build()
        
    def get_peram_strings(self):
        for field, value in self.fields.items():
            field = "{}={}".format(field, value)
            self.fields_strings.append(field)
    
    def declair_class(self):
        declairation = 'class {}:\n\n'.format(self.name)
        self.code_lines.append(declairation)

    def init_line(self):
        perams = (", ").join(self.fields_strings)
        func = '{}def __init__(self, {}):\n'.format(self.indent, perams)
        self.code_lines.append(func)

    def get_attrs(self):
        d = self.indent
        for field in self.fields:
            ater = "{}{}self.{} = {}\n".format(d, d, field, field)
            self.code_lines.append(ater)

    def END(self):
        self.code_lines.append("\n")
        self.code_lines.append("\n")

    
    def build(self):
        self.declair_class()
        self.get_peram_strings()
        self.init_line()
        self.get_attrs()
        self.END()
        
    def results(self):
        return self.code_lines
    
class SobjectModel:
    
    def __init__(self, name, fields):
        self.name = name
        self.fields = fields
        self.fields_strings = []
        self.indent = "    "
        self.code_lines = []
        self.build()
        
    def get_peram_strings(self):
        for field, value in self.fields.items():
            field = "{}={}".format(field, None)
            self.fields_strings.append(field)
    
    def model_field_types(self, salesforce_type):
        if salesforce_type == 'string':
            return 'CharField'
    
    def declair_class(self):
        declairation = 'class {}:\n\n'.format(self.name)
        self.code_lines.append(declairation)

    def init_line(self):
        perams = (", ").join(self.fields_strings)
        func = '{}def __init__(self, {}):\n'.format(self.indent, perams)
        self.code_lines.append(func)

    def get_attrs(self):
        d = self.indent
        for field in self.fields:
            ater = "modles.{} = {}\n".format(d, d, field, field)
            self.code_lines.append(ater)

    def END(self):
        self.code_lines.append("\n")
        self.code_lines.append("\n")

    
    def build(self):
        self.declair_class()
        self.get_peram_strings()
        self.init_line()
        self.get_attrs()
        self.END()
        
    def results(self):
        return self.code_lines