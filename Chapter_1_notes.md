# Types of machine learning systems.

**Supervised learning:** the data given to the system is labeled.

**Unsupervised learning:** the data given to the system isn't labeled.  

**Semi supervised learning:** the system can separate the data alone but needs the human supervision to give labels for the separated clusters.  

**Reinforcement learning:** it learns by positive and negative rewards.
****
**Batch learning:** the system is incapable of learning incrementally. in other words  it must be trained using all the available data. This will generally take a lot of time and computing
resources, so it is typically done offline. First the system is trained, and then it is
launched into production and runs without learning anymore; it just applies what it
has learned. This is called offline learning.
If you want a batch learning system to know about new data (such as a new type of
spam), you need to train a new version of the system from scratch on the full data set
(not just the new data, but also the old data), then stop the old system and replace it
with the new one.  

**Online learning:** you train the system incrementally by feeding it data instances
sequentially, either individually or by small groups called mini-batches. Each learning
step is fast and cheap, so the system can learn about new data on the fly, as it arrives.Online learning is great for systems that receive data as a continuous flow (e.g., stock
prices) and need to adapt to change rapidly or autonomously
****
**Instance based:** they work by simply comparing new data points to known data points.  
**Model based:** Another way to generalize from a set of examples is to build a model of these examples, then use that model to make predictions.
****
# Feature engineering
**Feature Selection:** selecting the most useful features to train among existing features

**Feature extraction:**combining existing features to produce a more useful one (as
we saw earlier,dimensionality reduction algorithms can help).
****
# Testing and Validating
**why we separate the data set into train and test sets..?**   
we do this as we want to know how well our model will generalize after training on the training data.   

**why we use validation data set..?**  
Suppose we are trying to regularize the model to avoid the over fitting, so our aim is to find best value of the hyper parameter and we did the following trying different hyper parameters then calculate the generalization error for each one finally we find the best one.  
the problem here is that we found the best model with the best hyper parameters for the test set so it's unlikely to work well when we generalize to the real world. so we divide our data set into Three parts  
**train:** where the model learn.  
**Validation:** for selecting the best hyper parameter needed for regularization.  
**test:** to test how well your model will generalize.
****
