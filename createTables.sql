CREATE TABLE IF NOT EXISTS locations (
    location_id INTEGER PRIMARY KEY,
    icao_code TEXT NOT NULL UNIQUE, -- Unique keys as airports cannot have duplicate ICAO/IATA codes 
    iata_code TEXT NOT NULL UNIQUE,
    location_name TEXT NOT NULL UNIQUE,
    city TEXT NOT NULL,
    country TEXT NOT NULL,
    local_timezone_utc TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS aircraftTypeRating (
    aircraft_type_rating_id INTEGER PRIMARY KEY,
    licence_endorsement TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS aircraftModel (
    aircraft_model_id INTEGER PRIMARY KEY,
    aircraft_model_type_rating_id TEXT NOT NULL,
    aircraft_manufacturer TEXT NOT NULL,
    capacity TEXT NOT NULL,
    FOREIGN KEY(aircraft_model_type_rating_id) REFERENCES aircraftTypeRating(aircraft_type_rating_id)-- Foreign key refrencing which type rating is needed to fly this model of aircraft
);

CREATE TABLE IF NOT EXISTS plane (
    plane_id INTEGER PRIMARY KEY,
    tailnumber TEXT NOT NULL,
    plane_model_id TEXT NOT NULL,
    FOREIGN KEY(plane_model_id) REFERENCES aircraftModel(aircraft_model_id)-- Foreign key refrencing what model of plane an idividiaul plane is
);

CREATE TABLE IF NOT EXISTS pilot (
    pilot_id INTEGER PRIMARY KEY,
    pilot_first_name TEXT NOT NULL,
    pilot_last_name TEXT NOT NULL,
    pilot_type_rating_id INTEGER NOT NULL,
    FOREIGN KEY(pilot_type_rating_id) REFERENCES aircraftTypeRating(aircraft_type_rating_id)-- Foreign key refrencing type rating the pilot holds
);

CREATE TABLE IF NOT EXISTS flights (
    flight_id INTEGER PRIMARY KEY,
    origin_location_id INTEGER NOT NULL,
    destination_location_id INTEGER NOT NULL,
    flight_pilot_id INTEGER NOT NULL,
    flight_plane_id INTEGER NOT NULL,
    departure_time_utc TEXT NOT NULL,
    arrival_time_utc TEXT NOT NULL,
    passengers_booked INTEGER DEFAULT 0,-- using a default so when a new flight can be schedualed without specifing there are zero passengers
    flight_status TEXT NOT NULL,
    time_delay TEXT,
    FOREIGN KEY(origin_location_id) REFERENCES locations(location_id), -- forgein keys refrencing both origin and destination locations
    FOREIGN KEY(destination_location_id) REFERENCES locations(location_id),
    FOREIGN KEY(flight_pilot_id) REFERENCES pilot(pilot_id), -- foreign key refrencing pilot for the flight
    FOREIGN KEY(flight_plane_id) REFERENCES plane(plane_id) -- foreign key refrencing plane for the flight
);