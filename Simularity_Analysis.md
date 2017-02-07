# Simularity Analysis
## Artificial Intelligence For Predictive Maintenance, Event Prediction, and Anomaly Detection
It creates a multivariate and complex view of the world based on the data it ingests and is able to do temporal reasoning, and learning on the fly, _without models to train and deploy, nor rules to create._

Simularity uses machine learning and statistical probabilities to learn what “normal” looks like in any time series data set.

## Predictive Maintenance
### eg. Hard Drive failure predictor

**INPUT** 

- Sensor data : 53 different sensors on the hard drives
- Sample set of failed drives
- Sample set of normal drives

**OUTPUT**

- A Time Series Predictive Archetype for hard drive failures

Monitors all sensors on all live drives in real time, and score them, determining whether or not they will fail, how soon we expect them to fail, and what type of failure it might be.

Dashboard indicates the real time status of the drives, and flags those that are showing signs of failure.

## Anomaly Detection
Simularity can find anomalies in logs and more effectively manage the data center.

## Real Time Deep Learning To The Edges Of The Internet Of Things
They are effectively doing real time deep learning on massive amounts of time series data. Automatically learn normal individual sensor behavior, including both short and long term cyclic behavior**(!!!)**.

Combination of Convolutional Neural Networks, Self Organizing maps, Clustering algorithms, statistical correlation and similarity measurements and symbolic representation.

**(!!!)** Here we can think of applying a LSTM(Long short term model) model to each sensor to identify both short and long term cyclic patterns and mark anomalous behaviour.

## Technology Used
![Image](http://simularity.com/wp-content/uploads/2015/05/technology-platform.png)


### Ideas Extracted:

- For real time predictive diagnosis a seperate LSTM model can be trained for each sensor which can monitor the state of that sensor.
- For rule generation other models need to be learned and patterns need to be extracted.
