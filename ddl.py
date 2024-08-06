from connector import set_connection
import pandas as pd

with open('C:/Users/LENOVO/Documents/finanalitycproject/queries/ddl.sql') as f:
    query=f.read()

with set_connection() as dc:
    dc.execute(query)
    tables = [ 
        'Countrys',
        'Players',
        'Teams', 
        'League', 
        'Player_Attributes', 
        'Team_Attributes',
        'Match'
        ]
    
    for table in tables:                
        df = pd.read_csv(f'C:/Users/LENOVO/Documents/finanalitycproject/source/{table}.csv')
        dc.query(f"""
            insert into {table}
            select *
            from df
        """)