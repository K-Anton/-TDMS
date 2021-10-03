
class Datatype:
    def __init__(self, val):
        # val is always an str object
        self._value = val
    def get_value(self):
        return self._value
    def set_value(self, val):
        self._value = val
    
class Char(Datatype):
    def __init__(self, val):
        if len(val) == 1:
            return super().__init__(val)
        else:
            raise ValueError("Wrong data for CHAR datatype.")
    
    def set_value(self, val):
        if len(val) == 1:
            return super().set_value(val)
        else:
            raise ValueError("Wrong data for CHAR datatype.")

class Int(Datatype):
    def __init__(self, val):
        try:
            val = int(val)
            return super().__init__(val)
        except Exception:
            raise ValueError("Wrong data for INT datatype.")

    def set_value(self, val):
        try:
            val = int(val)
            return super().set_value(val)
        except Exception:
            raise ValueError("Wrong data for INT datatype.")

class String(Datatype):
    def __init__(self, val):
        super().__init__(val)

class Real(Datatype):

    def __init__(self, val):
        try:
            val = float(val)
            return super().__init__(val)
        except Exception:
            raise ValueError("Wrong data for REAL datatype.")

    def set_value(self, val):
        try:
            val = float(val)
            return super().set_value(val)
        except Exception:
            raise ValueError("Wrong data for REAL datatype.")

class ComplexInt(Datatype):
    def __init__(self, val):
        try:
            val = complex(val)
            if val.real == int(val.real):
                return super().__init__(val)
            else:
                raise ValueError("Wrong data for COMPLEX INT datatype.")
        except Exception:
            raise ValueError("Wrong data for COMPLEX INT datatype.")

    def set_value(self, val):
        try:
            val = complex(val)
            if val.real == int(val.real):
                return super().__init__(val)
            else:
                raise ValueError("Wrong data for COMPLEX INT datatype.")
        except Exception:
            raise ValueError("Wrong data for COMPLEX INT datatype.")

class ComplexReal(Datatype):
    
    def __init__(self, val):
        try:
            val = complex(val)
            if val.real != int(val.real):
                return super().__init__(val)
            else:
                raise ValueError("Wrong data for COMPLEX REAL datatype.")
        except Exception:
            raise ValueError("Wrong data for COMPLEX REAL datatype.")

    def set_value(self, val):
        try:
            val = complex(val)
            if val.real != int(val.real):
                return super().__init__(val)
            else:
                raise ValueError("Wrong data for COMPLEX REAL datatype.")
        except Exception:
            raise ValueError("Wrong data for COMPLEX REAL datatype.")

