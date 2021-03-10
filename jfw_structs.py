import cstruct

class veryHighPriorityData_t(cstruct.CStruct):
    __byte_order__ = cstruct.LITTLE_ENDIAN
    __struct__ =""" 
       int16_t imuAxes[6];
       uint32_t epoch;
       """

    def get_dict(self):
        m_json = {}
        m_json['imuAxes'] = self.imuAxes
        m_json['epoch'] = self.epoch
        return m_json

class highPriorityData_t(cstruct.CStruct):
    __byte_order__ = cstruct.LITTLE_ENDIAN
    __struct__ =""" 
       uint16_t rpm;
       int32_t batteryShuntCurrent;
       uint32_t batteryG3Timestamp;
       int8_t buckCurrent;
       uint16_t throttle;
       """

    def get_dict(self):
        m_json = {}
        m_json['rpm'] = self.rpm
        m_json['batteryShuntCurrent'] = self.batteryShuntCurrent
        m_json['batteryG3Timestamp'] = self.batteryG3Timestamp
        m_json['buckCurrent'] = self.buckCurrent
        m_json['throttle'] = self.throttle
        return m_json

class normalPriorityData_t(cstruct.CStruct):
    __byte_order__ = cstruct.LITTLE_ENDIAN
    __struct__ =""" 
       uint32_t batteryG2Timestamp;
       int16_t batteryThermistorTemp[7];
       int16_t batteryIcTemp;
       int16_t batteryMosfetTemp;
       uint16_t distance;
       uint8_t brake;
       float coordinates[2];
       """

    def get_dict(self):
        m_json = {}
        m_json['batteryG2Timestamp'] = self.batteryG2Timestamp
        m_json['batteryThermistorTemp'] = self.batteryThermistorTemp
        m_json['batteryIcTemp'] = self.batteryIcTemp
        m_json['batteryMosfetTemp'] = self.batteryMosfetTemp
        m_json['distance'] = self.distance
        m_json['brake'] = self.brake
        m_json['coordinates'] = self.coordinates
        return m_json

class lowPriorityData_t(cstruct.CStruct):
    __byte_order__ = cstruct.LITTLE_ENDIAN
    __struct__ =""" 
       uint32_t batteryG1Timestamp;
       uint16_t batteryCellVoltages[15];
       uint16_t batteryStackVoltage;
       float batterySoc;
       float batterySoh;
       float estimatedRange;
       int32_t vimIcTemp;
       """

    def get_dict(self):
        m_json = {}
        m_json['batteryG1Timestamp'] = self.batteryG1Timestamp
        m_json['batteryCellVoltages'] = self.batteryCellVoltages
        m_json['batteryStackVoltage'] = self.batteryStackVoltage
        m_json['batterySoc'] = self.batterySoc
        m_json['batterySoh'] = self.batterySoh
        m_json['estimatedRange'] = self.estimatedRange
        m_json['vimIcTemp'] = self.vimIcTemp
        return m_json

class veryLowPriorityData_t(cstruct.CStruct):
    __byte_order__ = cstruct.LITTLE_ENDIAN
    __struct__ =""" 
       uint32_t batteryG4Timestamp;
       uint8_t batteryChgMosStatus;
       uint8_t batteryDsgMosStatus;
       uint8_t batteryPreMosStatus;
       uint16_t batteryBalancingStatus;
       """

    def get_dict(self):
        m_json = {}
        m_json['batteryG4Timestamp'] = self.batteryG4Timestamp
        m_json['batteryChgMosStatus'] = self.batteryChgMosStatus
        m_json['batteryDsgMosStatus'] = self.batteryDsgMosStatus
        m_json['batteryPreMosStatus'] = self.batteryPreMosStatus
        m_json['batteryBalancingStatus'] = self.batteryBalancingStatus
        return m_json

class asyncData_t(cstruct.CStruct):
    __byte_order__ = cstruct.LITTLE_ENDIAN
    __struct__ =""" 
       uint32_t timestamp;
       uint8_t fault;
       uint8_t batteryId[20];
       """

    def get_dict(self):
        m_json = {}
        m_json['timestamp'] = self.timestamp
        m_json['fault'] = self.fault
        m_json['batteryId'] = self.batteryId
        return m_json
