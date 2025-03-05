# 🌟 api_cmds – Simple API Command-Line Tools 🚀  

A collection of **cute & functional** CLI tools for fetching cool data from APIs! 🐱‍💻  

## 📦 Installation  

1️⃣ Clone this repo:  

<pre><code>
git clone https://github.com/LilaShiba/api_cmds.git  
cd api_cmds
</code></pre>

2️⃣  Make scripts executable:  

<pre><code>
chmod +x neo weather setup
</code></pre>

3️⃣ (Optional) Move them to `/usr/local/bin/` for global usage:  

<pre><code>
mv neo weather setup /usr/local/bin/
</code></pre>

## ✨ Usage  

💫 Just type the command in your terminal!  

### 🔭 Check for Near-Earth Objects (NEOs)  

<pre><code>
neo
</code></pre>

📡 Example output:  
<pre><code>
🚀 Top Closest Asteroids to Earth 🪐

1. 🪐 (2010 RF12) (2010 RF12)
   📌 ID: bK10R12F
   📅 Last Observed: 2022-08-24
   🔭 Diameter: 0.0071 km
   💨 Velocity: 5.10001588137266 km/s
   🎯 Impact Probability: 0.102637259069
   🌍 Risk Period: 2095-2122
   ───────────────────────────
</code></pre>

### ☁️ Get the Weather  

<pre><code>
weather
</code></pre>

🌤 Example output:  
<pre><code>
🔮 Fetching weather data for station: KLGA...

🌙✨ Magic Weather Report ✨🌙

📍 Station: KLGA
⏳ Timestamp: 2025-03-05T17:51:00+00:00
🌤️  Weather: Cloudy ☁️🌫️
🔥 Temperature: 10.6°C
💦 Dewpoint: 4.4°C
💨 Wind Speed: 27.72 km/h
🧭 Wind Direction: 170°
💧 Humidity: 65.496980088065%
⚖️ Pressure: 100680 Pa

🌟 Stay magical! 🌟
</code></pre>

### 🔑 API Keys  

If API keys are required, create a `.env` file in the same directory:  

<pre><code>
API_KEY=your_api_key_here
</code></pre>

## 📜 License  

This project is licensed under the MIT License.  

---
  
💖 Made with love for simple API commands! 🚀  
