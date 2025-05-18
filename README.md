# Weather Dashboard with Flask

A simple weather dashboard that displays current weather information for a given zip code using the OpenWeatherMap API.

## Setup Instructions

1. **Get an API Key**
   - Go to [OpenWeatherMap](https://openweathermap.org/) and sign up for a free account
   - Get your API key from your account dashboard

2. **Configure the Application**
   - Open `config.ini` and replace `YOUR_API_KEY_HERE` with your actual OpenWeatherMap API key

3. **Install Dependencies**
   ```
   pip install -r requirements.txt
   ```

4. **Run the Application**
   ```
   python app.py
   ```

5. **Access the Application**
   - Open a web browser and go to `http://127.0.0.1:5000/`

## Features

- Enter a zip code to get current weather information
- Displays temperature, weather condition, and "feels like" temperature
- Clean, responsive design
- Mobile-friendly interface

## Dependencies

- Python 3.6+
- Flask
- Requests
- configparser
