import jfwEncoderDecoder
import json

def main():
    # m_json = """{"vhpd": {"imuAxes": [-2222, 1, 900, 3176, -3158, 2808], "epoch": 946685729}, "hpd": {"rpm": 0, "batteryShuntCurrent": 0, "batteryG3Timestamp": 0, "buckCurrent": 0, "throttle": 0}, "npd": {"batteryG2Timestamp": 0, "batteryThermistorTemp": [0, 0, 0, 0, 0, 0, 0], "batteryIcTemp": 0, "batteryMosfetTemp": 0, "distance": 5, "brake": 0, "coordinates": [0.0, 0.0]}, "lpd": {"batteryG1Timestamp": 0, "batteryCellVoltages": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], "batteryStackVoltage": 0, "batterySoc": 0.0, "batterySoh": 0.0, "estimatedRange": 0.0, "vimIcTemp": 0}, "vlpd": {"batteryG4Timestamp": 0, "batteryChgMosStatus": 0, "batteryDsgMosStatus": 0, "batteryPreMosStatus": 0, "batteryBalancingStatus": 0}}"""
    # converting string to json 
    # final_dictionary = eval(m_json)
    # encoder = jfwEncoderDecoder.jfw_serializer.serializer(final_dictionary, len(final_dictionary))
    # pkt_data = encoder.encode()
    # decoder = jfwEncoderDecoder.jfw_deserializer.deserializer(pkt_data, len(pkt_data))
    # decoder.search()
    # ret_json = decoder.decode()
    # # print(str(ret_json))
    # if(jm_json == str(ret_json)):
    #     print("Success!")
    with open('file.json', "rb+") as f:
        lines = f.readlines()
        idx = 0
        for line in lines:
            idx += 1
            final_dictionary = json.loads(line)
            # print(type(m_json))
            # # converting string to json 
            # final_dictionary = eval(m_json)
            encoder = jfwEncoderDecoder.jfw_serializer.serializer(final_dictionary, len(final_dictionary))
            pkt_data = encoder.encode()
            decoder = jfwEncoderDecoder.jfw_deserializer.deserializer(pkt_data, len(pkt_data))
            decoder.search()
            ret_json = decoder.decode()
            # print(str(ret_json))
            if(json.dumps(final_dictionary) == str(ret_json)):
                print("Line "+str(idx)+": Success!")
            else:
                print("ERROR!!!!!!")

if __name__ == "__main__":
    main()