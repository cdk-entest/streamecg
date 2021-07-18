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

if __name__=="__main__":

    subscriber = streamecg.SimpleMQTTSubscriber(awshost=awshost,awsport=awsport,clienID=clientID,\
                                                thingName=thingName,caPath=caPath,certPath=certPath,\
                                                keyPath=keyPath,topic=topic,persisting_database=True)
    subscriber.receive_data()

