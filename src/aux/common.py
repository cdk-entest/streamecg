import numpy as np

def readFromBinary(path, dtype=np.int16):

    # open binary data file
    with open(path,"rb") as file:
        data = file.read()

    # convert to numpy array
    data = np.frombuffer(data,dtype=dtype)

    # return
    return data