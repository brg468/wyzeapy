from enum import Enum


class ThermostatProps(Enum):
    APP_VERSION = "app_version"
    IOT_STATE = "iot_state"  # Connection state: connected, disconnected
    SETUP_STATE = "setup_state"
    CURRENT_SCENARIO = "current_scenario"  # home, away
    PROTECT_TIME = "protect_time"
    COOL_SP = "cool_sp"  # Cool stop point
    EMHEAT = "emheat"
    TIME2TEMP_VAL = "time2temp_val"
    SAVE_COMFORT_BALANCE = "save_comfort_balance"  # savings, comfort, or balance value
    QUERY_SCHEDULE = "query_schedule"
    WORKING_STATE = "working_state"  # idle, etc.
    WIRING_LOGIC_ID = "wiring_logic_id"
    W_CITY_ID = "w_city_id"
    FAN_MODE = "fan_mode"  # auto, on, off
    TEMPERATURE = "temperature"  # current temp
    HUMIDITY = "humidity"  # current humidity
    KID_LOCK = "kid_lock"
    CALIBRATE_HUMIDITY = "calibrate_humidity"
    HEAT_SP = "heat_sp"  # heat stop point
    CALIBRATE_TEMPERATURE = "calibrate_temperature"
    MODE_SYS = "mode_sys"  # auto, heat, cool
    W_LAT = "w_lat"
    CONFIG_SCENARIO = "config_scenario"
    FANCIRC_TIME = "fancirc_time"
    W_LON = "w_lon"
    DEV_HOLD = "dev_hold"
    TEMP_UNIT = "temp_unit"
    ASW_HOLD = "asw_hold"
