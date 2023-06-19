
import mysql.connector


try:

  mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="64*18eVheS0pQ",
    database="erha_db"
  )

  mycursor = mydb.cursor()

  sql = " DELETE FROM transact_in WHERE date_time < SUBDATE(NOW(), INTERVAL 12 MONTH);"
  mycursor.execute(sql)

  mydb.commit()
  print(mycursor.rowcount, "record(s) deleted")


  mycursor = mydb.cursor()

  sql = " DELETE FROM transact_mv WHERE date_time < SUBDATE(NOW(), INTERVAL 12 MONTH);"
  mycursor.execute(sql)

  mydb.commit()
  print(mycursor.rowcount, "record(s) deleted")


  mycursor = mydb.cursor()

  sql = " DELETE FROM transact_out WHERE date_time < SUBDATE(NOW(), INTERVAL 12 MONTH);"
  mycursor.execute(sql)

  mydb.commit()
  print(mycursor.rowcount, "record(s) deleted")


  mycursor = mydb.cursor()

  sql = " DELETE FROM transact_wroff WHERE date_time < SUBDATE(NOW(), INTERVAL 12 MONTH);"
  mycursor.execute(sql)

  mydb.commit()
  print(mycursor.rowcount, "record(s) deleted")

  mycursor = mydb.cursor()

  sql = "DELETE e1 FROM dubl e1 INNER JOIN dubl e2 WHERE  e1.id < e2.id and e1.name = e2.name and e1.email = e2.email;"
  mycursor.execute(sql)

  mydb.commit()
  print(mycursor.rowcount, "record(s) deleted")



finally:
  mycursor.close()