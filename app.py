from flask import Flask, render_template, request
import configparser
import requests

app = Flask(__name__)
app.debug = True

@app.route('/')
def weather_dashboard():
    return render_template('home.html')

@app.route('/results', methods=['POST'])
def render_results():
    try:
        zip_code = request.form['zipCode']
        api_key = get_api_key()
        
        if not api_key or api_key == 'YOUR_API_KEY_HERE':
            return "Error: Please configure your OpenWeatherMap API key in config.ini"
            
        data = get_weather_results(zip_code, api_key)
        
        # Print the API response for debugging
        print("API Response:", data)
        
        # Check for API error response
        if 'error' in data:
            return f"API Error: {data['error']}"
            
        # Check if required data is present
        if not all(key in data for key in ['main', 'weather', 'name']):
            return f"Error: Invalid API response. Please check your API key and try again. Response: {data}"
        
        if not data['weather']:
            return "Error: No weather data available for this location"
            
        temp = "{0:.2f}".format(data["main"]["temp"])
        feels_like = "{0:.2f}".format(data["main"]["feels_like"])
        weather = data["weather"][0]["main"]
        location = data["name"]

        return render_template('results.html',
                            location=location, temp=temp,
                            feels_like=feels_like, weather=weather)
    except KeyError as e:
        return f"Error: Missing data in API response - {str(e)}"
    except Exception as e:
        return f"An error occurred: {str(e)}"

def get_api_key():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['openweathermap']['api']

def get_weather_results(zip_code, api_key):
    try:
        # Add country code (US) and remove any whitespace from zip code
        zip_code = zip_code.strip()
        api_url = f"https://api.openweathermap.org/data/2.5/weather?zip={zip_code},us&units=imperial&appid={api_key}"
        print(f"Making request to: {api_url}")
        r = requests.get(api_url)
        print(f"Status Code: {r.status_code}")
        print(f"Response: {r.text[:200]}...")  # Print first 200 chars of response
        r.raise_for_status()  # This will raise an HTTPError for bad responses
        return r.json()
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        if hasattr(e, 'response') and e.response is not None:
            print(f"Response content: {e.response.text}")
        return {"error": str(e)}
    except ValueError as e:
        print(f"Failed to parse JSON response: {e}")
        return {"error": "Failed to parse API response"}

if __name__ == '__main__':
    app.run()
