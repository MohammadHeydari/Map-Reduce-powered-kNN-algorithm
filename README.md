### Bare bones Map Reduce implementation of k-NN algorithm

#### Story

Created a simple implementation of k-NN algorithm as a part of academic project. k-NN is a simple algorithm that works on the basis of *similarity* between two data points. Its very useful as a part of recommendations and price predictions based on similarity. Common similarity calculations include 
  1.  Eucledian distance
  2.  Manhattan distance
  3.  Hamming distance

Its a lazy learning algorithm - meaning the data point in the question needs to be compared with all points in the data space. Distance calculations is a computationally intensive aspect concerning this [approach](https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm). 
  
An interesting use case was presented in the book [Programming Collective Intelligence](http://www.amazon.com/Programming-Collective-Intelligence-Building-Applications/dp/0596529325/ref=sr_1_1?s=books&ie=UTF8&qid=1458027123&sr=1-1&keywords=programming+collective+intelligence) wherein price modelling was done for an incoming product based on a attribute comparison with existing electronic inventory. 

#### Design

The processing intensive nature makes it an excellent candidate for Map-Reduce paradigm. Over all map reduce design is as follows:
  1.  *Mapper*  - Compute Eucledian Distance
  2.  *Reducer* - Sort the distances and predict the price using k-closest neighbors
  
A wrapper script collects :
  1.  Feature inputs from the user for the new datapoint to which the price needs to be predicted based on existing data points
  2.  Choice of k for prediction (This is dependent on data and business context)
  
#### Behavior

A Sample Interaction with application is given below:
![Results](https://github.com/vizkids/Map-Reduce-K-NN/blob/master/Results.JPG)

 #### Whats in the package ?
 
1.  Reference data - referene\_knn\_dataset.csv
    It contains sample inventory features of laptop datasets retrieved from eBay as comma seperated values.
    It is treated as reference data points for computing distances. 
    The features are in order *hard disk space,RAM,processor speed,price*

2.  Mapper Script - mapper.py
3.  Reducer Script - reducer.py
4.  Wrapper Script - wrapper.py


##### Other Info
* Currently this program is designed for Linux distros
* Does **not** contain information about the pulling data from eBay. It could be referenced from the book
* Its written in Python and uses Hadoop 2.7 streaming libraries
