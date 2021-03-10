from jfwEncoderDecoder import jfw_structs
from jfwEncoderDecoder import jfw_common
import cstruct
import json


class serializer():
    def __init__(self, buf, len):
        self.buf = buf
        self.max_size = len
        self.sync_char = [0xb5, 0x62]
        self.common = jfw_common.jfw()
    
    def encode(self, debug = False):
        try:
            temp_data = json.loads(self.buf)
            msg_id = 0
            pkt_size = 0
            pkt = []
            pkt_data = []
            for i in range(0,2):
                pkt.append(self.sync_char[i])
            fundamental_structures = list(6)
            fundamental_structures[0] = jfw_structs.veryHighPriorityData_t()
            fundamental_structures[1] = jfw_structs.highPriorityData_t()
            fundamental_structures[2] = jfw_structs.normalPriorityData_t()
            fundamental_structures[3] = jfw_structs.lowPriorityData_t()
            fundamental_structures[4] = jfw_structs.veryLowPriorityData_t()
            fundamental_structures[5] = jfw_structs.asyncData_t()
            for i in range(0, len(self.common.fundamental_structs)):
                if self.common.fundamental_structs[i][0] in temp_data:
                    msg_id          |=  self.common.fundamental_structs[i][1]
                    pkt_size        +=  fundamental_structures[i].size()
                    fundamental_structures[i].get_binary(temp_data[str(self.common.fundamental_structs[i][0])])
                    # temp_data       =   fundamental_structures[i].pack()
                    pkt_data.append(fundamental_structures[i].pack())
            pkt.append()#Append Length uint16_t data to be broken and stored as uint8_t
            pkt.append(msg_id)#Msg Id
            checksum = self.common.calcultate_checksum(pkt_data, len(pkt_data))
            pkt.append(pkt_data)
            for i in range(0,2):
                pkt.append(checksum[i])
            return pkt
        except:
            pass