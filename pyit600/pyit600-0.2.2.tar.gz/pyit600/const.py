"""Constants for the Salus iT600 smart devices."""

# Degree units
DEGREE = "°"

# Temperature units
TEMP_CELSIUS = f"{DEGREE}C"

# States
STATE_UNKNOWN = "unknown"

# Supported climate features
SUPPORT_TARGET_TEMPERATURE = 1
SUPPORT_PRESET_MODE = 16

# Supported cover features
SUPPORT_OPEN = 1
SUPPORT_CLOSE = 2
SUPPORT_SET_POSITION = 4

# HVAC modes
HVAC_MODE_OFF = "off"
HVAC_MODE_HEAT = "heat"
HVAC_MODE_AUTO = "auto"

# HVAC states
CURRENT_HVAC_OFF = "off"
CURRENT_HVAC_HEAT = "heating"
CURRENT_HVAC_IDLE = "idle"

# Supported presets
PRESET_FOLLOW_SCHEDULE = "Follow Schedule"
PRESET_PERMANENT_HOLD = "Permanent Hold"
PRESET_OFF = "Off"
