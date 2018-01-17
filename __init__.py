from modules import cbpi
from modules.core.hardware import ActorBase, SensorPassive, SensorActive
from modules.core.props import Property
from subprocess import call

@cbpi.actor
class Silvercrest(ActorBase):

    a_oncode = Property.Text("Switch ON code", configurable=True, default_value="1125744" )
    b_offcode = Property.Text("Switch OFF code", configurable=True, default_value="2045856" )

    def send(self,  code):
        try:
            call(["sudo /home/clemens/433Utils/RPi_utils/./codesend", code, "4 355"])
        except Exception as e:
            self.api.app.logger.error("FAIELD to switch 433Mhz Code: %s" % (code))

    def on(self, power=100):
        self.send(self.onCommand)

    def off(self):
        self.send(self.onCommand)


