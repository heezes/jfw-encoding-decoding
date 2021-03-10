import jfw_deserializer
import json

binaryFilePath = "3014693-893931545-540029520-3732.bin"
with open(binaryFilePath, "rb") as f:
    data = f.read()
    ser = jfw_deserializer.serializer(data, len(data))
    ser.search()
    temp = list()
    while(ser.decode_idx < len(ser.sync_char_off)):
        final_json = ser.decode(False)
        if(final_json != None):
            temp.append(json.loads(final_json))
print("Data Lost: "+ser.loss())
