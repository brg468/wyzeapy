from enum import Enum


class PropertyIDs(Enum):
    NOTIFICATION = "P1"
    ON = "P3"
    AVAILABLE = "P5"
    BRIGHTNESS = "P1501"  # From 0-100
    COLOR_TEMP = "P1502"  # In Kelvin
    COLOR = "P1507"  # As a hex string RrGgBb
    DOOR_OPEN = "P2001"  # 0 if the door is closed
    CONTACT_STATE = "P1301"
    MOTION_STATE = "P1302"
