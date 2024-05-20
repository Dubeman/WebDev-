import pytest
import app

def test_get_weather_data():
    # Use a known city for the test
    city = 'London'
    data = app.get_weather_data(city)
    print(data)

    # Check that the function returns data for the correct city
    assert data['name'] == city

    # Check that the function returns a 'weather' field in the response
    assert 'weather' in data

#add a test to check OpenAI is responding something and is not a error
def test_generate_response():
    weather_data = {
        "name": "London",
        "weather": [{"description": "clear sky"}]
    }
    temperature = 0.5
    top_p = 0.5

    response = app.generate_response(weather_data, temperature, top_p)
    print(response)

    assert response is not None
    assert response != ''
