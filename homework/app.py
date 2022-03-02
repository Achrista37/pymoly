import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end>"
    )


@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a series of precipitations"""
    # Query all passengers
    results_prcp = session.query(Measurement.date, Measurement.prcp).all()

    session.close()

    # Create a dictionary from the row data and put into prcp_dict dictionary
    all_prcp =[]
    for date, prcp in results_prcp:
        prcp_dict = {}
        prcp_dict["date"] = date
        prcp_dict["precipitation"] = prcp
        all_prcp.append(prcp_dict)

#    return jsonify(all_prcp)
#    all_prcp = []    
#    for date, prcp in results_prcp:
#        prcp_dict = {}
#        prcp_dict[date] = prcp    
#        all_prcp.append(prcp_dict)
#    return jsonify(prcp_dict)

@app.route("/api/v1.0/stations")
def stations():
# Create our session (link) from Python to the DB
    session = Session(engine)

#    """Return a series of stations"""
#    # Query all passengers
    results_station = session.query(Station.name, Station.station).all()
    session.close()

    # Create a dictionary from the row data and append to a list of all_passengers
    all_stations = []
    for name_st, code in results_station:
        station_dict = {}
        station_dict["name_st"] = name_st
        station_dict["code"] = code
        all_stations.append(station_dict)
    return jsonify(all_stations)


#if __name__ == '__main__':
#    app.run(debug=True)
#from flask import Flask, jsonify

#justice_league_members = [
#    {"superhero": "Aquaman", "real_name": "Arthur Curry"},
#    {"superhero": "Batman", "real_name": "Bruce Wayne"},
#    {"superhero": "Cyborg", "real_name": "Victor Stone"},
#    {"superhero": "Flash", "real_name": "Barry Allen"},
#    {"superhero": "Green Lantern", "real_name": "Hal Jordan"},
#    {"superhero": "Superman", "real_name": "Clark Kent/Kal-El"},
#    {"superhero": "Wonder Woman", "real_name": "Princess Diana"}
#]

#################################################
# Flask Setup
#################################################
#app = Flask(__name__)


#################################################
# Flask Routes
#################################################

#@app.route("/api/v1.0/justice-league")
#def justice_league():
#    """Return the justice league data as json"""
#
#    return jsonify(justice_league_members)
#
#
#@app.route("/")
#def welcome():
#    return (
#        f"Welcome to the Justice League API!<br/>"
#        f"Available Routes:<br/>"
#        f"/api/v1.0/justice-league<br/>"
#        f"/api/v1.0/justice-league/superhero/batman"
#    )


#"""TODO: Handle API route with variable path to allow getting info
#for a specific character based on their 'superhero' name """


if __name__ == "__main__":
    app.run(debug=True)
