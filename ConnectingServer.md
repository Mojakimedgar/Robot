ConnectingServer
__________________________________

--Navigate to PuTTY Directory
cd "C:\Program Files\PuTTY"

--start PuTTY and specify your .ppk file for authentication
putty.exe -i C:\Users\Asus\Downloads\NXTPULSE\NXTPULSE.ppk ubuntu@13.246.253.61

Installing Docker
_______________________________
sudo apt-get update
sudo apt-get install -y docker.io
sudo systemctl start docker
sudo systemctl enable dockers

Install Docker Compose: OpenRemote requires Docker Compose to manage multiple containers.
------------------------------------------------------------------------------------------
sudo apt-get install -y docker-compose


Installing Openremote in Ubuntu
_______________________________

Create a directory for OpenRemote:
----------------------------------

sudo mkdir -p /opt/openremote
cd /opt/openremote

Clone the OpenRemote repository:
--------------------------------
sudo git clone https://github.com/openremote/openremote.git
cd openremote

Build the Docker images:
------------------------------
sudo make all

Start OpenRemote using Docker Compose:
---------------------------------------
sudo docker-compose up

You can access the OpenRemote web interface using http://localhost:8688

Create a Docker compose file 
______________________________________
Already have a dir >>>>so skip
sudo mkdir -p /opt/openremote
cd /opt/openremote

Create a docker-compose yml file
---------------------------------
sudo nano docker-compose.yml

Add the OpenRemote docker-compose configuration
------------------------------------------------
version: '3'

services:
  manager:
    image: openremote/manager
    ports:
      - "8080:8080"
      - "443:443"
    environment:
      - TZ=Etc/UTC
    volumes:
      - manager_data:/data
    networks:
      - openremote_net

  keycloak:
    image: quay.io/keycloak/keycloak:latest
    environment:
      - KEYCLOAK_USER=admin
      - KEYCLOAK_PASSWORD=admin
      - PROXY_ADDRESS_FORWARDING=true
      - DB_VENDOR=h2
    ports:
      - "9080:8080"
    networks:
      - openremote_net

volumes:
  manager_data:

networks:
  openremote_net:
    driver: bridge

--------------------------------------------------------

Save a close the file
----------------------
ctrl + o >>save Enter  ..Ctrl + x to exit

Start OpenRemote Using Docker Compose
---------------------------------------
sudo docker-compose up -d

Access OpenRemote: Open your web browser and navigate to http://localhost:8080 to access the OpenRemote interface






























