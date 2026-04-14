# import realtime machine data to opcua server
from opcua import Server

# delay the code from crash
import time


class OPCUA:
    server = None
    uri = "Mini-5axis"
    idx = None
    node_isConnected = None
    node_isUSBExist = None
    node_SeriesNo = None
    node_MainBoardPlatformName = None
    node_READ_gcode = None
    node_MainProg = None
    node_CurProg = None
    node_CurSeq = None
    node_Mode = None
    node_Status = None
    node_Alarm = None
    node_AxisName = None
    node_DecPoint = None
    node_Unit = None
    node_Machcoordi = None
    node_Abscoordi = None
    node_Relcoordi = None
    node_distance = None
    node_OvFeed = None
    node_OvSpindle = None
    node_ActFeed = None
    node_ActSpindle = None
    node_PowerOnTime = None
    node_AccCuttingTime = None
    node_CuttingCycle = None
    node_WorkTime = None
    node_part_count = None
    node_require_part_count = None
    node_total_part_count = None
    node_IsAlarm = None
    node_AlmMsg = None
    node_AlmTime = None
    node_record = None
    node_recordcount = None
    node_timestamp = None

    def __init__(self):
        self.server = Server()
        self.server.set_endpoint("opc.tcp://0.0.0.0:4840/Mini-5axis/")
        self.idx = self.server.register_namespace(self.uri)
        self.DBFolder_status_add()

    def start(self):
        if (self.server is not None):
            self.server.start()

    def close(self):
        if (self.server is not None):
            self.server.stop()

    def DBFolder_status_add(self):
        objects = self.server.get_objects_node()
        myobj_information = objects.add_object(self.idx, "information")

        self.node_isConnected = myobj_information.add_variable(
            self.idx, "isConnected", False) #ns=2;i=2
        self.node_isUSBExist = myobj_information.add_variable(
            self.idx, "isUSBExist", False) #ns=2;i=3
        self.node_SeriesNo = myobj_information.add_variable(
            self.idx, "SeriesNo", "1.0.0.0") #ns=2;i=4
        self.node_MainBoardPlatformName = myobj_information.add_variable(
            self.idx, "MainBoardPlatformName", "1.0.0.0") #ns=2;i=5
        self.node_READ_gcode = myobj_information.add_variable(
            self.idx, "gcode", "") #ns=2;i=6

        Read_Status = myobj_information.add_object(self.idx, "cur status")
        self.node_MainProg = Read_Status.add_variable(self.idx, "MainProg","") #ns=2;i=8
        self.node_CurProg = Read_Status.add_variable(self.idx, "CurProg","") #ns=2;i=9
        self.node_CurSeq = Read_Status.add_variable(self.idx, "CurSeq", -1) #ns=2;i=10
        self.node_Mode = Read_Status.add_variable(self.idx, "Mode","") #ns=2;i=11
        self.node_Status = Read_Status.add_variable(self.idx, "Status", "") #ns=2;i=12
        self.node_Alarm = Read_Status.add_variable(self.idx, "Alarm", "") #ns=2;i=13

        Read_Poistion = myobj_information.add_object(self.idx, "cur position")
        self.node_AxisName = Read_Poistion.add_variable(self.idx, "AxisName",["","",""]) #ns=2;i=15
        self.node_DecPoint = Read_Poistion.add_variable(self.idx, "DecPoint", [0.0,0.0,0.0]) #ns=2;i=16
        self.node_Unit = Read_Poistion.add_variable(self.idx, "Unit", ["","",""]) #ns=2;i=17
        self.node_Machcoordi = Read_Poistion.add_variable(self.idx, "Mach coordination", [0.0,0.0,0.0]) #ns=2;i=18
        self.node_Abscoordi = Read_Poistion.add_variable(self.idx, "Abs coordination", [0.0,0.0,0.0]) #ns=2;i=19
        self.node_Relcoordi = Read_Poistion.add_variable(self.idx, "Rel coordination", [0.0,0.0,0.0]) #ns=2;i=20
        self.node_distance = Read_Poistion.add_variable(self.idx, "distance", [0.0,0.0,0.0]) #ns=2;i=21

        READ_spindle = myobj_information.add_object(self.idx, "cur spindle")
        self.node_OvFeed = READ_spindle.add_variable(self.idx, "OvFeed", 0.0) #ns=2;i=23
        self.node_OvSpindle = READ_spindle.add_variable(self.idx, "OvSpindle", 0.0) #ns=2;i=24
        self.node_ActFeed = READ_spindle.add_variable(self.idx, "ActFeed", 0.0) #ns=2;i=25
        self.node_ActSpindle = READ_spindle.add_variable(self.idx, "ActSpindle", 0) #ns=2;i=26

        READ_time = myobj_information.add_object(self.idx, "READ_time")
        self.node_PowerOnTime = READ_time.add_variable(self.idx, "PowerOnTime", 0) #ns=2;i=28
        self.node_AccCuttingTime = READ_time.add_variable(self.idx, "AccCuttingTime", 0) #ns=2;i=29
        self.node_CuttingCycle = READ_time.add_variable(self.idx, "CuttingCycle", 0) #ns=2;i=30
        self.node_WorkTime = READ_time.add_variable(self.idx, "WorkTime", 0) #ns=2;i=31

        READ_part_count = myobj_information.add_object(self.idx, "READ_part_count")
        self.node_part_count = READ_part_count.add_variable(self.idx, "part_count", 0) #ns=2;i=33
        self.node_require_part_count = READ_part_count.add_variable(self.idx, "require_part_count", 0) #ns=2;i=34
        self.node_total_part_count = READ_part_count.add_variable(self.idx, "total_part_count", 0) #ns=2;i=35

        READ_alm_current = myobj_information.add_object(self.idx, "READ_alm_current")
        self.node_IsAlarm = READ_alm_current.add_variable(self.idx, "IsAlarm", False) #ns=2;i=37
        self.node_AlmMsg = READ_alm_current.add_variable(self.idx, "AlmMsg", "") #ns=2;i=38
        self.node_AlmTime = READ_alm_current.add_variable(self.idx, "AlmTime", "") #ns=2;i=39

        READ_nc_record = myobj_information.add_object(self.idx, "READ_nc_record")
        self.node_record = READ_nc_record.add_variable(self.idx, "record", [""]) #ns=2;i=41
        self.node_recordcount = READ_nc_record.add_variable(self.idx, "recordcount", 0) #ns=2;i=42
        
        self.node_timestamp = myobj_information.add_variable(self.idx,"timestamp", 0) #ns=2;i=43

        self.node_isConnected.set_writable()
        self.node_isUSBExist.set_writable()
        self.node_SeriesNo.set_writable()
        self.node_MainBoardPlatformName.set_writable()
        self.node_READ_gcode.set_writable()

        #Read_Status
        self.node_MainProg.set_writable()
        self.node_CurProg.set_writable()
        self.node_CurSeq.set_writable()
        self.node_Mode.set_writable()
        self.node_Status.set_writable()
        self.node_Alarm.set_writable()

        #Read_Poistion
        self.node_AxisName.set_writable()
        self.node_DecPoint.set_writable()
        self.node_Unit.set_writable()
        self.node_Machcoordi.set_writable()
        self.node_Abscoordi.set_writable()
        self.node_Relcoordi.set_writable()
        self.node_distance.set_writable()

        #READ_spindle
        self.node_OvFeed.set_writable()
        self.node_OvSpindle.set_writable()
        self.node_ActFeed.set_writable()
        self.node_ActSpindle.set_writable()

        #READ_time
        self.node_PowerOnTime.set_writable()
        self.node_AccCuttingTime.set_writable()
        self.node_CuttingCycle.set_writable()
        self.node_WorkTime.set_writable()

        #READ_part_count
        self.node_part_count.set_writable()
        self.node_require_part_count.set_writable()
        self.node_total_part_count.set_writable()

        #READ_alm_current
        self.node_IsAlarm.set_writable()
        self.node_AlmMsg.set_writable()
        self.node_AlmTime.set_writable()

        #READ_nc_record
        self.node_record.set_writable()
        self.node_recordcount.set_writable()

        self.node_timestamp.set_writable()

if __name__ == "__main__":

    opcua = OPCUA()
    opcua.start()

    while True:
        try:
            while True:
                time.sleep(1)
        except:
            opcua.close()
