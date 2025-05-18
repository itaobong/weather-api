# 🌦️ Weather Dashboard with Flask

A simple weather dashboard that displays current weather information for a given ZIP code using the [OpenWeatherMap API](https://openweathermap.org/api).


## 🔧 Setup Instructions

### 1. Get an API Key

* Visit [OpenWeatherMap](https://openweathermap.org/api) and sign up for a free account.
* Once logged in, go to your dashboard and copy your **API key**.


### 2. Create a `config.ini` File

In the root directory of the project, create a file named `config.ini` with the following contents:

```ini
[openweathermap]
api=YOUR_API_KEY_HERE
```

🔒 **Replace `YOUR_API_KEY_HERE` with your actual API key.**

> ✅ Sample `config.ini`:

```ini
[openweathermap]
api=88073a42dddddddddd
```

### 3. Install Dependencies

Make sure you have Python 3.6 or later installed. Then run:

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
python app.py
```

Once running, open your browser and visit:

```
http://127.0.0.1:5000/
```

## ✨ Features

* Enter a ZIP code to get current weather information
* Displays:

  * Temperature
  * Weather condition
  * “Feels like” temperature
* Clean, responsive design
* Mobile-friendly interface

## 📦 Dependencies

* Python 3.6+
* Flask
* Werkzeug
* Requests
* configparser
