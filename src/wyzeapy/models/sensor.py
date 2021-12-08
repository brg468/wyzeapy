from typing import Dict, Any

from wyzeapy.models import Device, DeviceTypes


class Sensor(Device):
    def __init__(self, dictionary: Dict[Any, Any]):
        super().__init__(dictionary)

    @property
    def activity_detected(self) -> int:
        if self.type is DeviceTypes.CONTACT_SENSOR:
            return int(self.device_params['open_close_state'])
        elif self.type is DeviceTypes.MOTION_SENSOR:
            return int(self.device_params['motion_state'])
        else:
            raise AssertionError("Device must be of type CONTACT_SENSOR or MOTION_SENSOR")

    @property
    def is_low_battery(self) -> int:
        return int(self.device_params['is_low_battery'])
