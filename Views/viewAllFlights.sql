CREATE VIEW FLIGHTS_TRACKER as
SELECT 
    f.flight_number AS 'Flight Number',
    o.iata_code AS Departure,
    d.iata_code AS Destination,
    STRFTIME('%R',f.departure_time_utc) AS Schedualed,
    STRFTIME('%R',f.departure_time_utc,f.time_delay) AS Expected,
    f.flight_status AS Status
    from flights f
    JOIN locations o on f.origin_location_id = o.location_id
    JOIN locations d on f.destination_location_id = d.location_id; 
    