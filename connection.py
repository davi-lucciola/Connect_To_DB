'''
An class to make connection with db.

class:
    ConnectToDb
'''
import mysql.connector as mysql
from dotenv import load_dotenv
from os import getenv
from config_archive import config_archive

class ConnectToDb:
    def __init__(self, database:str, table: str = '', host: str = '127.0.0.1',user:str = 'root', port:str = '3306',password: str= '', db_config_path:str = 'env') -> None:
        '''
        An class to make connection with db.
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
        '''
        # Creating the plan config archive
        config_archive(database, db_config_path, host, port, user, password)

        # Loading all amb variables
        load_dotenv(db_config_path)
        
        # Connecting to database and MYSQL
        try:
            self.__conx = mysql.connect(
                host=getenv('HOST'),
                port=int(getenv('PORT')),
                user=getenv('USER_DB'),
                passwd=getenv('PASSWD'),
                db=getenv('DB')
            )
            print('Connected to DB successfully!')
        except Exception as err:
            raise err('There was an error connecting to the database!')
        else:
            self.__cursor = self.conx.cursor()
            self.__table = table
            self.__tables: list = self.tables_on_bd()
        
    def tables_on_bd(self) -> list: 
        self.cursor.execute('SHOW TABLES;')
        all_tables = [table[0] for table in self.cursor.fetchall()]
        return all_tables
    
    # Connection methods
    def close(self) -> None:
        self.conx.close()

    def commit(self) -> None:
        self.conx.commit()

    def rollback(self) -> None:
        self.conx.rollback()

    # Verification methods
    def __testing_table(self, table) -> str:
        if (table in self.tables) or (table is None):
            return table
        else:
            raise Exception('This table not exist in BD')
            
    # Getters
    @property
    def conx(self):
        return self.__conx
    
    @property
    def cursor(self):
        return self.__cursor
    
    @property
    def table(self):
        return self.__table

    @property
    def tables(self):
        return self.__tables
    
    # Setters
    @table.setter
    def table(self, table) -> None:
        self.__testing_table(table)
        print('Your table are changed successfully!')
        self.__table = table


if __name__ == '__main__':
    print(__doc__)
