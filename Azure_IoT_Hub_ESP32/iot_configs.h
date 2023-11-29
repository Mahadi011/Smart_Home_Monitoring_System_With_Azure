// Wifi
#define IOT_CONFIG_WIFI_SSID "Your SSID"
#define IOT_CONFIG_WIFI_PASSWORD "Your password"
#ifdef IOT_CONFIG_USE_X509_CERT

#define IOT_CONFIG_DEVICE_CERT "Device Certificate"
#define IOT_CONFIG_DEVICE_CERT_PRIVATE_KEY "Device Certificate Private Key"
#endif 
// Azure IoT
#define IOT_CONFIG_IOTHUB_FQDN "DTHsensor.azure-devices.net"
#define IOT_CONFIG_DEVICE_ID "people_count"
// Use device key if not using certificates
#ifndef IOT_CONFIG_USE_X509_CERT
#define IOT_CONFIG_DEVICE_KEY "tv40egvGIdS5qSoxtwE82TbQPq0t6xNzIAIoTNap4OA="
#endif // IOT_CONFIG_USE_X509_CERT

// Publish 1 message every 2 seconds
#define TELEMETRY_FREQUENCY_MILLISECS 2000
