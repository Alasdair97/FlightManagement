import sqlite3
from tabulate import tabulate

# Define DBOperation class to manage all data into the database.
# Give a name of your choice to the database


class DBOperations:
  sql_create_table = "create table TableName"
  sql_insert = ""
  sql_alter_data = ""
  sql_update_data = ""
  sql_delete_data = ""
  sql_drop_table = ""

  def __init__(self):
    try:
      self.create_tables()
    except Exception as e:
      print(e)
    finally:
      self.conn.close()

  def get_connection(self):
    self.conn = sqlite3.connect("FlightManagment.db")
    self.cur = self.conn.cursor()

  def create_tables(self):
    try:
      self.get_connection()
      self.read_sql_file('/workspaces/FlightManagement/Operations/createTables.sql')
      self.conn.commit()
    except Exception as e:
      print(e)
    finally:
      self.conn.close()

  def drop_all(self):
    try:
      self.get_connection()
      self.read_sql_file('/workspaces/FlightManagement/Operations/drop_all.sql')
    except Exception as e:
      print(e)
    finally:
      self.conn.close()

  def reset_db(self):
    try:
      self.drop_all()
      self.create_tables()
    except Exception as e:
      print(e)
    finally:
      self.conn.close()

  def insert_base_data(self):
    tables = ['locations','aircraftTypeRating','aircraftModel','plane','pilot','flights']
    try:
      self.get_connection()
      for table in tables:
        try:
          self.read_sql_file('/workspaces/FlightManagement/BaseDataLoad/insertInto_%s.sql' % table)
          self.conn.commit()
          print('Base %s Inserted' % table)
        except Exception as e:
          print(e)
    except Exception as e:
      print(e)
    finally:
      self.conn.close()

  def insert_data(self):
    try:
      self.get_connection()
      flight = FlightInfo()
      flight.set_flight_id(int(input("Enter FlightID: ")))

      self.cur.execute(self.sql_insert, tuple(str(flight).split("\n")))

      self.conn.commit()
      print("Inserted data successfully")
    except Exception as e:
      print(e)
    finally:
      self.conn.close()

  def view_all(self):
    try:
      self.get_connection()
      self.read_sql_file('/workspaces/FlightManagement/ViewsAndQuerys/viewAllFlights.sql')
      self.conn.commit()
      cursor = self.conn.cursor()
      cursor.execute(open("/workspaces/FlightManagement/ViewsAndQuerys/viewNiceData.sql").read())
      rows = cursor.fetchall()
      col_names = [description[0] for description in cursor.description]
      print(tabulate(rows, headers=col_names, tablefmt="psql"))

    except Exception as e:
      print(e)
    finally:
      self.conn.close()

  def search_data(self):
    try:
      while True:
        print("\n Search Options:")
        print("**********")
        print(" 1. Flight No")
        print(" 2. Departure Airport")
        print(" 3. Destination")
        print(" 4. Plane")
        print(" 5. Exit\n")
        __search_menu = int(input("Enter your choice: "))
        if __search_menu == 1:
          self.search_flight('FlightNo')
        elif __search_menu == 2:
          self.search_flight('DeptartureAirport')
        elif __choose_menu == 3:
          self.search_flight('Destination')
        elif __choose_menu == 4:
          self.search_flight('Plane')
        elif __choose_menu == 5:
          exit(0)
        else:
          print("Invalid Choice")
    except Exception as e:
      print(e)

  def search_flight(self,choice):
    base_query = open("/workspaces/FlightManagement/ViewsAndQuerys/viewNiceData.sql").read()[:-1]
    if choice == 'FlightNo':
      flightNo = str(input("Enter FlightNo: "))
      sql_search = base_query + " WHERE `Flight Number` = '%s'" % flightNo
    elif choice == 'DeptartureAirport':
      Depature = str(input("Enter Depature Airport code, city or name: "))
      sql_search = base_query + " WHERE Departure = '{0}' OR `Origin City` = '{0}' OR `Origin Alt Code` = '{0}' OR `Origin Airport` = '{0}' ".format(Depature)
    elif choice == 'Destination':
      sql_search = base_query + " WHERE `Flight Number` = '%s'" % flightNo
    elif choice == 'Plane':
      sql_search = "SELECT Tailnumber, Aircraft," + base_query[6:] + " WHERE `Flight Number` = '%s'" % flightNo
    else:
          print("Invalid Choice")
    try:
      self.get_connection()
      self.cur.execute(sql_search)
      rows = self.cur.fetchall()
      if rows:
        col_names = [description[0] for description in self.cur.description]
        print(tabulate(rows, headers=col_names, tablefmt="psql"))
      else:
        print("No Flight(s) found")

    except Exception as e:
      print(e)
    finally:
      self.conn.close()
  
  def update_data(self):
    try:
      self.get_connection()

      # Update statement

      if result.rowcount != 0:
        print(str(result.rowcount) + "Row(s) affected.")
      else:
        print("Cannot find this record in the database")

    except Exception as e:
      print(e)
    finally:
      self.conn.close()


# Define Delete_data method to delete data from the table. The user will need to input the flight id to delete the corrosponding record.

  def delete_data(self):
    try:
      self.get_connection()

      if result.rowcount != 0:
        print(str(result.rowcount) + "Row(s) affected.")
      else:
        print("Cannot find this record in the database")

    except Exception as e:
      print(e)
    finally:
      self.conn.close()

# Helper function to run SQL script files

  def read_sql_file(self,fileName):
    fileObject = open(fileName, 'r')
    sqlFile = fileObject.read()
    fileObject.close()
    sqlCommands = sqlFile.split(';')

    for command in sqlCommands:
      try:
        self.cur.execute(command)
      except Exception as e:
        print(e)


class FlightInfo:

  def __init__(self):
    self.flightID = 0
    self.flightOrigin = ''
    self.flightDestination = ''
    self.status = ''

  def set_flight_id(self, flightID):
    self.flightID = flightID

  def set_flight_origin(self, flightOrigin):
    self.flight_origin = flightOrigin

  def set_flight_destination(self, flightDestination):
    self.flight_destination = flightDestination

  def set_status(self, status):
    self.status = status

  def get_flight_id(self):
    return self.flightID

  def get_flight_origin(self):
    return self.flightOrigin

  def get_flight_destination(self):
    return self.flightDestination

  def get_status(self):
    return self.status

  def __str__(self):
    return str(
      self.flightID
    ) + "\n" + self.flightOrigin + "\n" + self.flightDestination + "\n" + str(
      self.status)


# The main function will parse arguments.
# These argument will be definded by the users on the console.
# The user will select a choice from the menu to interact with the database.

while True:
  print("\n Menu:")
  print("**********")
  print(" 1. Reset Database")
  print(" 2. Insert Base Data")
  print(" 3. View all from Flights data")
  print(" 4. Search a flight")
  print(" 5. Update data some records")
  print(" 6. Delete data some records")
  print(" 7. Exit\n")

  __choose_menu = int(input("Enter your choice: "))
  db_ops = DBOperations()
  if __choose_menu == 1:
    db_ops.reset_db()
  elif __choose_menu == 2:
    db_ops.insert_base_data()
  elif __choose_menu == 3:
    db_ops.view_all()
  elif __choose_menu == 4:
    db_ops.search_data()
  elif __choose_menu == 5:
    db_ops.update_data()
  elif __choose_menu == 6:
    db_ops.delete_data()
  elif __choose_menu == 7:
    db_ops.reset_db() #TODO for Testing remove before submission
    exit(0)
  else:
    print("Invalid Choice")
