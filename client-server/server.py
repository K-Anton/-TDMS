import socket
from database_class import Database

server = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)

server.bind(
    ("127.0.0.1", 1234)
)
while True:
    server.listen()
    print("Server is listening.")

    user_socket, address = server.accept()

    user_socket.send("You are connected to the server.\nEnter name of database: ".encode("utf-8"))
    db_name = user_socket.recv(2048).decode("utf-8")

    db = Database(db_name)

    while True:

        user_socket.send("Choose action:\n1-add table\n2-change table\n".encode("utf-8")+
        "3-delete table\n4-multiplication of 2 tables\n5-show database\n".encode("utf-8")+
        "6-drop database\n7-save to json\n8-load from json\n10-exit\n:".encode("utf-8"))
    
        switch = user_socket.recv(2048).decode("utf-8")

        if switch == "1":
            db.add_table()

        elif switch == "2":
            user_socket.send("Enter key of table which you want to change >> ".encode("utf-8"))
            key = user_socket.recv(2048).decode("utf-8")
            user_socket.send("Enter operation type(1-add field,".encode("utf-8")+
            " 2-delete_field, 3-change_field) >> ".encode("utf-8"))
            operation_type = user_socket.recv(2048).decode("utf-8")
            
            if operation_type == "1":
                user_socket.send("Field name >>".encode("utf-8"))
                field_name = user_socket.recv(2048).decode("utf-8")
                user_socket.send("Field type(int, string, char, real, complexInt, complexReal) >> ".encode("utf-8"))
                field_type = user_socket.recv(2048).decode("utf-8")
                user_socket.send("Enter value >> ".encode("utf-8"))
                field_value = user_socket.recv(2048).decode("utf-8")
                db.add_field_to_table(key, field_name, field_type, field_value)
                
            elif operation_type == "2":
                user_socket.send("Field name >>".encode("utf-8"))
                field_name = user_socket.recv(2048).decode("utf-8")
                db.delete_field_from_table(key, field_name)

            elif operation_type == "3":
                user_socket.send("Field name >>".encode("utf-8"))
                field_name = user_socket.recv(2048).decode("utf-8")
                user_socket.send("Field type(int, string, char, real, complexInt, complexReal) >> ".encode("utf-8"))
                field_type = user_socket.recv(2048).decode("utf-8")
                user_socket.send("Enter value >> ".encode("utf-8"))
                field_value = user_socket.recv(2048).decode("utf-8")
                db.change_field_in_table(key, field_name, field_type, field_value)

        elif switch == "3":
            user_socket.send("Enter key of table which you want to delete >> ".encode("utf-8"))
            key = user_socket.recv(2048).decode("utf-8")
            db.delete_table(key)

        elif switch == "4":
            user_socket.send("Enter key of first table >> ".encode("utf-8"))
            key1 = user_socket.recv(2048).decode("utf-8")
            user_socket.send("Enter key of second table >> ".encode("utf-8"))
            key2 = user_socket.recv(2048).decode("utf-8")
            print(db.multplication_of_two_tables(key1, key2))

        elif switch == "5":
            db.show()
        elif switch == "6":
            db.drop()
        elif switch == "7":
            db.save()
        elif switch == "8":
            db.load()
        elif switch == "10":
            break
        else:
            break