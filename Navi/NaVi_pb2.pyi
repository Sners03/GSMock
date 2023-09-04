from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Empty(_message.Message):
    __slots__ = ["debugMessage"]
    DEBUGMESSAGE_FIELD_NUMBER: _ClassVar[int]
    debugMessage: str
    def __init__(self, debugMessage: _Optional[str] = ...) -> None: ...

class PtfValues(_message.Message):
    __slots__ = ["panValueDeg", "tiltValueDeg", "focusValue"]
    PANVALUEDEG_FIELD_NUMBER: _ClassVar[int]
    TILTVALUEDEG_FIELD_NUMBER: _ClassVar[int]
    FOCUSVALUE_FIELD_NUMBER: _ClassVar[int]
    panValueDeg: float
    tiltValueDeg: float
    focusValue: float
    def __init__(self, panValueDeg: _Optional[float] = ..., tiltValueDeg: _Optional[float] = ..., focusValue: _Optional[float] = ...) -> None: ...

class Target(_message.Message):
    __slots__ = ["xMeter", "yMeter"]
    XMETER_FIELD_NUMBER: _ClassVar[int]
    YMETER_FIELD_NUMBER: _ClassVar[int]
    xMeter: float
    yMeter: float
    def __init__(self, xMeter: _Optional[float] = ..., yMeter: _Optional[float] = ...) -> None: ...

class Position3d(_message.Message):
    __slots__ = ["xMeter", "yMeter", "zMeter"]
    XMETER_FIELD_NUMBER: _ClassVar[int]
    YMETER_FIELD_NUMBER: _ClassVar[int]
    ZMETER_FIELD_NUMBER: _ClassVar[int]
    xMeter: float
    yMeter: float
    zMeter: float
    def __init__(self, xMeter: _Optional[float] = ..., yMeter: _Optional[float] = ..., zMeter: _Optional[float] = ...) -> None: ...

class Quaternion(_message.Message):
    __slots__ = ["w", "x", "y", "z"]
    W_FIELD_NUMBER: _ClassVar[int]
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    Z_FIELD_NUMBER: _ClassVar[int]
    w: float
    x: float
    y: float
    z: float
    def __init__(self, w: _Optional[float] = ..., x: _Optional[float] = ..., y: _Optional[float] = ..., z: _Optional[float] = ...) -> None: ...

class Pose(_message.Message):
    __slots__ = ["position", "orientation"]
    POSITION_FIELD_NUMBER: _ClassVar[int]
    ORIENTATION_FIELD_NUMBER: _ClassVar[int]
    position: Position3d
    orientation: Quaternion
    def __init__(self, position: _Optional[_Union[Position3d, _Mapping]] = ..., orientation: _Optional[_Union[Quaternion, _Mapping]] = ...) -> None: ...

class TargetStatus(_message.Message):
    __slots__ = ["isReached", "isUnreachable", "isAborted"]
    ISREACHED_FIELD_NUMBER: _ClassVar[int]
    ISUNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    ISABORTED_FIELD_NUMBER: _ClassVar[int]
    isReached: bool
    isUnreachable: bool
    isAborted: bool
    def __init__(self, isReached: bool = ..., isUnreachable: bool = ..., isAborted: bool = ...) -> None: ...

class Point3d(_message.Message):
    __slots__ = ["x", "y", "z"]
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    Z_FIELD_NUMBER: _ClassVar[int]
    x: float
    y: float
    z: float
    def __init__(self, x: _Optional[float] = ..., y: _Optional[float] = ..., z: _Optional[float] = ...) -> None: ...

class PointCloud(_message.Message):
    __slots__ = ["point"]
    POINT_FIELD_NUMBER: _ClassVar[int]
    point: _containers.RepeatedCompositeFieldContainer[Point3d]
    def __init__(self, point: _Optional[_Iterable[_Union[Point3d, _Mapping]]] = ...) -> None: ...

class Position2d(_message.Message):
    __slots__ = ["xMeter", "yMeter"]
    XMETER_FIELD_NUMBER: _ClassVar[int]
    YMETER_FIELD_NUMBER: _ClassVar[int]
    xMeter: float
    yMeter: float
    def __init__(self, xMeter: _Optional[float] = ..., yMeter: _Optional[float] = ...) -> None: ...

class Path(_message.Message):
    __slots__ = ["waypoint"]
    WAYPOINT_FIELD_NUMBER: _ClassVar[int]
    waypoint: _containers.RepeatedCompositeFieldContainer[Position2d]
    def __init__(self, waypoint: _Optional[_Iterable[_Union[Position2d, _Mapping]]] = ...) -> None: ...

class Weight(_message.Message):
    __slots__ = ["weightGram"]
    WEIGHTGRAM_FIELD_NUMBER: _ClassVar[int]
    weightGram: float
    def __init__(self, weightGram: _Optional[float] = ...) -> None: ...

class Telemetry(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
