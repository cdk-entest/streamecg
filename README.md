# An Algorithm for Real time Electrocardiography Processing 

**Summary**

- Stream Electrocardiography (ECG) from local PC to an EC2 via pub/sub MQTT protocol
- Signal is processed in window basic to output clean ECG waveform and heart rate values in real time 
- Implemented an algorithm [reference paper](http://cinc.mit.edu/archives/2011/pdf/0625.pdf) to calcluate heart rate from ECG signal 
- [video demo](https://haitran-swincoffee-demo.s3.ap-southeast-1.amazonaws.com/ECG_STREAMING_PROCESSING.mp4)

**Signal Processing Diagram**
