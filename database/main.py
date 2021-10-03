from database_class import Database

def test():
    name =input("Enter name of db >>")
    db = Database(name)
    while True:
        switch = int(input("Choose action:\n1-add table\n2-change table\n"+
        "3-delete table\n4-multiplication of 2 tables\n5-show database\n"+
        "6-drop database\n10-exit\n>> "))
        if switch == 1:
            db.add_table()
        elif switch == 2:
            key = input("Enter key of table which you want to change >> ")
            operation_type = input("Enter operation type(1-add field,"+
            " 2-delete_field, 3-change_field) >> ")
            db.change_table(key, operation_type)
        elif switch == 3:
            key = input("Enter key of table which you want to change >> ")
            db.delete_table(key)
        elif switch == 4:
            key1 = input("Enter key of first table >> ")
            key2 = input("Enter key of second table >> ")
            db.multiplication_of_two_tables(key1, key2)
        elif switch == 5:
            pass
        elif switch == 6:
            db.drop()
        elif switch == 10:
            break
        else:
            break

test()