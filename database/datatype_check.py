
def check_int(val):
    try:
        val = int(val.replace(" ", ""))
        return val
    except Exception:
        raise ValueError("Wrong data for INT datatype.")

def check_float(val):
    try:
        val = float(val.replace(" ", ""))
        return val
    except Exception:
        raise ValueError("Wrong data for INT datatype.")

def check_char(val):
    if len(val) == 1:
            return val
    else:
        raise ValueError("Wrong data for CHAR datatype.")

def check_string(val):
    return val

def check_complex_int(val):
    try:
        val = complex(val.replace(" ", ""))
        if val.real == int(val.real):
            return str(val)
        else:
            raise ValueError("Wrong data for COMPLEX INT datatype.")
    except Exception:
        raise ValueError("Wrong data for COMPLEX INT datatype.")

def check_complex_float(val):
    try:
        val = complex(val.replace(" ", ""))
        if val.real != int(val.real):
            return str(val)
        else:
            raise ValueError("Wrong data for COMPLEX INT datatype.")
    except Exception:
        raise ValueError("Wrong data for COMPLEX INT datatype.")