from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MeasurementRequest(_message.Message):
    __slots__ = ("scan_start_time", "location_index", "position", "spectrometer", "voltage_full_wave", "current_full_wave", "thermal", "temp", "pressure", "humid", "mfc", "timestamp", "protocol_index")
    class ThermalDataRow(_message.Message):
        __slots__ = ("temperature",)
        TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
        temperature: _containers.RepeatedScalarFieldContainer[float]
        def __init__(self, temperature: _Optional[_Iterable[float]] = ...) -> None: ...
    class ThermalMatrix(_message.Message):
        __slots__ = ("thermalDataRow",)
        THERMALDATAROW_FIELD_NUMBER: _ClassVar[int]
        thermalDataRow: _containers.RepeatedCompositeFieldContainer[MeasurementRequest.ThermalDataRow]
        def __init__(self, thermalDataRow: _Optional[_Iterable[_Union[MeasurementRequest.ThermalDataRow, _Mapping]]] = ...) -> None: ...
    SCAN_START_TIME_FIELD_NUMBER: _ClassVar[int]
    LOCATION_INDEX_FIELD_NUMBER: _ClassVar[int]
    POSITION_FIELD_NUMBER: _ClassVar[int]
    SPECTROMETER_FIELD_NUMBER: _ClassVar[int]
    VOLTAGE_FULL_WAVE_FIELD_NUMBER: _ClassVar[int]
    CURRENT_FULL_WAVE_FIELD_NUMBER: _ClassVar[int]
    THERMAL_FIELD_NUMBER: _ClassVar[int]
    TEMP_FIELD_NUMBER: _ClassVar[int]
    PRESSURE_FIELD_NUMBER: _ClassVar[int]
    HUMID_FIELD_NUMBER: _ClassVar[int]
    MFC_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    PROTOCOL_INDEX_FIELD_NUMBER: _ClassVar[int]
    scan_start_time: str
    location_index: int
    position: _containers.RepeatedScalarFieldContainer[float]
    spectrometer: _containers.RepeatedScalarFieldContainer[float]
    voltage_full_wave: _containers.RepeatedScalarFieldContainer[float]
    current_full_wave: _containers.RepeatedScalarFieldContainer[float]
    thermal: MeasurementRequest.ThermalMatrix
    temp: float
    pressure: float
    humid: float
    mfc: int
    timestamp: float
    protocol_index: int
    def __init__(self, scan_start_time: _Optional[str] = ..., location_index: _Optional[int] = ..., position: _Optional[_Iterable[float]] = ..., spectrometer: _Optional[_Iterable[float]] = ..., voltage_full_wave: _Optional[_Iterable[float]] = ..., current_full_wave: _Optional[_Iterable[float]] = ..., thermal: _Optional[_Union[MeasurementRequest.ThermalMatrix, _Mapping]] = ..., temp: _Optional[float] = ..., pressure: _Optional[float] = ..., humid: _Optional[float] = ..., mfc: _Optional[int] = ..., timestamp: _Optional[float] = ..., protocol_index: _Optional[int] = ...) -> None: ...

class MeasurementResponse(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: str
    def __init__(self, status: _Optional[str] = ...) -> None: ...
