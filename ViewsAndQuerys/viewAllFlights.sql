CREATE VIEW IF NOT EXISTS FLIGHTS_TRACKER as
SELECT 
    f.flight_number AS 'Flight Number',
    o.iata_code AS Departure,
    d.iata_code AS Destination,
    STRFTIME('%R',f.departure_time_utc) AS Schedualed,
    STRFTIME('%R',f.departure_time_utc,f.time_delay) AS Expected,
    STRFTIME('%R',f.arrival_time_utc,f.time_delay) AS Arrival,
    f.flight_status AS Status,
    o.city AS 'Origin City',
    d.city AS 'Destination City',
    o.icao_code AS 'Origin Alt Code',
    d.icao_code AS 'Destination Alt Code',
    o.location_name AS 'Origin Airport',
    d.location_name AS 'Destination Airport',
    p.tailnumber AS Tailnumber,
    m.aircraft_model_name AS Aircraft,
    pi.pilot_first_name || ' '|| pi.pilot_last_name AS Pilot
    from flights f
    JOIN locations o on f.origin_location_id = o.location_id
    JOIN locations d on f.destination_location_id = d.location_id
    JOIN plane p on f.flight_plane_id = p.plane_id
    JOIN aircraftModel m on p.plane_model_id = m.aircraft_model_id
    JOIN pilot pi on f.flight_pilot_id = pi.pilot_id;
