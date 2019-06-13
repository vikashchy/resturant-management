import sqlite3

DBFILE = 'customer.db'


def create_table(dbfile):
    dbconn = sqlite3.connect(database=dbfile)
    sql_create_customer_table = """ CREATE TABLE IF NOT EXISTS customerDetails (
                                    cust_name text NOT NULL,
                                    cust_email text primary key,
                                    cust_address text NOT NULL,
                                    cost_phone integer(10,2)
                                ); """
    dbconn.execute(sql_create_customer_table)
    dbconn.execute('insert into customerDetails values ("Vikash","vikash@123.com","Larica Toenshp",9632211633)')
    dbconn.commit()
    dbconn.close()


def create_conn():
    dbconn = sqlite3.connect(database=DBFILE)
    return dbconn


if __name__ == '__main__':
    try:
        create_table(DBFILE)
    except sqlite3.Error as e:
        print(f'Exception occured when creating database:{e}')
