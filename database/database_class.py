import json
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
        
        db_arr = list()
        db_arr.append(self._next_id)
        for key in self._tables.keys():
            db_arr.append([int(key), self._tables[key].get_fields()])
        
        json_db = json.dumps(db_arr)
        with open(f"{self._name}.json", "w") as f:
            f.write(json_db)

    def load(self, filename):
        with open(f"{self._name}.json", "r") as f:
            obj = json.loads(f.read())
        self._next_id = obj[0]
        obj.pop(0)
        self.drop()
        for i in obj:
            self._tables[f"{i[0]}"] = Table(i[0], i[1])

    def add_table(self):
        self._tables[f"{self._next_id}"] = Table(self._next_id)
        self._next_id += 1

    def delete_table(self, key):
        if key not in self._tables.keys():
            raise BaseException(f"No such table with key {key}")
        else:
            del self._tables[key]
    
    def add_field_to_table(self, key, field_name, field_type, field_value):
        if key not in self._tables.keys():
            raise BaseException(f"No such table with key {key}")
        else:
            self._tables[key].add_field(field_name, field_type, field_value)

    def change_field_in_table(self, key, field_name, field_type, field_value):

        if key not in self._tables.keys():
            raise BaseException(f"No such table with key {key}")
        else:
            self._tables[key].change_field(field_name, field_type, field_value)         

    def delete_field_from_table(self, key, field_name):
        if key not in self._tables.keys():
            raise BaseException(f"No such table with key {key}")
        else:
            self._tables[key].delete_field(field_name)

    def multplication_of_two_tables(self, key1, key2):
        if not key1 in self._tables.keys():
            raise BaseException(f"No such table with key {key1}")
        if not key2 in self._tables.keys():
            raise BaseException(f"No such table with key {key2}")

        res = dict()
        counter = 0
        fields1 = self._tables[key1].get_fields()
        fields2 = self._tables[key2].get_fields()

        for i in fields1.keys():
            val1 = str(i) + " : " + str(fields1[i])
            for j in fields2:
                val2 = str(j) + " : " + str(fields2[j])
                res[f"{counter}"] = val1 + " " + val2
                counter+=1
        
        return res
            
    def show(self):
        print("#"*20)
        print(f"Dabase {self._name}")
        print("#"*20)

        for key in self._tables.keys():
            print("-"*20 +"\n" + f"Table {key}" + "\n" + "-"*20 +"\n")
            self._tables[key].show()
            print("-"*20 +"\n")
        print("#"*20)
        