-- Keep a log of any SQL queries you execute as you solve the mystery.

-- get the crime description from crime scene reports
SELECT description FROM crime_scene_reports
WHERE month = 7
AND day = 28
AND year = 2021
AND street = 'Humphrey Street';
--Description:S
--Theft of the CS50 duck took place at 10:15am at the Humphrey Street bakery.
--Interviews were conducted today with three witnesses who were present at the time each of their interview transcripts mentions the bakery.
--Littering took place at 16:36. No known witnesses.

--find out what the three witnesses said
SELECT transcript FROM interviews
WHERE month = 7
AND day = 28
AND year = 2021
AND transcript LIKE '%bakery%';
--1.Sometime within ten minutes of the theft, I saw the thief get into a car in the bakery parking lot and drive away.
--  If you have security footage from the bakery parking lot, you might want to look for cars that left the parking lot in that time frame.
--2.I don't know the thief's name, but it was someone I recognized. Earlier this morning, before I arrived at Emma's bakery,
--  I was walking by the ATM on Leggett Street and saw the thief there withdrawing some money.
--3.As the thief was leaving the bakery, they called someone who talked to them for less than a minute. In the call,
--  I heard the thief say that they were planning to take the earliest flight out of Fiftyville tomorrow.
--  The thief then asked the person on the other end of the phone to purchase the flight ticket.

-- find all license_plate exited around the time frame
SELECT activity, license_plate, minute FROM bakery_security_logs
WHERE year = 2021
AND month = 7
AND day = 28
AND hour = 10
AND minute >= 15
ORDER BY minute;
+----------+---------------+--------+
| activity | license_plate | minute |
+----------+---------------+--------+
| exit     | 5P2BI95       | 16     |
| exit     | 94KL13X       | 18     |
| exit     | 6P58WS2       | 18     |
| exit     | 4328GD8       | 19     |
| exit     | G412CB7       | 20     |
| exit     | L93JTIZ       | 21     |
| exit     | 322W7JE       | 23     |
| exit     | 0NTHK55       | 23     |
| exit     | 1106N58       | 35     |
| entrance | NRYN856       | 42     |
| entrance | WD5M8I6       | 44     |
| entrance | V47T75I       | 55     |
+----------+---------------+--------+

--get atm transations on that day
SELECT account_number, amount, transaction_type FROM atm_transactions
WHERE year = 2021
AND month = 7
AND day = 28
AND atm_location = 'Leggett Street';
+----------------+--------+------------------+
| account_number | amount | transaction_type |
+----------------+--------+------------------+
| 28500762       | 48     | withdraw         |
| 28296815       | 20     | withdraw         |
| 76054385       | 60     | withdraw         |
| 49610011       | 50     | withdraw         |
| 16153065       | 80     | withdraw         |
| 86363979       | 10     | deposit          |
| 25506511       | 20     | withdraw         |
| 81061156       | 30     | withdraw         |
| 26013199       | 35     | withdraw         |
+----------------+--------+------------------+

-- find the earliest flight on the next day
SELECT destination_airport_id, id, hour, minute FROM flights
WHERE origin_airport_id IN (SELECT id FROM airports WHERE city = 'Fiftyville')
AND year = 2021
AND month = 7
AND day = 29
ORDER BY hour, minute;
+------------------------+----+------+--------+
| destination_airport_id | id | hour | minute |
+------------------------+----+------+--------+
| 4                      | 36 | 8    | 20     |
| 1                      | 43 | 9    | 30     |
| 11                     | 23 | 12   | 15     |
| 9                      | 53 | 15   | 20     |
| 6                      | 18 | 16   | 0      |
+------------------------+----+------+--------+

--find out the destination city
SELECT city FROM airports WHERE id = 4;
+---------------+
|     city      |
+---------------+
| New York City |
+---------------+

-- find the phone calls less than a minute on that day
SELECT caller, receiver, id FROM phone_calls
WHERE year = 2021
AND month = 7
AND day = 28
AND duration < 60;
+----------------+----------------+-----+
|     caller     |    receiver    | id  |
+----------------+----------------+-----+
| (130) 555-0289 | (996) 555-8899 | 221 |
| (499) 555-9472 | (892) 555-8872 | 224 |
| (367) 555-5533 | (375) 555-8161 | 233 |
| (499) 555-9472 | (717) 555-1342 | 251 |
| (286) 555-6063 | (676) 555-6554 | 254 |
| (770) 555-1861 | (725) 555-3243 | 255 |
| (031) 555-6622 | (910) 555-3251 | 261 |
| (826) 555-1652 | (066) 555-9701 | 279 |
| (338) 555-6650 | (704) 555-2131 | 281 |
+----------------+----------------+-----+


-- find the caller who fits all the descriptions
SELECT name FROM people
WHERE passport_number IN
(SELECT passport_number FROM passengers WHERE flight_id = 36)
AND phone_number IN (SELECT caller FROM phone_calls WHERE year = 2021 AND month = 7 AND day = 28 AND duration < 60)
AND license_plate IN (SELECT license_plate FROM bakery_security_logs WHERE year = 2021 AND month = 7 AND day = 28 AND hour = 10 AND minute >= 15 AND activity = 'exit')
AND id IN (SELECT person_id FROM bank_accounts WHERE account_number IN(
SELECT account_number FROM atm_transactions WHERE year = 2021 AND month = 7 AND day = 28 AND atm_location = 'Leggett Street' AND transaction_type = 'withdraw'));
+--------+
|  name  |
+--------+
| Taylor |
| Bruce  |
+--------+

--since there are two sus, we can get their license plate to see who exit fiftyville closer to 10:15, and it looks like it's Bruce
SELECT name, license_plate FROM people WHERE (name = 'Taylor' OR name = 'Bruce');
+--------+---------------+
|  name  | license_plate |
+--------+---------------+
| Taylor | 1106N58       |
| Bruce  | 94KL13X       |
+--------+---------------+

--find who's the receiver of the call
SELECT name FROM people WHERE phone_number IN(
SELECT receiver FROM phone_calls
WHERE year = 2021
AND month = 7
AND day = 28
AND duration < 60
AND caller IN
(SELECT phone_number FROM people WHERE name = 'Bruce'));
+-------+
| name  |
+-------+
| Robin |
+-------+