import sqlite3

class Connection():
    '''
    Database class to initilize connection and use it with context
    '''
    def __init__(self):
        self.connection = sqlite3.connect('database.db')
        self.cursor = None
    
    def __enter__(self):
        self.cursor = self.connection.cursor()
        return self.cursor
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_val is not None:
            self.connection.rollback()
        else:
            self.cursor.close()
            self.connection.commit()
            
def fetch(query,fetch_type:str='many', with_cols:bool=False):
    '''
    :param query: string format query 
    :param fetch_type: fetch number of rows: valid entries many, one and all. default one
    :param with_cols: bool flag to get columns from cursor
    '''
    try:
        with Connection() as cursor:
            cursor.execute(query)
            if with_cols:
                cols = [i[0] for i in cursor.description]
            if fetch_type=='many':
                return cursor.fetchmany(10), cols if 'cols' in locals() else None
            if fetch_type=='all':
                return cursor.fetchall(), cols if 'cols' in locals() else None
            if fetch_type=='one':
                return cursor.fetchone(), cols if 'cols' in locals() else None

    except Exception as err:
        print(err)
        
def execute(query:str,values:tuple=None):
    '''
    Function to execute single value with query
    :param query: string query to be executed 
    :param values: values if any to be passed with query 
    '''
    with Connection() as cursor:
        if values is not None:
            cursor.execute(query,values)
        else:
            cursor.execute(query)
    return True
    
def executemany(query:str,values:tuple):
    '''
    Function to execute many values to db
    :param query: string query to be executed 
    :param values: values if any to be passed with query 
    '''
    with Connection() as cursor:
        cursor.executemany(query,values)
    return True