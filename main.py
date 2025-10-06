import sqlite3
from tabulate import tabulate
from datetime import datetime, timedelta

# Tabulate used for 'pretty' outputs
# Datetime used for inputing date and time into new flights in correct format

class DBOperations:

  def __init__(self):
    try:
      self.create_tables()
    except Exception as e:
      print(e)
    finally:
      self.conn.close()

  def get_connection(self):
    self.conn = sqlite3.connect("FlightManagment.db") # Creates/Connects DB with name FlightManagment
    self.cur = self.conn.cursor() # Creates cursor to interact with DB

  def create_tables(self):
    try:
      self.get_connection()
      self.read_sql_file('/workspaces/FlightManagement/Operations/createTables.sql') # Creates empty table with all rules
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

  def reset_db(self): # Drops all tables and recreates them with no data
    try:
      self.drop_all()
      self.create_tables()
    except Exception as e:
      print(e)
    finally:
      self.conn.close()

  def insert_test_data(self,amount): # Adds data to tables to interact with
    if amount == "all":
      tables = ['locations','aircraftTypeRating','aircraftModel','plane','pilot','flights']
    elif amount == "base":
      tables = ['locations','aircraftTypeRating','aircraftModel','plane','pilot'] # Option to not insert any flights data
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

  def view_all(self): # Neat view of all flights in database
    try:
      self.get_connection()
      self.read_sql_file('/workspaces/FlightManagement/ViewsAndQuerys/viewAllFlights.sql')
      self.conn.commit()
      self.cur.execute(open("/workspaces/FlightManagement/ViewsAndQuerys/viewNiceData.sql").read())
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

  def search_data(self):
    try:
      while True:
        print("\n Search Options:")
        print("**********")
        print(" 1. Flight No")
        print(" 2. Departure Airport")
        print(" 3. Destination")
        print(" 4. Plane")
        print(" 5. All FLight Details - From Flight No") 
        print(" 6. Exit\n")
        __search_menu = int(input("Enter your choice: "))
        if __search_menu == 1:
          self.search_flight('FlightNo','normal')
        elif __search_menu == 2:
          self.search_flight('DeptartureAirport','normal')
        elif __search_menu == 3:
          self.search_flight('Destination','normal')
        elif __search_menu == 4:
          self.search_flight('Plane','normal')
        elif __search_menu == 5:
          self.search_flight('FlightNo','full')
        elif __search_menu == 6:
          break
        else:
          print("Invalid Choice")
    except Exception as e:
      print(e)

  def search_flight(self,choice,detail):
    try:
      self.get_connection()
      self.read_sql_file('/workspaces/FlightManagement/ViewsAndQuerys/viewAllFlights.sql')
      self.conn.commit()
    except Exception as e:
      print(e)
    base_query = open("/workspaces/FlightManagement/ViewsAndQuerys/viewNiceData.sql").read()[:-1] # Query that is edited to find selected flights
    if choice == 'FlightNo':
      flightNo = str(input("Enter FlightNo: "))
      if detail == 'normal':
        sql_search = base_query + " WHERE `Flight Number` = '%s'" % flightNo
      elif detail == 'full': # Returns all fields from VIEW
        sql_search = "SELECT *" + base_query[85:] + " WHERE `Flight Number` = '%s'" % flightNo
      else:
        sql_search = None
    elif choice == 'DeptartureAirport':
      Depature = str(input("Enter Depature Airport code, city or name: "))
      sql_search = base_query + " WHERE Departure = '{0}' OR `Origin City` = '{0}' OR `Origin Alt Code` = '{0}' OR `Origin Airport` = '{0}' ".format(Depature)
    elif choice == 'Destination':
      Destination = str(input("Enter Destination Airport code, city or name: "))
      sql_search = base_query + " WHERE Destination = '{0}' OR `Destination City` = '{0}' OR `Destination Alt Code` = '{0}' OR `Destination Airport` = '{0}' ".format(Destination)
    elif choice == 'Plane':
      plane = str(input("Enter Plane Tailnumber or Model: "))
      sql_search = "SELECT Tailnumber, Aircraft," + base_query[6:] + " WHERE Tailnumber = '{0}' OR Aircraft = '{0}'".format(plane)
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

  def create_data(self):
    try:
      while True:
        self.get_connection()
        print("\n Create Options:")
        print("**********")
        print(" 1. Create Flight Record")
        print(" 2. Create Pilot Record")
        print(" 3. Create Plane Record")
        print(" 4. Exit\n")
        __create_menu = int(input("Enter your choice: "))
        if __create_menu == 1:
          newFlight = FlightInfo() # Creates new FlightInfo instance to populate
          newFlight.build_info(self)
          sqlInsert="INSERT INTO 'flights'\
                    ('origin_location_id','destination_location_id','flight_pilot_id','flight_plane_id','departure_time_utc','arrival_time_utc','flight_number')\
                    VALUES\
                    ({},{},{},{},'{}','{}','{}');\
                    ".format(newFlight.flightOrgin, newFlight.flightDestination, newFlight.flightPilot, newFlight.flightPlane, newFlight.departureTime, newFlight.arrivalTime, newFlight.flightNumber)
        elif __create_menu == 2:
          FirstName =str(input("Enter Pilot First Name: "))
          LastName =str(input("Enter Pilot Last Name: "))
          TypeRating =int(input("Enter Type Rating id: "))
          sqlInsert="INSERT INTO pilot (pilot_first_name, pilot_last_name, pilot_type_rating_id) VALUES ('{0}','{1}',{2});".format(FirstName, LastName, TypeRating)
        elif __create_menu == 3:
          while True:
            try:
              Tailnumber =str(input("Enter Tailnumber Sufix: "))
              if len(Tailnumber) >= 5:
                Tailnumber = "G-" + Tailnumber.upper()
                break
              else:
                print("Tail nuumber suffix should be 5 characters or less")
            except Exception as e:
              print(e)
          plane_model =str(input("Enter Plane model: "))
          sqlInsert="INSERT INTO plane (tailnumber, plane_model_id) VALUES ('{0}',{1});".format(Tailnumber, plane_model)
        elif __create_menu == 4:
          break
        else:
          print("Invalid Choice")
        self.cur.execute(sqlInsert)
        self.conn.commit()
    except Exception as e:
      print(e)
    finally:
      self.conn.close()

  def update_data(self): # Finds table_id of record and updates a column
    try:
      tables = ['locations','aircraftTypeRating','aircraftModel','plane','pilot','flights']  
      printableTables = [[table] for table in tables]
      print(tabulate(printableTables, headers=["Tables"], tablefmt="fancy_grid"))
      user_table = str(input("Select table to update a record from: "))
      if(user_table in tables):
        user_id = int(input("Enter id to be updated: "))
        column_id = {
          'locations':'location_id',
          'aircraftTypeRating':'aircraft_type_rating',
          'aircraftModel':'aircraft_model_id',
          'plane':'plane_id',
          'pilot':'pilot_id',
          'flights':'flight_id'
        }
        idQuery = "SELECT {0} FROM {1} WHERE {0} = '{2}';".format(column_id[user_table],user_table, user_id)
        idToBeUpdated = self.get_id_from_table(idQuery)
        if idToBeUpdated:
          self.get_connection()
          self.cur.execute("select * from {0}".format(user_table))
          columns = [description[0] for description in self.cur.description]
          print("\n Column Options:")
          print("**********")
          for column in columns:
            print(column)
          user_column = str(input("Enter column to be updated: "))
          user_new_val = str(input("Enter a new value: "))
          updateQuery = "UPDATE {1} SET {4}={3} WHERE {0} = {2};".format(column_id[user_table],user_table, user_id, user_new_val,user_column)
          print(updateQuery)
          self.cur.execute(updateQuery)
          self.conn.commit()
        else:
          print("Cannot find this record in the database")
      else:
        print("Could not find table")
    except Exception as e:
      print(e)
    finally:
      self.conn.close()

  def delete_data(self): # Finds a record from a table and removes the row
    try:
      tables = ['locations','aircraftTypeRating','aircraftModel','plane','pilot','flights']  
      printableTables = [[table] for table in tables]
      print(tabulate(printableTables, headers=["Tables"], tablefmt="fancy_grid"))
      user_table = str(input("Select table to delete from: "))
      if(user_table in tables):
        user_id = int(input("Enter id to be deleted: "))
        column_id = {
          'locations':'location_id',
          'aircraftTypeRating':'aircraft_type_rating',
          'aircraftModel':'aircraft_model_id',
          'plane':'plane_id',
          'pilot':'pilot_id',
          'flights':'flight_id'
        }
        idQuery = "SELECT {0} FROM {1} WHERE {0} = '{2}';".format(column_id[user_table],user_table, user_id)
        idToBeDeleted = self.get_id_from_table(idQuery)
        if idToBeDeleted:
          deleteQuery = "DELETE FROM {1} WHERE {0} = {2};".format(column_id[user_table],user_table, user_id)
          print(deleteQuery)
          self.get_connection()
          self.cur.execute(deleteQuery)
          self.conn.commit()
        else:
          print("Cannot find this record in the database")
      else:
        print("Could not find table")
    except Exception as e:
      print(e)
    finally:
      self.conn.close()

  def get_id_from_table(self,query): # Function for getting the table_ids of records for use in update and delete functions
    self.get_connection()
    self.cur.execute(query)
    rows = self.cur.fetchone()
    idNumber = str(rows[0])
    return idNumber

  def read_sql_file(self,fileName): # Helper function to run SQL script files
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
    self.passengers_booked = 0
    self.flight_status = 'On Time'
    self.time_delay = "0000"

  def build_info(self, db): # Builds flight info from step by step user input
    self.db = db
    print("Enter Origin")
    self.flightOrgin = self.get_flight_location('Origin')
    print("Enter Destination")
    self.flightDestination = self.get_flight_location('Destination')
    self.flightPlane = self.get_plane()
    typeRatingQueryBase = open("/workspaces/FlightManagement/ViewsAndQuerys/selectTypeRatingFromPlaneID.sql").read()[:-3]
    typeRatingQuery = typeRatingQueryBase + self.flightPlane + "';"
    typeRating = self.db.get_id_from_table(typeRatingQuery) # Passes through type rating of aircraft to be able to selct pilot 
    self.flightPilot = self.get_pilot(typeRating)
    self.departureTime = self.get_departure_time()
    flightDuration = self.get_duration()
    self.arrivalTime = self.departureTime + flightDuration
    self.flightNumber = "FM" + str(int(input("Input Flight Number: FM")))

  def get_flight_location(self,terminal):
    while True:
      try:
        flightLocation =str(input("Enter Airport id or Code: "))
        flightLocationquery = "SELECT location_id FROM locations WHERE icao_code = '{0}' OR iata_code = '{0}' OR location_id = '{0}';".format(flightLocation)
        confirmedLocation = self.db.get_id_from_table(flightLocationquery)
        if confirmedLocation:
          return confirmedLocation
        else:
          print("Not a recognised Location")
      except Exception as e:
        print(e)

  def get_plane(self):
    print("\n Select Plane By:")
    print("**********")
    print(" 1. tailnumber")
    print(" 2. Plane ID")
    print(" 3. Random of Model")
    print(" 4. Random\n")
    __plane_menu = int(input("Enter your choice: "))
    if __plane_menu == 1:
      tailnumber = "G-" + str(input("Enter Plane Tailnumber Suffix: G-"))
      flightPlanequery = "SELECT plane_id FROM plane WHERE tailnumber = '{0}';".format(tailnumber)
      return self.db.get_id_from_table(flightPlanequery)
    elif __plane_menu == 2:
      return str(input("Enter Pilot id: "))
    elif __plane_menu == 3:
      model = str(input("Enter Plane Model: "))
      planequery = "SELECT aircraft_model_id FROM aircraftModel WHERE aircraft_model_name = '{0}';".format(model)
      model_id = self.db.get_id_from_table(planequery)
      flightPlanequery = "SELECT plane_id FROM plane WHERE plane_model_id = '{0}' ORDER BY RANDOM() LIMIT 1;".format(model_id)
      return self.db.get_id_from_table(flightPlanequery)
    elif __plane_menu == 4:
      flightPlanequery = "SELECT plane_id FROM plane ORDER BY RANDOM() LIMIT 1;"
      return self.db.get_id_from_table(flightPlanequery)
    else:
      print("Invalid Choice")
    
  def get_pilot(self,TypeRating):
    print("\n Select Pilot By:")
    print("**********")
    print(" 1. Full Name")
    print(" 2. Pilot ID")
    print(" 3. Random Qualifed\n")
    __pilot_menu = int(input("Enter your choice: "))
    if __pilot_menu == 1:
      FirstName =str(input("Enter Pilot First Name: "))
      LastName =str(input("Enter Pilot Last Name: "))
      flightPilotquery = "SELECT pilot_id FROM pilot WHERE pilot_first_name = '{0}' OR pilot_last_name = '{1}';".format(FirstName,LastName)
      return self.db.get_id_from_table(flightPilotquery)
    elif __pilot_menu == 2:
      return str(input("Enter Pilot id: "))
    elif __pilot_menu == 3:
      flightPilotquery = "SELECT pilot_id FROM pilot WHERE pilot_type_rating_id = '{0}' ORDER BY RANDOM() LIMIT 1;".format(TypeRating)
      return self.db.get_id_from_table(flightPilotquery)
    else:
      print("Invalid Choice")
    
  def get_departure_time(self):
    while True:
        dateTime = input("Enter date and time of flight YYYY-MM-DD HH:MM: ")
        try:
            departure_time = datetime.strptime(dateTime, "%Y-%m-%d %H:%M")
            return departure_time
        except ValueError:
            print("Invalid format use YYYY-MM-DD HH:MM (2025-10-01 14:30)")

  def get_duration(self):
    while True:
        durationTime = input("Enter the time duration of flight HH:MM: ")
        try:
            duration_time = datetime.strptime(durationTime, "%H:%M")
            durationDelta = timedelta(hours=duration_time.hour, minutes=duration_time.minute)
            return durationDelta
        except ValueError:
            print("Invalid format use HH:MM (02:30)")

  def __str__(self):
    return str(
      "Origin: {0}\nDestination: {1}\n".format(self.flightOrgin,self.flightDestination) + \
      "Plane: {0}\nPilot: {1}\n".format(self.flightPlane,self.flightPilot) + \
      "Departing: {0}\n".format(self.departureTime) + \
      "Arriving: {0}\n".format(self.arrivalTime) + \
      "FlightNo: {0}\n".format(self.flightNumber)
    )

while True:
  print("\n Menu:")
  print("**********")
  print(" 1. Reset Database")
  print(" 2. Insert Test Data")
  print(" 3. View all from Flights data")
  print(" 4. Search a flight")
  print(" 5. Insert Base Data (Excluding Flights)")
  print(" 6. Create New Data record") 
  print(" 7. Update data some records")
  print(" 8. Delete data some records")
  print(" 9. Exit\n")

  __choose_menu = int(input("Enter your choice: "))
  db_ops = DBOperations()
  if __choose_menu == 1:
    db_ops.reset_db()
  elif __choose_menu == 2:
    db_ops.insert_test_data('all')
  elif __choose_menu == 3:
    db_ops.view_all()
  elif __choose_menu == 4:
    db_ops.search_data()
  elif __choose_menu == 5:
    db_ops.insert_test_data('base')
  elif __choose_menu == 6:
    db_ops.create_data()
  elif __choose_menu == 7:
    db_ops.update_data()
  elif __choose_menu == 8:
    db_ops.delete_data()
  elif __choose_menu == 9:
    exit(0)
  else:
    print("Invalid Choice")
