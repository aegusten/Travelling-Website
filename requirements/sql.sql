CREATE TABLE countries (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) UNIQUE NOT NULL,
    visa_requirement VARCHAR(50) CHECK (visa_requirement IN ('No Visa Required', 'E-Visa Available', 'Visa Required')),
    average_travel_cost DECIMAL(10,2),
    currency VARCHAR(10),
    language VARCHAR(100)
);

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(100) UNIQUE NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    passport_country INT REFERENCES countries(id) ON DELETE SET NULL,
    preferred_travel_style VARCHAR(50),
    dietary_needs VARCHAR(100)
);

CREATE TABLE itineraries (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id) ON DELETE CASCADE,
    name VARCHAR(255) NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    total_budget DECIMAL(10,2) NOT NULL
);

CREATE TABLE itinerary_items (
    id SERIAL PRIMARY KEY,
    itinerary_id INT REFERENCES itineraries(id) ON DELETE CASCADE,
    date DATE NOT NULL,
    location VARCHAR(255),
    activity VARCHAR(255),
    cost DECIMAL(10,2)
);

CREATE TABLE reviews (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id) ON DELETE CASCADE,
    country_id INT REFERENCES countries(id) ON DELETE CASCADE,
    rating INT CHECK (rating BETWEEN 1 AND 5),
    comment TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id) ON DELETE CASCADE,
    itinerary_id INT REFERENCES itineraries(id) ON DELETE CASCADE,
    status VARCHAR(50) CHECK (status IN ('Booked', 'Pending', 'Cancelled')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE activities (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    location VARCHAR(255),
    average_cost DECIMAL(10,2),
    category VARCHAR(100) CHECK (category IN ('Sightseeing', 'Adventure', 'Relaxation', 'Cultural'))
);

CREATE TABLE activity_recommendations (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id) ON DELETE CASCADE,
    activity_id INT REFERENCES activities(id) ON DELETE CASCADE,
    score DECIMAL(5,2) CHECK (score BETWEEN 0 AND 100)
);

CREATE TABLE visa_rules (
    id SERIAL PRIMARY KEY,
    country_id INT REFERENCES countries(id) ON DELETE CASCADE,
    passport_country_id INT REFERENCES countries(id) ON DELETE CASCADE,
    visa_requirement VARCHAR(50) CHECK (visa_requirement IN ('No Visa Required', 'E-Visa Available', 'Visa Required'))
);

CREATE TABLE budget_recommendations (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id) ON DELETE CASCADE,
    country_id INT REFERENCES countries(id) ON DELETE CASCADE,
    recommended_budget DECIMAL(10,2) NOT NULL
);

SELECT c.name AS destination, v.visa_requirement
FROM visa_rules v
JOIN countries c ON v.country_id = c.id
WHERE v.passport_country_id = (
    SELECT passport_country FROM users WHERE id = 1
)
AND v.visa_requirement IN ('No Visa Required', 'E-Visa Available')
ORDER BY visa_requirement;

SELECT c.name AS destination, v.visa_requirement
FROM visa_rules v
JOIN countries c ON v.country_id = c.id
WHERE v.passport_country_id = (
    SELECT passport_country FROM users WHERE id = 1
)
AND v.visa_requirement = 'Visa Required';


