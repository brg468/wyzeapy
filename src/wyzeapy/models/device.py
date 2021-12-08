from typing import Dict, Any

from wyzeapy.models.device_types import DeviceTypes


class Device:
    product_type: str
    product_model: str
    mac: str
    nickname: str
    device_params: Dict[str, Any]
    raw_dict: Dict[str, Any]
    callback_function = None

    def __init__(self, dictionary: Dict[Any, Any]):
        self.available = False

        self.raw_dict = dictionary
        for k, v in dictionary.items():
            setattr(self, k, v)

    @property
    def type(self) -> DeviceTypes:
        try:
            return DeviceTypes(self.product_type)
        except ValueError:
            return DeviceTypes.UNKNOWN

    def __repr__(self) -> str:
        return "<Device: {}, {}>".format(DeviceTypes(self.product_type), self.mac)
