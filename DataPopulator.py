import sqlite3

conn = sqlite3.connect('test.db')
print("Opened database successfully")
# Populates database with values
conn.execute("INSERT INTO WORDS (ABRV,Long) \
      VALUES ('OMG','Oh my god')")
conn.execute("INSERT INTO WORDS (ABRV,Long) \
      VALUES ('BRB','be right back')")
conn.execute("INSERT INTO WORDS (ABRV,Long) \
      VALUES ('TTYL','Talk to you later')")
conn.execute("INSERT INTO WORDS (ABRV,Long) \
      VALUES ('OMW','On my way')")
conn.execute("INSERT INTO WORDS (ABRV,Long) \
      VALUES ('CH','Caleb Haley')")

# Commit changes
conn.commit()
print("Records created successfully")
# Close connection
conn.close()
