from modules import cbpi
from modules.core.hardware import ActorBase, SensorPassive, SensorActive
from modules.core.props import Property
from subprocess import call

@cbpi.actor
class Silvercrest(ActorBase):

    a_oncode = Property.Text("Switch ON code", configurable=True, default_value="1125744" )
    b_offcode = Property.Text("Switch OFF code", configurable=True, default_value="2045856" )

    def send(self,  code):
        r = ""
        try:
            call(["sudo /home/clemens/433Utils/RPi_utils/./codesend %s 4 355" % (code)], shell=True)
        except Exception as e:
            self.api.app.logger.error("FAILED to switch 433Mhz Code: %s %s" % (code, r))
        self.api.app.logger.error("SWITCHED 433Mhz Code: %s %s" % (code, r))

    def on(self, power=100):
        self.send(self.a_oncode)

    def off(self):
        self.send(self.b_offcode)


