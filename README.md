Step 1: Set Up MySQL
Ensure your MySQL database is up and running, and you have the necessary credentials to access it.

Step 2: Install an MQTT Broker
You'll need an MQTT broker to handle the communication between MySQL and OpenRemote. You can use brokers like Mosquitto, HiveMQ, or any other MQTT broker

Navigate to Mosquitto Directory
-------------------------------
Download Mosquitto

 cd "C:\Program Files\mosquitto"
Start mosquitto
-----------------
mosquitto

Verify Mosquitto is Running
----------------------------
Check Listening Ports: Run the following command to see if Mosquitto is listening on port 1883:
netstat -an | find "1883"

#Use mosquitto_pub and mosquitto_sub Commands: 
These command-line tools allow you to publish and subscribe to topic

Test the Installation
---------------------
Open Command Prompt: Press Win + R, type cmd, and press Enter.

#Start Mosquitto: Type mosquitto -v and press Enter.
 You should see Mosquitto starting and waiting for connections1.
 
#Test Publishing and Subscribing: Open two Command Prompt windows.
 In the first window, type mosquitto_sub -t "test/topic". 
 In the second window, type mosquitto_pub -t "test/topic" -m "Hello, Mosquitto!". 
 You should see the message "Hello, Mosquitto!" in the subscriber window1.
 
 Verify MQTT Connection:
 ____________________________
 Use the mosquitto_pub and mosquitto_sub commands to ensure that your MQTT client is able to publish and subscribe to messages.
 Subscribe to a topic using:
 ------------------------------
 mosquitto_sub -h localhost -t "test/topic"
 In another terminal, publish a message to the same topic:
 ----------------------------------------------------------
 mosquitto_pub -h localhost -t "test/topic" -m "Test message"
 
 #subscribe to the MQTT topic and check if the data is being published successfully:
 
 mosquitto_sub -h localhost -t "robotdb/device_data"

Step 3: Create a Script to Fetch Data from MySQL

#Using the PyCharm Interface
Open PyCharm: Launch your PyCharm IDE.
Open a Project: Open the project where you want to install the packages.
Open Settings: Go to File > Settings (or PyCharm > Preferences on macOS).
Project Interpreter: In the left pane, select Project: <Your Project Name> and then click on Project Interpreter.
Add Packages: Click on the + button on the right side of the window to open the Available Packages dialog.
Search and Install: In the search bar, type paho-mqtt and click Install Package. Repeat the process for mysql-connector-python

##Write a script to fetch data from MySQL and publish it to the MQTT broker. Here's an example using Python: //Done

Step 4: Set Up OpenRemote MQTT Agent
In OpenRemote, create an MQTT Agent to subscribe to the topic you're publishing to. Here's how:

Create an MQTT Agent: Go to the OpenRemote Manager UI and create a new MQTT Agent.

Configure the Agent: Set the MQTT broker address, port, and credentials if needed.

Set the Publish/Subscribe Topic: Configure the topic to which you're publishing data from MySQL5 .

5. Link Assets to MQTT Agent
Create assets in OpenRemote and link their attributes to the MQTT Agent. This way, when data is published to the MQTT topic, it will be received by OpenRemote and stored in the linked assets
