import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError


# value to connect server
server="LAPTOP-CJG2OK7J\SQLEXPRESS"
database="AdventureWorks2019"
 
def extract(): 
    engine = create_engine('mssql+pyodbc://@' + 'LAPTOP-CJG2OK7J\SQLEXPRESS' + '/' + 'AdventureWorks2019' + '?trusted_connection=yes&driver=SQL+Server+Native+Client+11.0')

# test connection
    try:
        engine.connect() 
        print("success")
    except SQLAlchemyError as err:
        print("error", err.__cause__) 
        return
# read sql
    with engine.connect() as conn:
        df = pd.read_sql_query('SELECT TOP(10) AddressID FROM [AdventureWorks2019].[Person].[Address]', conn)
        return df

postgres_server = 'PostgreSQL 14'
postgres_id = 'postgres'
postgres_pw = 'Galaxy123'

# load data to postgresql
def load(df, tbl):
    try:
        engine = create_engine(f'postgresql://{postgres_id}:{postgres_pw}@localhost:5432/AdventureWorks')
        # save df to postgres
        df.to_sql(f'stg_{tbl}', engine, if_exists='replace', index=False, chunksize=100000)
        # add elapsed time to final print out
        print("Data imported successful")
    except Exception as e:
        print("Data load error: " + str(e))
if __name__ == "__main__":
    df = extract()
    if df is not None:
        load(df,'Address')

