from table_class import Table
from database_class import Database
import unittest

class TestDatabaseMethods(unittest.TestCase):
    
    def setUp(self):
        self.db = Database('test_db')
        self.db.add_table()

    def test_add_table(self):
        
        self.db.add_table()
        self.db.add_table()
        self.assertEqual(self.db.get_next_id(), 3)

    def test_add_field_to_table(self):
        
        self.db.add_field_to_table("0", "test", "complexInt", "10 + 3j")
        test_tables = self.db.get_tables()
        fields = test_tables["0"].get_fields()
        self.assertEqual(fields["test"], f"{complex(10+3j)}")

    def test_multiplication(self):
        
        self.db.add_field_to_table("0", "test1", "int", "101")
        self.db.add_table()
        self.db.add_field_to_table("1", "test2", "string", "test string")
        res = self.db.multplication_of_two_tables("0", "1")
        expected = {'0': 'test1 : 101 test2 : test string'}
        self.assertEqual(res, expected)

class TestTableMethods(unittest.TestCase):
    def setUp(self):
        
        self.table = Table(0)
    
    def test_add_field(self):
        
        self.table.add_field("test", "int", "101")
        self.assertEqual(len(self.table.get_fields()), 1)


if __name__ == '__main__':
    unittest.main()