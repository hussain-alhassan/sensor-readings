# Sensor Readings
Sensor Readings is a software system that does the following:
- It has a file (sensor.py) producing sensor readings.
- Storing the readings to the database.
- It displays the data on a web page with leaving a red alert on the record that has a temperature outside the range -20 .. +15.

## Technologies used:
    - Flask (Python Web Framework)
    - SQLAlchemy (Database Toolkit for Python)

### Instalation (Note: Python 3 is required. For Mac, use python3 in the command line)

1- Open a terminal window and clone the project by running this command.
```sh
git clone git@github.com:hussain-alhassan/sensor-readings.git
```
2- Navigate to the project root directory.
```sh
cd sensor-readings
```
3- Install the dependencies.
```sh
python -m pip install -r requirements.txt
```
4- Migrate the database
```sh
flask db upgrade
```
5- Run the server to test the project on the browser.
```sh
flask run
```
6- Open a new terminal window and navigate to the project root directrory again 'sensor-readings'. Then run this command to allow the sensor to send data to the server.
```sh
python sensor.py
```
7- Click this link http://127.0.0.1:5000 (your url might be slighly different. Note: localhost might not work).


Written by Hussain Alhassan. Feel free to use it :)