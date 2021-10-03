from datatype_check import check_char, check_complex_float, check_complex_int, check_float, check_int, check_string

class Table:

    def __init__(self, key, fields=None):
        self._key = key
        if fields is None:
            self._fields = dict()
        else:
            self._fields = fields
    
    def get_fields(self):
        return self._fields

    def get_key(self):
        return self._key

    def add_field(self, field_name, field_type, field_value):
        
        if field_name in self._fields.keys():
            raise BaseException(f"Field with name {field_name} already exist.")

        if field_type == 'int':
            value = check_int(field_value)
        elif field_type == 'string':
        	value = check_string(field_value)
        elif field_type == 'char':
            value = check_char(field_value)
        elif field_type == 'real':
            value = check_float(field_value)
        elif field_type == 'complexInt':   
        	value = check_complex_int(field_value)
        elif field_type == 'complexReal':
        	value = check_complex_float(field_value)
        else:
            raise TypeError(f"Datatype {field_type} is not supported.")

        self._fields[field_name] = value

    def change_field(self, field_name, field_type, field_value):
        
        if field_name not in self._fields.keys():
            raise BaseException(f"No such field with name {field_name}")

        if field_type == 'int':
            value = check_int(field_value)
        elif field_type == 'string':
            value = check_string(field_value)
        elif field_type == 'char':
            value = check_char(field_value)
        elif field_type == 'real':
            value = check_float(field_value)
        elif field_type == 'complexInt':
            value = check_complex_int(field_value)
        elif field_type == 'complexReal':
            value = check_complex_float(field_value)
        else:
            raise TypeError(f"Datatype {field_type} is not supported.")
        
        self._fields[field_name] = value

    def delete_field(self, field_name):
        if field_name not in self._fields.keys():
            raise BaseException(f"No such field with name {field_name}")
        else:
            self._fields.pop(field_name)

    def show(self):
        for key in self._fields.keys():
            print(f"{key} - {self._fields[key]}")
