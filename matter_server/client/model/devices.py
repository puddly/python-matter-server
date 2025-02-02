from __future__ import annotations

from .device import MatterDevice

from matter_server.vendor.chip.clusters import Objects as all_clusters


class OrphanClusters(MatterDevice, device_type=0xF001):
    """Orphan Clusters."""

    clusters = {
        all_clusters.ProxyConfiguration,
        all_clusters.ProxyDiscovery,
        all_clusters.ProxyValid,
        all_clusters.PulseWidthModulation,
    }


class RootNode(MatterDevice, device_type=0x0016):
    """Root Node."""

    clusters = {
        all_clusters.AccessControl,
        all_clusters.Basic,
        all_clusters.Descriptor,
        all_clusters.GeneralCommissioning,
        all_clusters.PowerSourceConfiguration,
        all_clusters.TimeSynchronization,
        all_clusters.GroupKeyManagement,
        all_clusters.NetworkCommissioning,
        all_clusters.AdministratorCommissioning,
        all_clusters.OperationalCredentials,
        all_clusters.LocalizationConfiguration,
        all_clusters.TimeFormatLocalization,
        all_clusters.UnitLocalization,
        all_clusters.GeneralDiagnostics,
        all_clusters.DiagnosticLogs,
        all_clusters.SoftwareDiagnostics,
        all_clusters.EthernetNetworkDiagnostics,
        all_clusters.WiFiNetworkDiagnostics,
        all_clusters.ThreadNetworkDiagnostics,
    }


class PowerSource(MatterDevice, device_type=0x0011):
    """Power Source."""

    clusters = {
        all_clusters.Identify,
        all_clusters.Descriptor,
        all_clusters.PowerSource,
    }


class OtaRequestor(MatterDevice, device_type=0x0012):
    """OTA Requestor."""

    clusters = {
        all_clusters.Identify,
        all_clusters.Descriptor,
        all_clusters.OtaSoftwareUpdateRequestor,
    }


class OtaProvider(MatterDevice, device_type=0x0014):
    """OTA Provider."""

    clusters = {
        all_clusters.Identify,
        all_clusters.Descriptor,
        all_clusters.OtaSoftwareUpdateProvider,
    }


class Bridge(MatterDevice, device_type=0x000E):
    """Bridge."""

    clusters = {
        all_clusters.Identify,
        all_clusters.Descriptor,
        all_clusters.BridgedActions,
    }


class BridgedDevice(MatterDevice, device_type=0x0013):
    """Bridged Device."""

    clusters = {
        all_clusters.Identify,
        all_clusters.Descriptor,
        all_clusters.BridgedDeviceBasic,
        all_clusters.PowerSourceConfiguration,
        all_clusters.PowerSource,
    }


class OnOffLight(MatterDevice, device_type=0x0100):
    """On/Off Light."""

    clusters = {
        all_clusters.Identify,
        all_clusters.Descriptor,
        all_clusters.Groups,
        all_clusters.Scenes,
        all_clusters.OnOff,
        all_clusters.LevelControl,
    }


class DimmableLight(MatterDevice, device_type=0x0101):
    """Dimmable Light."""

    clusters = {
        all_clusters.Identify,
        all_clusters.Descriptor,
        all_clusters.Groups,
        all_clusters.Scenes,
        all_clusters.OnOff,
        all_clusters.LevelControl,
    }


class ColorTemperatureLight(MatterDevice, device_type=0x010C):
    """Color Temperature Light."""

    clusters = {
        all_clusters.Identify,
        all_clusters.Descriptor,
        all_clusters.Groups,
        all_clusters.Scenes,
        all_clusters.OnOff,
        all_clusters.LevelControl,
        all_clusters.ColorControl,
    }


class ExtendedColorLight(MatterDevice, device_type=0x010D):
    """Extended Color Light."""

    clusters = {
        all_clusters.Identify,
        all_clusters.Descriptor,
        all_clusters.Groups,
        all_clusters.Scenes,
        all_clusters.OnOff,
        all_clusters.LevelControl,
        all_clusters.ColorControl,
    }


class OnOffPlugInUnit(MatterDevice, device_type=0x010A):
    """On/Off Plug-in Unit."""

    clusters = {
        all_clusters.Identify,
        all_clusters.Descriptor,
        all_clusters.Groups,
        all_clusters.Scenes,
        all_clusters.OnOff,
        all_clusters.LevelControl,
    }


