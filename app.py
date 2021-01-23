from flask import Flask, request, Response, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Reading(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sensor_id = db.Column(db.Integer, nullable=False)
    sensor_type = db.Column(db.String(255), nullable=False, default='temperature')
    value = db.Column(db.Integer, nullable=False)
    alert = db.Column(db.Boolean)
    time_stamp = db.Column(db.DateTime, nullable=False, default=datetime.now().astimezone(timezone.utc))

    def json(self):
        return {
            "sensor_id": self.sensor_id,
            "sensor_type": self.sensor_type,
            "value": self.value,
            "time_stamp": self.time_stamp.isoformat()
        }

@app.route('/sensor-readings', methods=['POST'])
def sensor_readings():
    reading = request.json
    reading_record = Reading(
        sensor_id= reading['id'],
        sensor_type = reading['type'],
        value = reading['value'],
        alert = reading['alert'],
        time_stamp = datetime.fromisoformat(reading['time_stamp']),
    )

    db.session.add(reading_record)
    db.session.commit()
    
    return Response(status=204)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get-sensor-readings')
def get_recent_readings():
    
    Recent_readings = Reading.query.all()[-10:]
    return jsonify(list(map(lambda reading: reading.json(), Recent_readings)))

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
