'''
class -> ConnectToDb:
Esta classe devolve um objeto conectado no banco com os seguintes atributos

- conx = Conexão com o Banco
- cursor = Cursor
- table = Tabela atual
- tables = Todas as tabelas no Banco
'''
import mysql.connector as mysql
from dotenv import load_dotenv
from os import getenv
from config_archive import config_archive

class ConnectToDb:
    def __init__(self, database:str, table: str = '', host: str = '127.0.0.1',user:str = 'root', port:str = '3306',password: str= '', auto_commit: bool = True, db_config_path:str = 'env') -> None:
        '''
        Atributes:
        - conx
        - cursor
        - table
        - tables
        '''
        # Carregando o arquivo plano de configuração
        config_archive(db_config_path, host, user, port, password, database)
        load_dotenv(db_config_path)
        
        # Conectando ao banco
        try:
            self.__conx = mysql.connect(
                host=getenv('HOST'),
                port=int(getenv('PORT')),
                user=getenv('USER_DB'),
                passwd=getenv('PASSWD'),
                db=getenv('DB')
            )
            print('Conectado ao banco com sucesso!')
        except Exception as err:
            raise err('Houve um erro ao se conectar no banco!')
        else:
            self.__cursor = self.conx.cursor()
            self.__table = table
            self.__tables: list = self.tables_on_bd()
            self.__auto_commit: bool = auto_commit
        
    def tables_on_bd(self): 
        self.cursor.execute('SHOW TABLES')
        all_tables = [table[0] for table in self.cursor.fetchall()]
        return all_tables
    
    # Metodos na conexão
    def close(self):
        self.conx.close()

    def commit(self):
        self.conx.commit()
    
    def auto_commiting(self):
        if self.auto_commit:
            self.commit()

    def rollback(self):
        self.conx.rollback()

    # Metodos de verificação
    def __testing_table(self, table):
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

    @property
    def auto_commit(self):
        return self.__auto_commit
    
    # Setters
    @table.setter
    def table(self, table):
        self.__testing_table(table)
        print('Tabela alterada com sucesso!')
        self.__table = table


if __name__ == '__main__':
    print(__doc__)
