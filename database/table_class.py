from datatypes_classes import Int, Char, String, Real, ComplexInt, ComplexReal
from field_class import Field

class Table:

    def __init__(self, key):
        self._key = key
        self._fields = dict()
    
    def get_fields(self):
        return self._fields

    def get_key(self):
        return self._key

    def add_field(self, field_name, field_type, field_value):
        
        if field_name in self._fields.keys:
            raise BaseException(f"Field with name {field_name} already exist.")

        if field_type == 'int':
            value = Int(field_value)
        elif field_type == 'string':
        	value = String(field_value)
        elif field_type == 'char':
            value = Char(field_value)
        elif field_type == 'real':
            value = Real(field_value)
        elif field_type == 'complexInt':   
        	value = ComplexInt(field_value)
        elif field_type == 'complexReal':
        	value = ComplexReal(field_value)
        else:
            raise TypeError(f"Datatype {field_type} is not supported.")

        self._fields[field_name] = Field(field_name, value)

    def change_field(self, old_field_name, new_field_name=None, 
                    field_type=None, field_value=None):
        
        if old_field_name not in self._fields.keys:
            raise BaseException(f"No such field with name {old_field_name}")

        if field_type is not None:
            if field_type == 'int':
                value = Int(field_value)
            elif field_type == 'string':
                value = String(field_value)
            elif field_type == 'char':
                value = Char(field_value)
            elif field_type == 'real':
                value = Real(field_value)
            elif field_type == 'complexInt':
                value = ComplexInt(field_value)
            elif field_type == 'complexReal':
                value = ComplexReal(field_value)
            else:
                raise TypeError(f"Datatype {field_type} is not supported.")
            self._fields[old_field_name].set_value(value)

        if new_field_name is not None:
            if new_field_name in self._fields.keys:
                raise BaseException(f"Field with name {new_field_name} already exist.")
            else:
                self._fields[new_field_name] = self._fields.pop(old_field_name)
                self._fields[new_field_name].set_name(new_field_name)

    def delete_field(self, field_name):
        if field_name not in self._fields.keys:
            raise BaseException(f"No such field with name {field_name}")
        else:
            self._fields.pop(field_name)

