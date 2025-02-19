# Python script to fetch data from MySQL and publish it to OpenRemote via MQTT
import pymysql
import paho.mqtt.client as mqtt
import json
import time
from prettytable import PrettyTable

# MySQL Configuration
MYSQL_HOST = "13.247.23.5"
MYSQL_USER = "robot"
MYSQL_PASSWORD = "robot123#"
MYSQL_DB = "robotdb"

# MQTT Configuration
MQTT_BROKER = "localhost"  # Change if using a remote broker
MQTT_PORT = 1883
MQTT_TOPIC = "robotdb/device_data"

# Connect to MySQL
db = pymysql.connect(host=MYSQL_HOST, user=MYSQL_USER, password=MYSQL_PASSWORD, database=MYSQL_DB)
cursor = db.cursor()

# Connect to MQTT
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.connect(MQTT_BROKER, MQTT_PORT, 60)


def fetch_and_publish_device_data():
    try:
        query = "SELECT id, Start_date, End_date, Diagnostic, Code, Serial, Operator_Id, Bed_Id FROM device_data;"
        cursor.execute(query)
        rows = cursor.fetchall()

        # Create a table to display the fetched data
        table = PrettyTable()
        table.field_names = ["Id", "Start Date", "End Date", "Diagnostic", "Code", "Serial", "Operator Id", "Bed Id"]

        for row in rows:
            if len(row) >= 8:
                payload = {
                    "Id": row[0],
                    "Start_Date": row[1],
                    "End_Date": row[2],
                    "Diagnostic": row[3],
                    "Code": row[4],
                    "Serial": row[5],
                    "Operator_Id": row[6],
                    "Bed_Id": row[7]
                }
                client.publish(MQTT_TOPIC, json.dumps(payload))
                print(f"Published: {payload}")

                # Add row to the table
                table.add_row([row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]])
            else:
                print(f"Skipping row due to insufficient length: {row}")

        print(table)

    except Exception as e:
        print(f"An error occurred: {e}")


# Monitor database changes and publish data in real-time
def monitor_database():
    last_row_count = 0
    while True:
        query = "SELECT COUNT(*) FROM device_data;"
        cursor.execute(query)
        row_count = cursor.fetchone()[0]

        if row_count != last_row_count:
            fetch_and_publish_device_data()
            last_row_count = row_count

        time.sleep(5)  # Adjust the sleep time as needed

monitor_database()
