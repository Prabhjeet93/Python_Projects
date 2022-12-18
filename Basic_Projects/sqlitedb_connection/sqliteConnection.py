import sqlite3

# This creates our donors table and populates it with data.
def create():
    # open the database and obtain a connection
    with sqlite3.connect("donors.db") as conn:
        # obtain a cursor from the connection
        c = conn.cursor()

        # delete all rows from the table named "donors"
        c.execute("DROP TABLE donors")
        
        # create the donors table
        c.execute('''CREATE TABLE donors
                     (id integer primary key,
                      name text,
                      address text,
                      amount real)''')
        
        # insert data into the donors table
        c.execute('''INSERT INTO donors
                     (name, address, amount) values
                     ("Bob Barker", "1720 PIR Lane", 14.75),
                     ("Ruby Tuesday", "21 4th St.", 25.00),
                     ("Virginia Hope", "3 East Creek Rd.", 217.14)''')

# The report() function queries all rows from the database and prints out all donor information in a formatted table.
def report():
    # open the database and obtain a connection
    with sqlite3.connect("donors.db") as conn:
        # obtain a cursor from the connection
        c = conn.cursor()
        
        # retrieve all rows from the donors table and order them by amount in descending order
        c.execute('''SELECT * FROM donors ORDER BY amount DESC''')
        
        # print out the donor information in a formatted table
        print("{:<20} {:<20} {:<30} {:<10}".format("id", "Name", "Address", "Amount"))
        print("-"*80)
        for row in c:
            print("{:<20} {:<20} {:<30} {:<10}".format(*row))

# The run() function calls create() and report().
def run():
    create()
    report()

if __name__ == "__main__":
    run()
