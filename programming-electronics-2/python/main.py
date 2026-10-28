import ast
from arduino.app_bricks.cloud_llm import CloudLLM, CloudModel
from arduino.app_bricks.streamlit_ui import st
from arduino.app_utils import App, Bridge
from prompt import SYSTEM_MESSAGE

# The st.cache_resource decorator below saves the return value of a function into cache.
# This means there is only a single CloudLLM object created, even when Streamlit reruns the App.
@st.cache_resource
def init_llm_brick() -> CloudLLM:
    """Initialize the Brick (API key is loaded from configuration)"""
    return CloudLLM(
        model=CloudModel.ANTHROPIC_CLAUDE,
        system_prompt=SYSTEM_MESSAGE
    )


def play_melody(message, llm: CloudLLM):
    """Get LLM melody response and send to MCU via Bridge."""
    print("message is " + str(message))
    if message:
        response = llm.chat(message)
        print(response)

        try:
            # melody variable needs passed to MCU
            melody = ast.literal_eval(response)

            print("melody is " + str(melody))

            Bridge.call("playSounds", melody)
        except (ValueError, SyntaxError):
            print(f"LLM returned unexpected format: {response}")

llm_brick = init_llm_brick()

st.title("Robot Noise Generator")

with st.container():
    user_input = st.chat_input("generate a robot noise")

play_melody(user_input, llm_brick)

App.run()