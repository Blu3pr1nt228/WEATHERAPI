from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Replace 'your_api_key_here' with your actual WeatherAPI.com API key
API_KEY = 'f839973c1d1a4f1ebee14135240807'
BASE_URL = 'http://api.weatherapi.com/v1/current.json'

@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    if not city:
        return jsonify({'error': 'City parameter is required'}), 400
    
    try:
        response = requests.get(BASE_URL, params={'key': API_KEY, 'q': city})
        data = response.json()
        
        if 'error' in data:
            return jsonify({'error': data['error']['message']}), 404
        
        weather_info = {
            'city': data['location']['name'],
            'temperature': data['current']['temp_c'],
            'condition': data['current']['condition']['text'],
            'humidity': data['current']['humidity'],
            'wind_speed': data['current']['wind_kph']
        }
        return jsonify(weather_info), 200
    
    except requests.RequestException as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
