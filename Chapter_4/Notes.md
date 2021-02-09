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
# Learning Curves
![Curve for a model has under fitting](/Chapter_4/Images/Learning_Curve_For_Under_Fitting.png)  
This model has under fitting as the the error is high on the training data and also the error is much higher on the validation data.  
We can improve it by using a more **complex model** or come up with **better features**.

![Over_Fitting_Curve](/Chapter_4/Images/Over_Fitting_Curve.png)  
there is an obvious gap between the error on training set and error on validation set which indicates the the model over fits the data.   
we can solve this by **adding more training data**.  
### The Bias/Variance Tradeoff
###### Generalization error
Is a measure of how accurately an algorithm is able to predict outcome values for previously unseen data.
###### Bias
Error due to wrong assumptions, such as assuming that the data is linear when it is actually quadratic. A high-bias model is most
likely to **underfit** the training data.  
###### Variance
Error due to the model’s excessive sensitivity to small variations in the
training data. A model with many degrees of freedom (such as a high-degree polynomial model) is likely to have high variance, and thus to **overfit** the training
data.
###### Irreducible error
Error due to the noisiness of the data itself. The only way to reduce this
part of the error is to clean up the data (e.g., fix the data sources, such as broken
sensors, or detect and remove outliers)

If we add all three we get the Generalization Error.
