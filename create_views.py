from connector import set_connection

with open('queries/v_matches.sql', 'r') as f:
    with set_connection() as dc:
        dc.execute(f.read())