##### IMPORTS ###################

# App Lab packages/bricks
from arduino.app_utils import App, Bridge
from arduino.app_bricks.dbstorage_tsstore import TimeSeriesStore
from arduino.app_bricks.streamlit_ui import st

# Third party packages
import pandas as pd

##### CONSTANTS ###################
UPDATE_FREQUENCY = 10  # seconds between sensor reads

# Chart parameters
QUERY_WINDOW = "-10m"  # how far back to query for charts
AGGR_WINDOW = "1m"     # bucket size for aggregation
SAMPLES_TO_DISPLAY = 6

##### FUNCTIONS #################
# Since Streamlit reruns the Python code from top to bottom on every user interaction,
# Arduino recommends saving Bricks to cache 
@st.cache_resource
def init_db() -> TimeSeriesStore:
    """Initialize and start the Influx database"""
    db_init = TimeSeriesStore()
    db_init.start()
    return db_init

def store_sensor_data_to_db(db) -> None:
    """Call MCU function to get sensor values and save it to the database."""
    sensor_1_data = Bridge.call("readSensor_1")
    db.write_sample("sensor_1", sensor_1_data)

    sensor_2_data = Bridge.call("readSensor_2")
    db.write_sample("sensor_2", sensor_2_data)
    
    ###########################################
    ## ADD BRIDGE CALL & DATABASE WRITE BELOW #
    #⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇#



    #⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆#
    ## ADD BRIDGE CALL & DATABASE WRITE ABOVE #
    ###########################################


def get_samples_for_chart(field_name: str, db) -> pd.DataFrame:
    """Read samples and convert to Dataframe."""

    # read_samples returns a list of tuples
    sensor_data = db.read_samples(
        measure=field_name, # Name of field in database
        start_from=QUERY_WINDOW,
        end_to="now()",
        aggr_window=AGGR_WINDOW,
        aggr_func="max",
        limit=SAMPLES_TO_DISPLAY # How many samples to read
    )

    # Convert tuple to pandas dataframe for easy visualization
    df = pd.DataFrame(sensor_data, columns=["field_name", "timestamp", "value"])
    
    # Convert unwieldy ISO timestamp format to simpler datetime format
    df["timestamp"] = pd.to_datetime(df["timestamp"], format="ISO8601")
    
    return df


@st.fragment(run_every=UPDATE_FREQUENCY)
def read_write_display_loop(db) -> None:
    """Loop that manages the read, write, and display of sensor data."""

    store_sensor_data_to_db(db)

    sensor_1_data = get_samples_for_chart("sensor_1", db)
    sensor_1_chart.line_chart(sensor_1_data, x="timestamp", y="value", height=200)
    
    sensor_2_data = get_samples_for_chart("sensor_2", db)
    sensor_2_chart.line_chart(sensor_2_data, x="timestamp", y="value", height=200)

    ##################################################
    ## ADD CODE TO GET SAMPLES & DISPLAY CHART BELOW #
    #⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇#



    #⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆#
    ## ADD CODE TO GET SAMPLES & DISPLAY CHART ABOVE #
    ##################################################


##### BODY ######################
db_brick = init_db()

st.title("Cave Data")

st.write("sensor 1 data")
sensor_1_chart = st.empty()

st.write("sensor 2 data")
sensor_2_chart = st.empty()

######################################
## ADD UI TEXT AND PLACEHOLDER BELOW #
#⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇#



#⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆#
## ADD UI TEXT AND PLACEHOLDER ABOVE #
######################################

# This function call is what starts the timed looping
read_write_display_loop(db_brick)

App.run() # Optional!  We have handled starting the db brick ourselves 
