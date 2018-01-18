from modules import cbpi
from modules.core.hardware import ActorBase, SensorPassive, SensorActive
from modules.core.props import Property
from subprocess import call

@cbpi.actor
class Silvercrest433Mhz(ActorBase):

    socket = Property.Select("socket", options=["A", "B", "C", "D"])

    on_codes = {
    	'A': '1045296',
    	'B': '1045300',
    	'C': '1045308',
    	'D': '772370'
    }

    off_codes = {
    	'A': '280608',
    	'B': '230816',
    	'C': '772380',
    	'D': '1045298'
    }

    def send(self,  code):
        try:
            call(["sudo /home/pi/433Utils/RPi_utils/./codesend %s 4 355" % (code)], shell=True)
        except Exception as e:
            self.api.app.logger.error("FAILED to switch Silvercrest 433Mhz Code: %s" % (code))

    def on(self, power=100):
        self.send(self.on_codes[self.socket])
        self.api.app.logger.info("SWITCHED Silvercrest 433Mhz Socket: %s - %s" % (self.socket, self.on_codes[self.socket]))

    def off(self):
        self.send(self.off_codes[self.socket])
        self.api.app.logger.info("SWITCHED Silvercrest 433Mhz Socket: %s - %s" % (self.socket, self.off_codes[self.socket]))

@cbpi.actor
class SelfLearning433Mhz(ActorBase):

    oncode = Property.Text("Switch ON code", configurable=True, default_value="")
    offcode = Property.Text("Switch OFF code", configurable=True, default_value="")

    def send(self,  code):
        try:
            call(["sudo /home/pi/433Utils/RPi_utils/./codesend %s 4 355" % (code)], shell=True)
        except Exception as e:
            self.api.app.logger.error("FAILED to switch 433Mhz Code: %s" % (code))
        self.api.app.logger.info("SWITCHED Selflearning 433Mhz Code: %s" % (code))

    def on(self, power=100):
        self.send(self.oncode)
        self.api.app.logger.info("SWITCHED Selflearning 433Mhz Socket: %s" % (self.oncode))

    def off(self):
        self.send(self.offcode)
        self.api.app.logger.info("SWITCHED Selflearning 433Mhz Socket: %s" % (self.offcode))
