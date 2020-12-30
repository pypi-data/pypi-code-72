# automatically generated by the FlatBuffers compiler, do not modify

# namespace: flat

import flatbuffers

# /// The state of a rigid body in Rocket League's physics engine.
# /// This gets updated in time with the physics tick, not the rendering framerate.
# /// The frame field will be incremented every time the physics engine ticks.
class RigidBodyState(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsRigidBodyState(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = RigidBodyState()
        x.Init(buf, n + offset)
        return x

    # RigidBodyState
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # RigidBodyState
    def Frame(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # RigidBodyState
    def Location(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            x = o + self._tab.Pos
            from .Vector3 import Vector3
            obj = Vector3()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # RigidBodyState
    def Rotation(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            x = o + self._tab.Pos
            from .Quaternion import Quaternion
            obj = Quaternion()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # RigidBodyState
    def Velocity(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            x = o + self._tab.Pos
            from .Vector3 import Vector3
            obj = Vector3()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # RigidBodyState
    def AngularVelocity(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            x = o + self._tab.Pos
            from .Vector3 import Vector3
            obj = Vector3()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

def RigidBodyStateStart(builder): builder.StartObject(5)
def RigidBodyStateAddFrame(builder, frame): builder.PrependInt32Slot(0, frame, 0)
def RigidBodyStateAddLocation(builder, location): builder.PrependStructSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(location), 0)
def RigidBodyStateAddRotation(builder, rotation): builder.PrependStructSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(rotation), 0)
def RigidBodyStateAddVelocity(builder, velocity): builder.PrependStructSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(velocity), 0)
def RigidBodyStateAddAngularVelocity(builder, angularVelocity): builder.PrependStructSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(angularVelocity), 0)
def RigidBodyStateEnd(builder): return builder.EndObject()
