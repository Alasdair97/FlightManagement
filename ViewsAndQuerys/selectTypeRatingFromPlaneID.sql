SELECT aircraft_type_rating_id FROM aircraftTypeRating atr
JOIN plane p on am.aircraft_model_id = p.plane_model_id
JOIN aircraftModel am on atr.aircraft_type_rating_id = am.aircraft_model_type_rating_id
WHERE p.plane_id = 'X';