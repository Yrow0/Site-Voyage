-- Insérer les 10 voyages
INSERT INTO app_voyage_trips (departuredate, returndate, destination, transporttype, price, seats)
VALUES
('2024-07-01 08:00:00', '2024-07-10 18:00:00', 'New York', 'Avion', 1000.00, 400),
('2024-08-01 08:00:00', '2024-08-10 18:00:00', 'Paris', 'Train', 800.00, 300),
('2024-09-01 08:00:00', '2024-09-10 18:00:00', 'Tokyo', 'Avion', 1500.00, 500),
('2024-10-01 08:00:00', '2024-10-10 18:00:00', 'London', 'Avion', 1200.00, 450),
('2024-11-01 08:00:00', '2024-11-10 18:00:00', 'Rome', 'Avion', 1100.00, 420),
('2024-12-01 08:00:00', '2024-12-10 18:00:00', 'Sydney', 'Avion', 1800.00, 600),
('2025-01-01 08:00:00', '2025-01-10 18:00:00', 'Barcelona', 'Avion', 1300.00, 480),
('2025-02-01 08:00:00', '2025-02-10 18:00:00', 'Berlin', 'Train', 900.00, 350),
('2025-03-01 08:00:00', '2025-03-10 18:00:00', 'Dubai', 'Avion', 2000.00, 700),
('2025-04-01 08:00:00', '2025-04-10 18:00:00', 'Rio de Janeiro', 'Avion', 1700.00, 550);

-- Insérer 4 hébergements pour chaque voyage
-- Insérer 4 hébergements pour chaque voyage
INSERT INTO app_voyage_accommodation (trip_id, hotelname, address, phonenumber, startdate, enddate, details)
SELECT
    trip.id,
    'Hotel ' || trip.destination || ' ' || num AS hotelname,
    'Address ' || trip.destination || ' ' || num AS address,
    '123-456-' || trip.id || num AS phonenumber,
    trip.departuredate + (num-1) AS startdate,
    trip.departuredate + num AS enddate,
    'Details for Hotel ' || trip.destination || ' ' || num AS details
FROM
    app_voyage_trips AS trip,
    (SELECT 1 AS num UNION SELECT 2 UNION SELECT 3 UNION SELECT 4) AS nums;
