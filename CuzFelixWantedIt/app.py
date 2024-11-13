from flask import Flask, render_template, jsonify
import paho.mqtt.client as mqtt

app = Flask(__name__)

# MQTT setup
MQTT_BROKER = "localhost"
MQTT_TOPIC_TEMPHUM = "sensor/temphum"
sensor_data = {"temperature": [], "humidity": []}
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe(MQTT_TOPIC_TEMPHUM)
def on_message(client, userdata, msg):
    data = msg.payload.decode().split(',')
    temperature, humidity = float(data[0]), float(data[1])
    sensor_data["temperature"].append(temperature)
    sensor_data["humidity"].append(humidity)
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_BROKER, 1883, 60)
client.loop_start()
@app.route('/')
def index():
    return render_template('index.html')
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

@app.route('/sensor-data')
def get_sensor_data():
    return jsonify(sensor_data)

@app.route('/latest-sensor-data')
def get_latest_sensor_data():
    if len(sensor_data["temperature"]) > 0 and len(sensor_data["humidity"]) > 0:
        latest_temperature = sensor_data["temperature"][-1]
        latest_humidity = sensor_data["humidity"][-1]
        return jsonify({
            "temperature": latest_temperature,
            "humidity": latest_humidity
        })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')