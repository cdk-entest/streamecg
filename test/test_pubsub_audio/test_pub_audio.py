import streamecg

# parameters
awshost = "a209xbcpyxq5au-ats.iot.ap-southeast-1.amazonaws.com"
awsport = 8883
clientID = "testDevice"
thingName = "Test-thing"
caPath = "./../../cerfiticates/root.pem"
certPath = "./../../cerfiticates/90dd0acc83-certificate.pem.crt"
keyPath = "./../../cerfiticates/90dd0acc83-private.pem.key"
topic = "test/testing1"
chunkSize =  8000
samplingRate  = 8000

def test_publish_audio_data():
    # logLevel
    logLevel = 0
    # publisher
    publisher = streamecg.SimpleMQTTPublisher(awshost=awshost,awsport=awsport,clientID=clientID,\
                                              thingName=thingName,caPath=caPath,certPath=certPath,
                                              keyPath=keyPath,topic=topic)
    # audio data
    audio = streamecg.AudioRecorder(chunkSize=chunkSize, samplingRate=samplingRate)
    # send data
    # log data for compare
    if logLevel == 1:
        with open("datalocal.txt", "wb") as file:
            pass
    while True:
        # get a chunk of data
        data = audio.record()
        # convert to byte array
        data = data.tobytes()
        # send data
        publisher.send_data(data)
        # log data
        if logLevel == 1:
            with open("datalocal.txt", "ab") as file:
                file.write(data)

if __name__=="__main__":
    test_publish_audio_data()