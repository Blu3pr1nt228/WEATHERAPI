# Simple Weather API

## Description
This is a simple RESTful API for retrieving weather information for a specific city using WeatherAPI.com.

## Endpoint
- `GET /weather`
  - **Query Parameter:** `city` (name of the city)

## Response Format
- **HTTP 200 OK**
  ```json
  {
    "city": "City Name",
    "temperature": 20.5,
    "condition": "Sunny",
    "humidity": 60,
    "wind_speed": 15.0
  }
