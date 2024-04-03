import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError


# value to connect server
server="{sql server name}"
database="{database name}"
 
def extract(): 
    engine = create_engine('mssql+pyodbc://@' + '{server name}' + '/' + '{database name}' + '?trusted_connection=yes&driver={driver name}')

# test connection
    try:
        engine.connect() 
        print("success")
    except SQLAlchemyError as err:
        print("error", err.__cause__) 
        return
# read sql
    with engine.connect() as conn:
        df = pd.read_sql_query('{SQL query}', conn)
        return df

postgres_server = '{postgres server name}'
postgres_id = '{postgres id}'
postgres_pw = '{postgres pw}'

# load data to postgresql
def load(df, tbl):
    try:
        engine = create_engine(f'postgresql://{postgres_id}:{postgres_pw}@localhost:5432/{postgres database name}')
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

