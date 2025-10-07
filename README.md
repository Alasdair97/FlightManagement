# FlightManagement
Coursework for CM500292

## Tables

| Table              | Description                           |
|--------------------|---------------------------------------|
| locations          | Stores airport locations including timezone and country data     |
| aircraftTypeRating | Defines type rating limitations       |
| aircraftModel      | Contains aircraft model information   |
| plane              | Individual plane records              |
| pilot              | Pilot personal and license details    |
| flights            | Flight records                        |


## Use of Options

### 1. Reset Database

This will Drop all tables from the database and create new empty tables

> No Arguments needed

### 2. Insert Test Data

This will insert all test data to all columns

> No Arguments needed

### 3. View all from Flights data

This will display all flights in the database

> No Arguments needed

### 4. Search a flight

Gives Options for searching for existing flights

> Function displays options for arguments that are parsed individually
#### Example

```Example
Enter your choice: 4

 Search Options:
*****************
 1. Flight No
 2. Departure Airport
 3. Destination
 4. Plane
 5. All FLight Details - From Flight No
 6. Exit

Enter your choice: 1
Enter FlightNo: FM5292
+-----------------+-------------+---------------+--------------+------------+-----------+----------+
| Flight Number   | Departure   | Destination   | Schedualed   | Expected   | Arrival   | Status   |
|-----------------+-------------+---------------+--------------+------------+-----------+----------|
| FM5292          | LHR         | HEL           | 12:00        | 12:00      | 14:50     | On Time  |
+-----------------+-------------+---------------+--------------+------------+-----------+----------+
```

### 5. Insert Base Data (Excluding Flights)

Inserts data to all tables except flights incase wanting to work from blank flight table

> No Arguments needed

### 6. Create New Data record 

Allows the creation of flights, pilots and planes to be added to thier respective tables

> Function displays options for arguments that are parsed individually

> Before running this insert at least base data
#### Example
```
Enter your choice: 6

 Create Options:
***************
 1. Create Flight Record
 2. Create Pilot Record
 3. Create Plane Record
 4. Exit

Enter your choice: 1
Enter Origin
Enter Airport id or Code: LHR
Enter Destination
Enter Airport id or Code: HEL

 Select Plane By:
****************
 1. tailnumber
 2. Plane ID
 3. Random of Model
 4. Random

Enter your choice: 4

 Select Pilot By:
*****************
 1. Full Name
 2. Pilot ID
 3. Random Qualifed

Enter your choice: 3
Enter date and time of flight YYYY-MM-DD HH:MM: 2025-10-08 12:00 
Enter the time duration of flight HH:MM: 02:50
Input Flight Number: FM5292
```
### 7. Update data some records

Allows the user to select any table and update any value on it.

> Function displays options for arguments that are parsed individually

> NOTE: Before running this insert at least base data
#### Example

```
Enter your choice: 7
╒════════════════════╕
│ Tables             │
╞════════════════════╡
│ locations          │
├────────────────────┤
│ aircraftTypeRating │
├────────────────────┤
│ aircraftModel      │
├────────────────────┤
│ plane              │
├────────────────────┤
│ pilot              │
├────────────────────┤
│ flights            │
╘════════════════════╛
Select table to update a record from: flights
Enter id to be updated: 102

 Column Options:
**********
╒═════════════════════════╕
│ Tables                  │
╞═════════════════════════╡
│ flight_id               │
├─────────────────────────┤
│ origin_location_id      │
├─────────────────────────┤
│ destination_location_id │
├─────────────────────────┤
│ flight_pilot_id         │
├─────────────────────────┤
│ flight_plane_id         │
├─────────────────────────┤
│ departure_time_utc      │
├─────────────────────────┤
│ arrival_time_utc        │
├─────────────────────────┤
│ passengers_booked       │
├─────────────────────────┤
│ flight_status           │
├─────────────────────────┤
│ time_delay              │
├─────────────────────────┤
│ flight_number           │
╘═════════════════════════╛
Enter column to be updated: passengers_booked
Enter a new value: 106
UPDATE flights SET passengers_booked=106 WHERE flight_id = 102;
```

### 8. Delete data some records

Allows the user to select any table and delete any record on it.

>Function displays options for arguments that are parsed individually

> NOTE: Before running this insert at least base data
#### Example

```
Enter your choice: 8
╒════════════════════╕
│ Tables             │
╞════════════════════╡
│ locations          │
├────────────────────┤
│ aircraftTypeRating │
├────────────────────┤
│ aircraftModel      │
├────────────────────┤
│ plane              │
├────────────────────┤
│ pilot              │
├────────────────────┤
│ flights            │
╘════════════════════╛
Select table to delete from: flights
Enter id to be deleted: 102
DELETE FROM flights WHERE flight_id = 102;
```

### 9. Exit

Exists the program