class DimmablePlugInUnit(MatterDevice, device_type=0x010B):
    """Dimmable Plug-in Unit."""

    clusters = {
        all_clusters.Identify,
        all_clusters.Descriptor,
        all_clusters.Groups,
        all_clusters.Scenes,
        all_clusters.OnOff,
        all_clusters.LevelControl,
    }


class Pump(MatterDevice, device_type=0x0303):
    """Pump."""

    clusters = {
        all_clusters.Identify,
        all_clusters.Descriptor,
        all_clusters.Groups,
        all_clusters.Scenes,
        all_clusters.OnOff,
        all_clusters.PumpConfigurationAndControl,
        all_clusters.LevelControl,
        all_clusters.TemperatureMeasurement,
        all_clusters.PressureMeasurement,
        all_clusters.FlowMeasurement,
    }


class OnOffLightSwitch(MatterDevice, device_type=0x0103):
    """On/Off Light Switch."""

    clusters = {
        all_clusters.Identify,
        all_clusters.Descriptor,
        all_clusters.Groups,
        all_clusters.Scenes,
    }


class DimmerSwitch(MatterDevice, device_type=0x0104):
    """Dimmer Switch."""

    clusters = {
        all_clusters.Identify,
        all_clusters.Descriptor,
        all_clusters.Groups,
        all_clusters.Scenes,
    }


class ColorDimmerSwitch(MatterDevice, device_type=0x0105):
    """Color Dimmer Switch."""

    clusters = {
        all_clusters.Identify,
        all_clusters.Descriptor,
        all_clusters.Groups,
        all_clusters.Scenes,
    }


class ControlBridge(MatterDevice, device_type=0x0840):
    """Control Bridge."""

    clusters = {
        all_clusters.Identify,
        all_clusters.Descriptor,
        all_clusters.Groups,
        all_clusters.Scenes,
    }


class PumpController(MatterDevice, device_type=0x0304):
    """Pump Controller."""

    clusters = {
        all_clusters.Identify,
        all_clusters.Descriptor,
        all_clusters.Groups,
        all_clusters.Scenes,
    }


class GenericSwitch(MatterDevice, device_type=0x000F):
    """Generic Switch."""

    clusters = {
        all_clusters.Identify,
        all_clusters.Descriptor,
        all_clusters.Groups,
        all_clusters.Scenes,
        all_clusters.Switch,
        all_clusters.FixedLabel,
        all_clusters.UserLabel,
    }


class ContactSensor(MatterDevice, device_type=0x0015):
    """Contact Sensor."""

    clusters = {
        all_clusters.Identify,
        all_clusters.Descriptor,
        all_clusters.Groups,
    }


class LightSensor(MatterDevice, device_type=0x0106):
    """Light Sensor."""

    clusters = {
        all_clusters.Identify,
        all_clusters.Descriptor,
        all_clusters.Groups,
        all_clusters.IlluminanceMeasurement,
    }


class OccupancySensor(MatterDevice, device_type=0x0107):
    """Occupancy Sensor."""

    clusters = {
        all_clusters.Identify,
        all_clusters.Descriptor,
        all_clusters.Groups,
        all_clusters.OccupancySensing,
    }


class TemperatureSensor(MatterDevice, device_type=0x0302):
    """Temperature Sensor."""

    clusters = {
        all_clusters.Identify,
        all_clusters.Descriptor,
        all_clusters.Groups,
        all_clusters.TemperatureMeasurement,
    }


class PressureSensor(MatterDevice, device_type=0x0305):
    """Pressure Sensor."""

    clusters = {
        all_clusters.Identify,
        all_clusters.Descriptor,
        all_clusters.Groups,
        all_clusters.PressureMeasurement,
    }


class FlowSensor(MatterDevice, device_type=0x0306):
    """Flow Sensor."""

    clusters = {
        all_clusters.Identify,
        all_clusters.Descriptor,
        all_clusters.Groups,
        all_clusters.FlowMeasurement,
    }


class HumiditySensor(MatterDevice, device_type=0x0307):
    """Humidity Sensor."""

    clusters = {
        all_clusters.Identify,
        all_clusters.Descriptor,
        all_clusters.Groups,
        all_clusters.RelativeHumidityMeasurement,
    }


class OnOffSensor(MatterDevice, device_type=0x0850):
    """On/Off Sensor."""

    clusters = {
        all_clusters.Identify,
        all_clusters.Descriptor,
        all_clusters.Groups,
        all_clusters.Scenes,
    }


