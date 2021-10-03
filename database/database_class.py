from table_class import Table


class Database:
    
    def __init__(self, name):
        self._name = name
        self._next_id = 0
        self._tables = dict()
    
    def get_tables(self):
        return self._tables
    
    def get_name(self):
        return self._name
    
    def get_next_id(self):
        return self._next_id

    def drop(self):
        self._tables.clear()
        self._next_id = 0

    def save(self):
        pass

    def load(self):
        pass

    def add_table(self):
        table = Table(self._next_id)
        self._tables[f"{self._next_id}"] = table
        self._next_id += 1

    def delete_table(self, key):
        if key not in self._tables.keys:
            raise BaseException(f"No such table with key {key}")
        else:
            del self._tables[key]
    
    def change_table(self, key, operation_type):
        if key not in self._tables.keys:
            raise BaseException(f"No such table with key {key}")
        
        if operation_type == "1":
            self.__tables[key].add_field()
            
        elif operation_type == "2":
            self.__tables[key].delete_field()
            
        elif operation_type == "3":
            self.__tables[key].change_field()

        else:
            raise BaseException(f"Wrong operation type {operation_type}")

    def multplication_of_two_tables(self, key1, key2):
        if not key1 in self._tables.keys:
            raise BaseException(f"No such table with key {key1}")
        if not key2 in self._tables.keys:
            raise BaseException(f"No such table with key {key2}")

        res = dict()
        counter = 0
        for i in self._tables[key1].get_fields():
            val1 = str(i.get_name()) + str(i.get_value().get_value())
            for j in self._tables[key2].get_fields():
                val2 = str(j.get_name()) + str(j.get_value().get_value())
                res[f"{counter}"] = val1 + val2
                counter+=1
        
        return res
            
