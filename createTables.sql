CREATE TABLE location (
    location_id INTEGER PRIMARY KEY,
    icao_code TEXT NOT NULL UNIQUE,
    iata_code TEXT NOT NULL UNIQUE,
    location_name TEXT NOT NULL UNIQUE,
    city TEXT NOT NULL,
    country TEXT NOT NULL,
    local_timezone_utc TEXT NOT NULL
);

CREATE TABLE aircraftTypeRating (
    aircraft_type_rating_id INTEGER PRIMARY KEY,
    licence_endorsement TEXT NOT NULL
);

CREATE TABLE aircraftModel (
    aircraft_model_id INTEGER PRIMARY KEY,
    aircraft_model_type_rating_id TEXT NOT NULL,
    aircraft_manufacturer TEXT NOT NULL,
    capacity TEXT NOT NULL,
    FOREIGN KEY(aircraft_model_type_rating_id) REFERNCES aircraftTypeRating(aircraft_type_rating_id)
);

CREATE TABLE plane (
    plane_id INTEGER PRIMARY KEY,
    tailnumber TEXT NOT NULL,
    plane_model_id TEXT NOT NULL,
    FOREIGN KEY(plane_model_id) REFERNCES aircraftModel(aircraft_model_id)
);

CREATE TABLE pilot (
    pilot_id INTEGER PRIMARY KEY,
    pilot_first_name TEXT NOT NULL,
    pilot_last_name TEXT NOT NULL,
    pilot_type_rating_id INTEGER NOT NULL,
    FOREIGN KEY(pilot_type_rating_id) REFERNCES aircraftTypeRating(aircraft_type_rating_id)
);

CREATE TABLE flights (
    flight_id INTEGER PRIMARY KEY,
    origin_location_id INTEGER NOT NULL,
    destination_location_id INTEGER NOT NULL,
    flight_pilot_id INTEGER NOT NULL,
    plane_id INTEGER NOT NULL,
    departure_time_utc DATETIME NOT NULL,
    arrival_time_utc DATETIME NOT NULL,
    passengers_booked INTEGER DEFUALT 0,
    flight_status TEXT NOT NULL,
    time_delay TEXT,
    FOREIGN KEY(origin_location_id) REFERNCES location(location_id),
    FOREIGN KEY(destination_location_id) REFERNCES location(location_id),
    FOREIGN KEY(flight_pilot_id) REFERNCES pilot(pilot_id),
    FOREIGN KEY(destination_location_id) REFERNCES location(location_id)
);