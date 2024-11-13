import sqlite3
from datetime import datetime
from flask import Flask, render_template, jsonify
from flask import Flask, render_template
#import paho.mqtt.client as mqtt

app = Flask(__name__)

# MQTT Configuration
BROKER_ADDRESS = "localhost"  # Change this to your broker's address
TOPIC = "your/topic"

# MQTT callback functions
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe(TOPIC)

def on_message(client, userdata, msg):
    print(f"Message received: {msg.payload.decode()} on topic {msg.topic}")

# Initialize MQTT Client
#mqtt_client = mqtt.Client()
#mqtt_client.on_connect = on_connect
#mqtt_client.on_message = on_message

# Start the MQTT client in the background
#mqtt_client.connect(BROKER_ADDRESS, 1883, 60)
#mqtt_client.loop_start()

# Routes
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/live-data')
def live_data():
    return render_template('live_data.html')

@app.route('/historical-data')
def historical_data():
    return render_template('historical_data.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)


