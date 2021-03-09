import cstruct

class veryHighPriorityData(cstruct.CStruct):
    __byte_order__ = cstruct.LITTLE_ENDIAN
    __struct__ = """
        int16_t imuAxes[6];
        uint32_t epoch;
     """
    def print_info(self):
        print("\nepoch: "+str(self.epoch))
        print("imuAxes:  %s" % "".join([" %d" % x for x in self.imuAxes]))

class highPriorityData(cstruct.CStruct):
    __byte_order__ = cstruct.LITTLE_ENDIAN
    __struct__ = """
        uint16_t rpm;
        int32_t batteryShuntCurrent;
        uint32_t batteryG3Timestamp;
        int8_t  buckCurrent;
        uint16_t throttle;
     """
    def print_info(self):
        print("\nrpm: "+str(self.rpm))
        print("batteryShuntCurrent: "+str(self.batteryShuntCurrent))
        print("batteryG3Timestamp: "+str(self.batteryG3Timestamp))
        print("buckCurrent: %f"%(self.buckCurrent))
        print("throttle: "+str(self.throttle))

class normalPriorityData(cstruct.CStruct):
    __byte_order__ = cstruct.LITTLE_ENDIAN
    __struct__ = """
        uint32_t batteryG2Timestamp;
        int16_t batteryThermistorTemp[7];
        int16_t batteryIcTemp;
        int16_t batteryMosfetTemp;
        uint16_t distance;
        uint8_t   brake;
        float  coordinates[2];
    """
    def print_info(self):
        print("\nbatteryG2Timestamp: "+str(self.batteryG2Timestamp))
        print("batteryThermistorTemp:  %s" % "".join([" %d" % x for x in self.batteryThermistorTemp]))
        print("batteryIcTemp: "+str(self.batteryIcTemp))
        print("batteryMosfetTemp: "+str(self.batteryMosfetTemp))
        print("distance: "+str(self.distance))
        print("brake: "+str(self.brake))
        print("coordinates:  %s" % "".join([" %f" % x for x in self.coordinates]))

class lowPriorityData(cstruct.CStruct):
    __byte_order__ = cstruct.LITTLE_ENDIAN
    __struct__ = """
        uint32_t batteryG1Timestamp;
        uint16_t batteryCellVoltages[15];
        uint16_t batteryStackVoltage;
        float  batterySoc;
        float  batterySoh;
        float  estimatedRange;
        int32_t  vimIcTemp;
     """
    def print_info(self):
        print("\nbatteryG1Timestamp: "+str(self.batteryG1Timestamp))
        print("batteryCellVoltages:  %s" % "".join([" %d" % x for x in self.batteryCellVoltages]))
        print("batteryStackVoltage: "+str(self.batteryStackVoltage))
        print("batterySoc: %f"%(self.batterySoc))
        print("batterySoh: %f"%(self.batterySoh))
        print("vimIcTemp: "+str(self.vimIcTemp))

class veryLowPriorityData(cstruct.CStruct):
    __byte_order__ = cstruct.LITTLE_ENDIAN
    __struct__ = """
        uint32_t batteryG4Timestamp;
        uint8_t batteryChgMosStatus;
        uint8_t batteryDsgMosStatus;
        uint8_t batteryPreMosStatus;
        uint16_t batteryBalancingStatus;
     """
    def print_info(self):
        print("\nbatteryG4Timestamp: "+str(self.batteryG4Timestamp))
        print("batteryChgMosStatus: "+str(self.batteryChgMosStatus))
        print("batteryDsgMosStatus: "+str(self.batteryDsgMosStatus))
        print("batteryPreMosStatus: "+str(self.batteryPreMosStatus))
        print("batteryBalancingStatus: "+str(self.batteryBalancingStatus))


class asyncData(cstruct.CStruct):
    __byte_order__ = cstruct.LITTLE_ENDIAN
    __struct__ = """
        uint32_t timestamp;
	    uint8_t fault;
        uint8_t batteryId[20];
     """
    def print_info(self):
        print("\timestamp: "+str(self.timestamp))
        print("fault: "+str(self.fault))
        print("battery Id: " % "".join(["%c" % x for x in self.batteryId]))
