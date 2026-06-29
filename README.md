# 🌦️ PyWeather

<p align="center">
  <img src="PyWeather Images/logo.png" alt="PyWeather Logo" width="180" height="70">
</p>

<p align="center">

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey)
![GUI](https://img.shields.io/badge/GUI-Tkinter-green)
![License](https://img.shields.io/badge/License-Apache2.0-yellow)
![Status](https://img.shields.io/badge/Status-Completed-success)

</p>

## Development of a Real-Time Weather Monitoring and Forecasting System for Nigeria

**PyWeather** is a Python-based desktop application developed as an undergraduate thesis project in the Department of Meteorology and Climate Science. The application provides real-time weather monitoring, weather forecasting, climate information, and data visualization for locations across Nigeria through an intuitive graphical user interface.

The system integrates multiple weather APIs and climate datasets to provide current weather conditions, short-term forecasts, satellite imagery, and historical climate information in a single application.

---

# 📖 Table of Contents

- About
- Features
- System Architecture
- Screenshots
- Technologies Used
- APIs and Data Sources
- Installation
- Future Improvements
- Research Contribution
- Author
- Citation
- License

---

# 🌍 About

Weather information is essential for agriculture, disaster risk reduction, aviation, transportation, education, and daily decision-making. Access to accurate and timely weather information helps communities prepare for extreme weather events and improve resilience.

PyWeather was developed to provide an easy-to-use desktop application capable of delivering:

- Real-time weather observations
- Weather forecasts
- Satellite imagery
- Climate data
- Weather visualization

specifically for Nigeria.

---

# ✨ Features

## 🌤 Current Weather

- Temperature
- Feels Like Temperature
- Humidity
- Atmospheric Pressure
- Wind Speed
- Wind Direction
- Visibility
- Cloud Cover
- Sunrise & Sunset
- Weather Description

---

## 📅 Weather Forecast

- Hourly Forecast
- Daily Forecast
- Rain Probability
- Wind Forecast

---

## 🛰 Satellite Imagery

Display satellite imagery showing

- Cloud Cover
- Rainfall
- Thunderstorms
- Weather Systems

---

## 🌍 Climate Data

Historical climate information including

- Land Surface Temperature
- Climate Trends
- Long-term Temperature Records

---

## 📈 Data Visualization

Interactive charts displaying

- Temperature Trends
- Humidity
- Pressure
- Wind Speed
- Weather Variables

---

## 💾 Data Logging

Automatically save weather observations into CSV files for future analysis.

---

# 🏗 System Architecture

```
                Weather APIs
                      │
                      ▼
            Data Collection Module
                      │
                      ▼
           Weather Processing Engine
                      │
         ┌────────────┼────────────┐
         ▼            ▼            ▼
 Current Weather   Forecast    Climate Data
         │            │            │
         └────────────┼────────────┘
                      ▼
               Visualization Layer
                      ▼
               Tkinter GUI
```

---

# 📷 Screenshots

## Home Page

<h2>Application Preview</h2>

<p align="center">
  <img src="PyWeather Images/logo.png" width="48%">
  <img src="PyWeather Images/logo.png" width="48%">
</p>

<p align="center">
  <img src="PyWeather Images/logo.png" width="48%">
  <img src="PyWeather Images/logo.png" width="48%">
</p>

<p align="center">
  <img src="PyWeather Images/logo.png" width="48%">
  <img src="PyWeather Images/logo.png" width="48%">
</p>

---

## Current Weather

> *(Insert Screenshot)*

---

## Forecast

> *(Insert Screenshot)*

---

## Satellite Imagery

> *(Insert Screenshot)*

---

## Charts

> *(Insert Screenshot)*

---

# 🛠 Technologies Used

- Python
- Tkinter
- OpenWeatherMap API
- ERA5
- Requests
- Pandas
- Matplotlib
- Pillow
- CSV
- JSON

---

# 🌐 APIs and Data Sources

| API | Purpose |
|------|----------|
| OpenWeatherMap | Current Weather |
| OpenWeatherMap Forecast API | Weather Forecast |
| ERA5 | Climate Data |
| Satellite Imagery Providers | Weather Satellite Images |

---

# ⚙ Installation

Clone the repository

```bash
git clone https://github.com/yourusername/PyWeather.git
```

Navigate to the project

```bash
cd PyWeather
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
python main.py
```


---

# 🚀 Future Improvements

- Air Quality Monitoring
- Heat Stress Index
- Flood Early Warning
- Machine Learning Forecasting
- Mobile Version
- Web Dashboard
- GIS Integration
- Severe Weather Alerts
- Climate Risk Assessment
- User Accounts
- Weather Notifications

---

# 🎓 Research Contribution

This project was developed as an undergraduate thesis titled:

> **Development of a Real-Time Weather Monitoring and Forecasting System for Nigeria (PyWeather)**

The research demonstrates how Python can be leveraged to develop an integrated weather monitoring system that improves access to meteorological information for Nigeria.

---

# 📊 Potential Applications

- Meteorological Services
- Universities
- Schools
- Farmers
- Aviation
- Disaster Management
- Transportation
- Climate Research
- Environmental Monitoring

---

# 👨‍💻 Author

**Ajalaruru Usman Olamilekan**

Meteorologist | Python Developer | Climate Researcher

Department of Meteorology and Climate Science

Federal University of Technology Akure (FUTA)

Nigeria

---

# 📚 Citation

If you use this project in your research, please cite:

```
Ajalaruru, U. O. (2025).
Development of a Real-Time Weather Monitoring and Forecasting System for Nigeria (PyWeather).
Undergraduate Thesis,
Department of Meteorology and Climate Science,
Federal University of Technology Akure.
```

---

# 🤝 Contributing

Contributions are welcome.

1. Fork the repository.

2. Create a feature branch.

3. Commit your changes.

4. Push to your fork.

5. Submit a Pull Request.

---

# ⭐ Support

If you find this project useful, please consider giving it a ⭐ on GitHub.

---

# 📄 License

This project is licensed under the MIT License.

See the LICENSE file for details.
