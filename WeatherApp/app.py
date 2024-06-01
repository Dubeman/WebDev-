import requests
import os
from flask import Flask, render_template, request
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

app = Flask(__name__)

client = OpenAI()
client.api_key = os.getenv('OPENAI_API_KEY')
OPENWEATHER_API_KEY = os.getenv('OPENWEATHER_API_KEY')

def get_weather_data(city):
    """
    Retrieves weather data for a given city using the OpenWeatherMap API.

    Args:
        city (str): The name of the city.

    Returns:
        dict: The weather data in JSON format.
    """
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_API_KEY}"
    response = requests.get(url)
    return response.json()

def generate_response(weather_data, temperature, top_p):
    """
    Generates a conversational response using the OpenAI GPT-3.5 Turbo model.

    Args:
        weather_data (dict): The weather data for a location.
        temperature (float): The desired temperature parameter for the response.
        top_p (float): The desired top-p parameter for the response.

    Returns:
        str: The generated response in a conversational style.
    """
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": f"The weather data for a location is as follows: {weather_data}. Can you provide a summary in a conversational style? Just the answer is fine."}
    ]
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=temperature,
        max_tokens=150
    )
    return response.choices[0].message.content

@app.route('/', methods=['GET', 'POST'])
def home():
    forecast = None
    if request.method == 'POST':
        city = request.form.get('city')
        temperature = float(request.form.get('temperature'))
        top_p = float(request.form.get('top_p'))

        weather_data = get_weather_data(city)
        forecast = generate_response(weather_data, temperature, top_p)

    return render_template('home.html', forecast=forecast)

if __name__ == '__main__':
    app.run(debug=True)