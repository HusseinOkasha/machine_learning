# Linear Regression  
![Linear_Regression_model_prediction_equation](/Chapter_4/Images/Linear_Regression_model_prediction.png)

![MSE_for_cost_function](/Chapter_4/Images/MSE_Equation.png)

### Normal Equation
Is a closed form of the MSE equation (Simplified)  
![MSE_for_cost_function](/Chapter_4/Images/Normal_Equation.png)

### Gradient_Descent
The general idea of Gradient Descent is to
tweak parameters iteratively in order to minimize a cost function
##### Batch Gradient_Descent
it uses the whole training set to compute the gradients at every step.
it optimal solution but with low speed.
##### Stochastic Gradient Descent
it uses a random instance of the training data and use it to calculate the next step,this makes the algorithm much faster.
Unlike Batch Gradient descent this algorithm makes the cost function bounce up and down decreasing on average. It will not settle down when it reach local minimum or global minimum but it will move around it giving good solution but not the optimal one.  
Also it has better chance to find the global minimum due to it's random nature.
##### Mini Batch Gradient_Descent
it takes small random sets of instance from the training set each iteration. it's advantage over the SGD is that it will end walking closer to the minimum ,But on the other hand it may be harder for it to escape from local minima and find the global minimum.
![BGD & SGD & MBSGD](/Chapter_4/Images/BGD&SGD&MBSGD.png)       

**Regression:** means predicting values.
