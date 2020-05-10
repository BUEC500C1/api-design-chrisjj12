import openweather

def test_api():
    assert len(openweather.airport_weather("Total Rf Heliport")) != 0
    assert len(openweather.airport_weather("Washington Dulles International Airport")) != 0
    assert len(openweather.airport_weather("Idaho Falls Regional Airport")) != 0
    assert len(openweather.airport_weather("Jamestown Regional Airport")) != 0
    assert len(openweather.airport_weather("Rush County Airport")) != 0
    assert len(openweather.airport_weather("Mooreland Municipal Airport")) != 0
    assert len(openweather.airport_weather("Icheon-dong Heliport")) != 0
    assert len(openweather.airport_weather("Louis Armstrong New Orleans International Airport")) != 0
    assert len(openweather.airport_weather("Osama and Stefan International Domestic Airport")) == 0
