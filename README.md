# Connect_To_DB

## connection.py
an class for connect in a database (mysql)
This class are made to be inherited, and in this new class config all CRUD methods 

        Instance Parameters:
            - db_config_path (str): path where the archive will be created
            - database (str): the database you will connect
            - host (str): host where your database is
            - port (str): the connection port
            - user (str): user you will log in db
            - passwd (str): your user password to log in db 

        Atributes:
            - conx (MySQLConnection): connection with mysql
            - cursor (CursorBase): cursor for execute sql commands
            - table (str): table for apply sql commands
            - tables (list): list with all tables on DB

## config archive
an module with functions to create the configs archives
