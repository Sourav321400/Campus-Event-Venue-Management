SET SERVEROUTPUT ON;

-- Test fee calculation
SELECT CALCULATE_EVENT_FEE(40) AS ESTIMATED_FEE FROM DUAL;
SELECT CALCULATE_EVENT_FEE(150) AS ESTIMATED_FEE FROM DUAL;

-- Test booking procedure (use an unused booking ID and an available venue)
BEGIN
    BOOK_VENUE(9001, 1, 101);
END;
/

-- Display booking report
BEGIN
    DISPLAY_BOOKING_REPORT;
END;
/

-- Verify current data
SELECT * FROM EVENTS ORDER BY EVENT_ID;
SELECT * FROM VENUES ORDER BY VENUE_ID;
SELECT * FROM BOOKINGS ORDER BY BOOKING_ID;
SELECT * FROM BOOKING_AUDIT ORDER BY AUDIT_ID;

-- To test the DELETE audit trigger, delete a test booking:
-- DELETE FROM BOOKINGS WHERE BOOKING_ID = 9001;
-- COMMIT;
-- SELECT * FROM BOOKING_AUDIT ORDER BY AUDIT_ID;

-- Note: deleting a booking does not automatically reset VENUES.AVAILABLE.
-- Reset the relevant venue manually when appropriate:
-- UPDATE VENUES SET AVAILABLE = 'Y' WHERE VENUE_ID = 101;
-- COMMIT;
