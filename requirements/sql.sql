------------------------------------------------------------------------------
-- 1. Countries
------------------------------------------------------------------------------
CREATE TABLE countries (
    id                  SERIAL PRIMARY KEY,
    name                VARCHAR(100) UNIQUE NOT NULL,
    -- If you want a default "No Visa Required" setting, remove it and rely on visa_rules
    average_travel_cost DECIMAL(10,2),
    currency            VARCHAR(10),
    language            VARCHAR(100),
    description         TEXT,
    image_url           TEXT
);

------------------------------------------------------------------------------
-- 2. Users
------------------------------------------------------------------------------
CREATE TABLE users (
    id                  SERIAL PRIMARY KEY,
    username            VARCHAR(100) UNIQUE NOT NULL,
    email               VARCHAR(255) UNIQUE NOT NULL,
    password_hash       TEXT NOT NULL,

    first_name          VARCHAR(100),
    last_name           VARCHAR(100),

    -- Link to the country of passport (optional if not set)
    passport_country    INT REFERENCES countries(id) ON DELETE SET NULL,

    preferred_travel_style  VARCHAR(50),
    dietary_needs           VARCHAR(100),
    travel_group_size       INT,
    accessibility_needs     TEXT
);

------------------------------------------------------------------------------
-- 3. Travel Groups (Optional grouping of users)
------------------------------------------------------------------------------
CREATE TABLE travel_groups (
    id          SERIAL PRIMARY KEY,
    name        VARCHAR(255),
    description TEXT
);

CREATE TABLE user_travel_groups (
    user_id         INT REFERENCES users(id) ON DELETE CASCADE,
    travel_group_id INT REFERENCES travel_groups(id) ON DELETE CASCADE,
    PRIMARY KEY (user_id, travel_group_id)
);

------------------------------------------------------------------------------
-- 4. User Preferences (merges budget, accommodation, dining, etc.)
--    You can store them as columns or JSONB. Below uses columns.
------------------------------------------------------------------------------
CREATE TABLE user_preferences (
    id                     SERIAL PRIMARY KEY,
    user_id                INT UNIQUE REFERENCES users(id) ON DELETE CASCADE,

    -- Budget fields
    accommodation_budget   DECIMAL(10,2),
    transportation_budget  DECIMAL(10,2),
    food_budget            DECIMAL(10,2),
    activities_budget      DECIMAL(10,2),
    miscellaneous_budget   DECIMAL(10,2),

    -- Accommodation
    accommodation_type VARCHAR(50)
        CHECK (accommodation_type IN ('Hotel','Hostel','Vacation Rental','Other')),
    preferred_location  VARCHAR(255),
    required_amenities TEXT,

    -- Transportation (no "Flight" included)
    transportation_mode VARCHAR(50)
        CHECK (transportation_mode IN ('Train','Bus','Car Rental','Other')),
    class_preference VARCHAR(50)
        CHECK (class_preference IN ('Economy','Business','First Class')),
    rental_car_type VARCHAR(50),

    -- Activities
    activity_category VARCHAR(100)
        CHECK (activity_category IN ('Sightseeing','Adventure','Relaxation','Cultural','Other')),
    specific_interests TEXT,

    -- Dining
    cuisine_preferences TEXT,
    dining_budget       DECIMAL(10,2)
);

------------------------------------------------------------------------------
-- 5. Points of Interest (Unify Activities, Events, Accommodations, etc.)
------------------------------------------------------------------------------
CREATE TABLE points_of_interest (
    id             SERIAL PRIMARY KEY,
    name           VARCHAR(255) NOT NULL,
    description    TEXT,
    location       VARCHAR(255),
    average_cost   DECIMAL(10,2),
    rating         DECIMAL(3,2) CHECK (rating BETWEEN 0 AND 5),
    image_url      TEXT,

    -- Distinguishes categories (e.g. "Activity", "Event", "Accommodation", "Restaurant", "Transportation", etc.)
    category VARCHAR(50) CHECK (
         category IN ('Activity','Event','Accommodation','Restaurant','Transportation','Other')
    ),

    -- Optional: date range (useful for events)
    start_date     DATE,
    end_date       DATE
);

------------------------------------------------------------------------------
-- 6. (Optional) POI Recommendations for Users
--    A bridging table if you generate AI-based suggestions for user + point_of_interest
------------------------------------------------------------------------------
CREATE TABLE poi_recommendations (
    id           SERIAL PRIMARY KEY,
    user_id      INT REFERENCES users(id) ON DELETE CASCADE,
    poi_id       INT REFERENCES points_of_interest(id) ON DELETE CASCADE,
    score        DECIMAL(5,2) CHECK (score BETWEEN 0 AND 100)
);

