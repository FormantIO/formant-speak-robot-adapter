from formant.sdk.agent.v1 import Client as FormantClient
import pyttsx3
import time

class FormantSpeakAdapter:
    def __init__(self):
        print("Initializing Formant Speak, Robot! adapter")
        
        # # Create Formant client and register callbacks
        self._fclient = FormantClient(ignore_throttled=True, ignore_unavailable=True)
        self._fclient.register_config_update_callback(self._start_restart)
        self._fclient.create_event("ONVIF Adapter online", notify=False, severity="info")
        self._fclient.register_command_request_callback(
            self.handle_speech_request, command_filter=["speak_robot"]
        )

        # # Create text to speech enging
        self.engine = pyttsx3.init()

        self._rate = 125
        self._volume = 1.0
        self._voice = 1

        self._update_config()


    def _formant_log(self, log):
        print(log)
        self._fclient.post_text(
            "speak_adapter.info", log)
        time.sleep(0.25)

    def _start_restart(self):
        pass

    def _update_config(self):
        # Pull new values from app config if they exist
        try:
            self._formant_log("Starting config update")
            self._rate = str(self._fclient.get_app_config("speech_rate", self._rate))
            self._rate = str(self._fclient.get_app_config("speech_volume", self._volume))
            self._rate = str(self._fclient.get_app_config("speech_voice", self._voice))
 
            self.engine.setProperty('rate', self._rate)
            self.engine.setProperty('volume', self._volume)

            voices = self.engine.getProperty('voices')
            self.engine.setProperty('voice', voices[self._voice].id)
            
        except Exception as e:
            self._formant_log("Failed config update %s" % str(e))


    def handle_speech_request(self, text):
        try:
            self.engine.say(str(text.data))
            self.engine.runAndWait()

        except Exception as e:
            self._fclient.post_text("speak_adapter.errors", "Error handling command: %s" %  str(e))

if __name__ == "__main__":
    FormantSpeakAdapter()
