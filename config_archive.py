from os import path, system
import platform

def config_archive(db_config_path:str = 'env', host: str = '127.0.0.1',user:str = 'root', port:str = '3306',passwd: str= '', database:str = ''):
    # Se o arquivo não existir

    if platform.system() == 'Windows':
        DIR_SEP = '\\'
    else:
        DIR_SEP = '/'
    if not path.isfile(db_config_path):
        pastas = db_config_path.split(DIR_SEP)[:-1]
        directory = '.'
        for pasta in pastas:
            directory += DIR_SEP + pasta
            system(f'mkdir {directory}') # Criando diretorios

        amb_variables = [
            f'HOST={host}', 
            f'USER_DB={user}', 
            f'PORT={port}', 
            f'PASSWD={passwd}', 
            f'DB={database}'
        ]

        # Inserindo variaveis de ambiente no arquivo de configuração
        with open(db_config_path, 'w', encoding='utf-8') as file:
            for variable in amb_variables:
                file.write(variable + '\n')