------------------------------------------------------------------------------
-- 7. Visa Rules (single definition, no duplication)
------------------------------------------------------------------------------
CREATE TABLE visa_rules (
    id                      SERIAL PRIMARY KEY,
    country_id              INT REFERENCES countries(id) ON DELETE CASCADE,
    passport_country_id     INT REFERENCES countries(id) ON DELETE CASCADE,

    visa_requirement        VARCHAR(50)
        CHECK (visa_requirement IN ('No Visa Required','E-Visa Available','Visa Required')),

    -- Optional fields if you want more detail:
    visa_cost               DECIMAL(10,2),
    processing_time_days     INT,
    additional_requirements  TEXT
);

------------------------------------------------------------------------------
-- 8. Insurance (Optional, if you need multiple providers)
------------------------------------------------------------------------------
CREATE TABLE insurance_options (
    id               SERIAL PRIMARY KEY,
    provider_name    VARCHAR(255),
    coverage_details TEXT,
    cost             DECIMAL(10,2)
);

------------------------------------------------------------------------------
-- 9. Itineraries
------------------------------------------------------------------------------
CREATE TABLE itineraries (
    id                    SERIAL PRIMARY KEY,
    user_id               INT REFERENCES users(id) ON DELETE CASCADE,
    name                  VARCHAR(255) NOT NULL,
    start_date            DATE NOT NULL,
    end_date              DATE NOT NULL,
    total_budget          DECIMAL(10,2) NOT NULL,

    -- Link to a main destination country (optional if multi-country trips)
    destination_country   INT REFERENCES countries(id) ON DELETE CASCADE
);

------------------------------------------------------------------------------
-- 10. Itinerary Items
------------------------------------------------------------------------------
CREATE TABLE itinerary_items (
    id           SERIAL PRIMARY KEY,
    itinerary_id INT REFERENCES itineraries(id) ON DELETE CASCADE,

    date         DATE NOT NULL,
    location     VARCHAR(255),
    activity     VARCHAR(255),   -- e.g. "City Tour" or "Taxi to hotel"
    cost         DECIMAL(10,2),

    category VARCHAR(50) CHECK (
        category IN ('Accommodation','Transportation','Activity','Meal','Other')
    )
);

------------------------------------------------------------------------------
-- 11. (Optional) Link Insurance to an Itinerary
------------------------------------------------------------------------------
CREATE TABLE itinerary_insurance (
    id                  SERIAL PRIMARY KEY,
    itinerary_id        INT REFERENCES itineraries(id) ON DELETE CASCADE,
    insurance_option_id INT REFERENCES insurance_options(id) ON DELETE CASCADE
);

------------------------------------------------------------------------------
-- 12. Reviews (User reviews for countries)
------------------------------------------------------------------------------
CREATE TABLE reviews (
    id          SERIAL PRIMARY KEY,
    user_id     INT REFERENCES users(id) ON DELETE CASCADE,
    country_id  INT REFERENCES countries(id) ON DELETE CASCADE,
    rating      INT CHECK (rating BETWEEN 1 AND 5),
    comment     TEXT,
    created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

------------------------------------------------------------------------------
-- 13. Bookings (If you handle booking logic in-house)
------------------------------------------------------------------------------
CREATE TABLE bookings (
    id           SERIAL PRIMARY KEY,
    user_id      INT REFERENCES users(id) ON DELETE CASCADE,
    itinerary_id INT REFERENCES itineraries(id) ON DELETE CASCADE,
    status       VARCHAR(50) CHECK (status IN ('Booked','Pending','Cancelled')),
    created_at   TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

------------------------------------------------------------------------------
-- 14. Budget Recommendations (If you use AI or logic to match users & countries)
------------------------------------------------------------------------------
CREATE TABLE budget_recommendations (
    id                SERIAL PRIMARY KEY,
    user_id           INT REFERENCES users(id) ON DELETE CASCADE,
    country_id        INT REFERENCES countries(id) ON DELETE CASCADE,
    recommended_budget DECIMAL(10,2) NOT NULL
);

------------------------------------------------------------------------------

/*
  NOTES / TIPS:

  1) By unifying “activities,” “events,” “accommodations” into the single
     `points_of_interest` table, you reduce duplication and queries for
     “what to do in X location” become simpler. Use the `category` column
     to differentiate them.

  2) The `user_preferences` table consolidates accommodation, budget,
     transportation, and dining preferences. You can also store these
     as JSONB if you prefer more flexibility in PostgreSQL.

  3) “Flight” references have been removed from check constraints.
     (e.g., “transportation_mode” no longer includes “Flight.”)

  4) Index foreign keys and columns you’ll search on frequently for 
     better performance, e.g.:
        CREATE INDEX ON visa_rules (country_id, passport_country_id);
        CREATE INDEX ON user_preferences (user_id);
        -- etc.

  5) If you don’t need insurance, remove `insurance_options` and
     `itinerary_insurance`. If you don’t need group travel, remove
     `travel_groups` and `user_travel_groups`.

  6) “Budget Recommendations” and “POI Recommendations” are optional 
     bridging tables if you plan to store recommended countries/POI for
     each user. If not needed, remove them to reduce complexity.
*/
