"""Huawei LTE constants."""

DOMAIN = "huawei_lte"

DEFAULT_DEVICE_NAME = "LTE"

UPDATE_SIGNAL = f"{DOMAIN}_update"
UPDATE_OPTIONS_SIGNAL = f"{DOMAIN}_options_update"

KEY_DEVICE_BASIC_INFORMATION = "device_basic_information"
KEY_DEVICE_INFORMATION = "device_information"
KEY_DEVICE_SIGNAL = "device_signal"
KEY_MONITORING_TRAFFIC_STATISTICS = "monitoring_traffic_statistics"
KEY_WLAN_HOST_LIST = "wlan_host_list"

DEVICE_TRACKER_KEYS = {KEY_WLAN_HOST_LIST}

SENSOR_KEYS = {
    KEY_DEVICE_INFORMATION,
    KEY_DEVICE_SIGNAL,
    KEY_MONITORING_TRAFFIC_STATISTICS,
}

ALL_KEYS = DEVICE_TRACKER_KEYS | SENSOR_KEYS
