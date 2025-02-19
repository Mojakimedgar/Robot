# Python script to fetch data from MySQL and publish it to OpenRemote via MQTT
import pymysql
import paho.mqtt.client as mqtt
import json
import time

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

def fetch_and_publishdevicedata():
    try:
        query = "SELECT id, Start_date, End_date, Diagnostic, Code, Serial, Operator_Id, Bed_Id FROM device_data;"
        cursor.execute(query)
        rows = cursor.fetchall()

        # Check the number of rows returned
        print(f"Total rows: {len(rows)}")

        for row in rows:
            print(f"Row: {row}, Length: {len(row)}")  # Debugging line
            try:

                if len(row) >= 8:  # Ensure length of row is at least 3
                    payload = {
                        "Id": row[0],
                        "Start_Date": row[1],
                        "End_Date": row[2],
                        "Diagnostic": row[3],
                        "Code": row[4],
                        "Serial": row[5],
                        "Operator_Id": row[6],
                        "Bed_Id": row[1]
                    }
                    # Publish data to MQTT
                    client.publish(MQTT_TOPIC, json.dumps(payload))
                    print(f"Published: {payload}")
                    time.sleep(1)  # Prevent flooding
                else:
                    print(f"Skipping row due to insufficient length: {row}")
            except IndexError as e:
                print(f"Error accessing tuple indices for row {row}: {e}")

    except Exception as e:
        print(f"An error occurred: {e}")

"""
def fetch_and_publishModem():
    try:
        query = "SELECT Modem_num, Sim_num, Serial FROM modem;"
        #query = "SELECT id, Start_date, End_date, Diagnostic, Code, Serial, Operator_Id, Bed_Id FROM device_data;"
        cursor.execute(query)
        rows = cursor.fetchall()

        # Check the number of rows returned
        print(f"Total rows: {len(rows)}")

        for row in rows:
            print(f"Row: {row}, Length: {len(row)}")  # Debugging line
            try:

                if len(row) >= 3:  # Ensure length of row is at least 3
                    payload = {
                        "Modem_Num": row[0],
                        "Sim_num": row[1],
                        "Serial": row[2]
                    }
                    # Publish data to MQTT
                    client.publish(MQTT_TOPIC, json.dumps(payload))
                    print(f"Published: {payload}")
                    time.sleep(1)  # Prevent flooding
                else:
                    print(f"Skipping row due to insufficient length: {row}")
            except IndexError as e:
                print(f"Error accessing tuple indices for row {row}: {e}")

    except Exception as e:
        print(f"An error occurred: {e}")


def fetch_and_publishOperator():
    try:
        query = "SELECT Operator_Id, First_name, Last_name, Username, CODE, Shift, Role FROM operator;"
        cursor.execute(query)
        rows = cursor.fetchall()

        # Check the number of rows returned
        print(f"Total rows: {len(rows)}")

        for row in rows:
            print(f"Row: {row}, Length: {len(row)}")  # Debugging line
            try:

                if len(row) >= 6:  # Ensure length of row is at least 3
                    payload = {
                        "Operator_Id": row[0],
                        "First_name": row[1],
                        "Last_name": row[2],
                        "Username": row[3],
                        "CODE": row[4],
                        "Shift": row[5],
                        "Role": row[6],

                    }
                    # Publish data to MQTT
                    client.publish(MQTT_TOPIC, json.dumps(payload))
                    print(f"Published: {payload}")
                    time.sleep(1)  # Prevent flooding
                else:
                    print(f"Skipping row due to insufficient length: {row}")
            except IndexError as e:
                print(f"Error accessing tuple indices for row {row}: {e}")

    except Exception as e:
        print(f"An error occurred: {e}")
        

def fetch_and_publishRobot():
    try:
        query = "SELECT Serial, Hospital_Id FROM robot;"
        cursor.execute(query)
        rows = cursor.fetchall()

        # Check the number of rows returned
        print(f"Total rows: {len(rows)}")

        for row in rows:
            print(f"Row: {row}, Length: {len(row)}")  # Debugging line
            try:

                if len(row) >= 2:  # Ensure length of row is at least 3
                    payload = {
                        "Operator_Id": row[0],
                        "First_name": row[1]
                    }
                    # Publish data to MQTT
                    client.publish(MQTT_TOPIC, json.dumps(payload))
                    print(f"Published: {payload}")
                    time.sleep(1)  # Prevent flooding
                else:
                    print(f"Skipping row due to insufficient length: {row}")
            except IndexError as e:
                print(f"Error accessing tuple indices for row {row}: {e}")

    except Exception as e:
        print(f"An error occurred: {e}")


def fetch_and_publishHospital():
    try:
        query = "SELECT Hospital_Id, Hospital_Name, Hospital_Group_Id FROM hospital;"
        cursor.execute(query)
        rows = cursor.fetchall()

        # Check the number of rows returned
        print(f"Total rows: {len(rows)}")

        for row in rows:
            print(f"Row: {row}, Length: {len(row)}")  # Debugging line
            try:

                if len(row) >= 22:  # Ensure length of row is at least 3
                    payload = {
                        "Hospital_Id,": row[0],
                        "Hospital_Name": row[1],
                        "Hospital_Group_Id": row[2]
                    }
                    # Publish data to MQTT
                    client.publish(MQTT_TOPIC, json.dumps(payload))
                    print(f"Published: {payload}")
                    time.sleep(1)  # Prevent flooding
                else:
                    print(f"Skipping row due to insufficient length: {row}")
            except IndexError as e:
                print(f"Error accessing tuple indices for row {row}: {e}")

    except Exception as e:
        print(f"An error occurred: {e}")

"""
fetch_and_publishdevicedata()
#fetch_and_publishModem()
#fetch_and_publishOperator()
#fetch_and_publishRobot()
#fetch_and_publishHospital()

