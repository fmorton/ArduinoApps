from arduino.app_utils import App,Bridge
from arduino.app_bricks.streamlit_ui import st

REFRESH_INTERVAL_SECONDS = 2

@st.fragment(run_every=REFRESH_INTERVAL_SECONDS)
def read_sensors() -> None:
    sensorValue = Bridge.call("readSensor")

    st.metric(label="Sensor", value=sensorValue)

st.title("Title Goes Here")
st.divider() # Horizontal line

read_sensors()

App.run() 