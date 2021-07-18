import streamecg
import numpy as np
import time

# parameters
awshost = "a209xbcpyxq5au-ats.iot.ap-southeast-1.amazonaws.com"
awsport = 8883
clientID = "testDevice"
thingName = "Test-thing"
caPath = "./../../cerfiticates/root.pem"
certPath = "./../../cerfiticates/90dd0acc83-certificate.pem.crt"
keyPath = "./../../cerfiticates/90dd0acc83-private.pem.key"
topic = "test/testing1"
chunkSize =  500
samplingRate  = 500

def test_publish_ecg_data():
    # publisher
    publisher = streamecg.SimpleMQTTPublisher(awshost=awshost,awsport=awsport,clientID=clientID,\
                                              thingName=thingName,caPath=caPath,certPath=certPath,
                                              keyPath=keyPath,topic=topic)
    # ecg data
    print("load ecg data...")
    ecg = np.loadtxt("./../../data/1018ssa.csv", delimiter=',', dtype=float)
    ecg = ecg[:, 1]
    ecg = ecg / (1.1 * np.max(np.abs(ecg)))
    ecg = np.array(32767 * ecg, np.int16)

    # send data
    print("sending data...")
    for k in range(len(ecg) // chunkSize):
        data = ecg[k * chunkSize:(k + 1) * chunkSize]
        data = data.tobytes()
        publisher.send_data(data)
        time.sleep(1)

if __name__=="__main__":
    test_publish_ecg_data()