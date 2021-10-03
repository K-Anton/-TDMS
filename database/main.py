from database_class import Database

def console_print():
    name =input("Enter name of db >>")
    db = Database(name)
    while True:
        switch = int(input("Choose action:\n1-add table\n2-change table\n"+
        "3-delete table\n4-multiplication of 2 tables\n5-show database\n"+
        "6-drop database\n7-save to json\n8-load from json\n10-exit\n>> "))
        
        if switch == 1:
            db.add_table()
        elif switch == 2:
            key = input("Enter key of table which you want to change >> ")
            operation_type = int(input("Enter operation type(1-add field,"+
            " 2-delete_field, 3-change_field) >> "))
            
            if operation_type == 1:
                db.add_field_to_table(key, input("Field name >>"), 
                input("Field type(int, string, char, real, complexInt, complexReal) >> "), 
                input("Enter value >> "))
            elif operation_type == 2:
                db.delete_field_from_table(key, input("Enter field name >> "))
            elif operation_type == 3:
                db.change_field_in_table(key, input("Enter field name >> "), 
                input("Field type(int, string, char, real, complexInt, complexReal) >> "),
                input("Enter field value >> "))
        elif switch == 3:
            key = input("Enter key of table which you want to change >> ")
            db.delete_table(key)
        elif switch == 4:
            key1 = input("Enter key of first table >> ")
            key2 = input("Enter key of second table >> ")
            print(db.multplication_of_two_tables(key1, key2))
        elif switch == 5:
            db.show()
        elif switch == 6:
            db.drop()
        elif switch == 7:
            db.save()
        elif switch == 8:
            db.load("db")
        elif switch == 10:
            break
        else:
            break

console_print()