class DoorLock(MatterDevice, device_type=0x000A):
    """Door Lock."""

    clusters = {
        all_clusters.Identify,
        all_clusters.Descriptor,
        all_clusters.Scenes,
        all_clusters.Groups,
        all_clusters.DoorLock,
        all_clusters.Alarms,
        all_clusters.PollControl,
        all_clusters.ElectricalMeasurement,
        all_clusters.TimeSynchronization,
    }


class DoorLockController(MatterDevice, device_type=0x000B):
    """Door Lock Controller."""

    clusters = {
        all_clusters.Identify,
        all_clusters.Descriptor,
        all_clusters.Scenes,
        all_clusters.Groups,
        all_clusters.TimeSynchronization,
    }


class WindowCovering(MatterDevice, device_type=0x0202):
    """Window Covering."""

    clusters = {
        all_clusters.Identify,
        all_clusters.Descriptor,
        all_clusters.Scenes,
        all_clusters.Groups,
        all_clusters.WindowCovering,
    }


class WindowCoveringController(MatterDevice, device_type=0x0203):
    """Window Covering Controller."""

    clusters = {
        all_clusters.Identify,
        all_clusters.Descriptor,
        all_clusters.Scenes,
        all_clusters.Groups,
    }


class HeatingCoolingUnit(MatterDevice, device_type=0x0300):
    """Heating/Cooling Unit."""

    clusters = {
        all_clusters.Identify,
        all_clusters.Descriptor,
        all_clusters.Groups,
        all_clusters.Thermostat,
        all_clusters.FanControl,
        all_clusters.LevelControl,
        all_clusters.OnOff,
    }


class Thermostat(MatterDevice, device_type=0x0301):
    """Thermostat."""

    clusters = {
        all_clusters.Identify,
        all_clusters.Descriptor,
        all_clusters.Scenes,
        all_clusters.Groups,
        all_clusters.Alarms,
        all_clusters.Thermostat,
        all_clusters.ThermostatUserInterfaceConfiguration,
        all_clusters.FanControl,
        all_clusters.TemperatureMeasurement,
        all_clusters.OccupancySensing,
        all_clusters.RelativeHumidityMeasurement,
    }


class Fan(MatterDevice, device_type=0x002B):
    """Fan."""

    clusters = {
        all_clusters.Identify,
        all_clusters.Groups,
        all_clusters.FanControl,
    }


class VideoPlayer(MatterDevice, device_type=0x0023):
    """Video Player."""

    clusters = {
        all_clusters.Identify,
        all_clusters.Descriptor,
        all_clusters.MediaPlayback,
        all_clusters.KeypadInput,
        all_clusters.ApplicationLauncher,
        all_clusters.MediaInput,
        all_clusters.OnOff,
        all_clusters.Channel,
        all_clusters.AudioOutput,
        all_clusters.LowPower,
        all_clusters.WakeOnLan,
        all_clusters.TargetNavigator,
        all_clusters.AccountLogin,
        all_clusters.ContentLauncher,
    }


class Speaker(MatterDevice, device_type=0x0022):
    """Speaker."""

    clusters = {
        all_clusters.Identify,
        all_clusters.Descriptor,
        all_clusters.OnOff,
        all_clusters.LevelControl,
    }


class ContentApplication(MatterDevice, device_type=0x0024):
    """Content Application."""

    clusters = {
        all_clusters.Identify,
        all_clusters.Descriptor,
        all_clusters.ApplicationBasic,
        all_clusters.KeypadInput,
        all_clusters.ApplicationLauncher,
        all_clusters.AccountLogin,
        all_clusters.ContentLauncher,
        all_clusters.MediaPlayback,
        all_clusters.TargetNavigator,
        all_clusters.Channel,
    }


class ModeSelect(MatterDevice, device_type=0x0027):
    """Mode Select."""

    clusters = {
        all_clusters.Identify,
        all_clusters.Descriptor,
        all_clusters.ModeSelect,
    }


class AllClustersAppServerExample(MatterDevice, device_type=0x0000):
    """All-clusters-app Server Example."""

    clusters = {
        all_clusters.Identify,
        all_clusters.Descriptor,
        all_clusters.BarrierControl,
        all_clusters.ColorControl,
        all_clusters.DoorLock,
        all_clusters.Groups,
        all_clusters.IasZone,
        all_clusters.LevelControl,
        all_clusters.OnOff,
        all_clusters.Scenes,
        all_clusters.TemperatureMeasurement,
    }


class SecondaryNetworkCommissioningDeviceType(MatterDevice, device_type=0xF002):
    """Secondary Network Commissioning Device Type."""

    clusters = {
        all_clusters.NetworkCommissioning,
    }
