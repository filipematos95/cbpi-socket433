import time
from rpi_rf import RFDevice

from modules import cbpi
from modules.core.hardware import ActorBase, SensorPassive, SensorActive
from modules.core.props import Property

class RemoteSwitch(object):

    def __init__(self, key_on = 742333 , key_off = 742325 ,pin= 17):
       
        self.pin = pin
        self.key_off = key_off
        self.key_on = key_o
        rfdevice.enable_tx()

    def switchOn(self, device):
        rfdevice.tx_code(self.key_on, "default", "default")
        rfdevice.cleanup()  

    def switchOff(self, device):
        rfdevice.tx_code(self.key_off, "default", "default")
        rfdevice.cleanup()  

@cbpi.actor
class Socket433MHz(ActorBase):
    socket = Property.Select("socket", options=[1, 2, 3, 4, 5, 6])
    code_on = Property.Text(label="ON Code", configurable=True, description="Enter the code for turning the 433Hz socket on")
    code_off = Property.Text(label="OFF Code", configurable=True, description="Enter the code for turning the 433Hz socket off")
    pin =  Property.Text(label="GPIO PIN", configurable=True, description="Enter the code GPIO PIN for the rf transmitter")
    
    @classmethod
    def init_global(cls):
        cls.device = RemoteSwitch(key_on=self.code_on, key_off = self.code_off, pin=self.pin)

    def on(self, power=100):
        self.device.switchOn(int(self.socket))

    def off(self):
        self.device.switchOff(int(self.socket))
