# Mushroom AI

I have been studying deep learning and recently as of writing this received a certification. I learned in my course how 
to write a deep neural network for binary classification with a single output neuron. In future courses I will learn 
how to expand on that.

For now, I would like to implement what I have learned in a simple restful api written in python that can be used to 
identify mushrooms. My hope is that this api could be used in a colleagues mobile application.

## API outline

#### Routes

/train
- post
- receives admin key
- 


## AI outline

L layer

layer_dims_example:
layers_dims = [12288, 20, 7, 5, 1]

def initialize_parameters_deep(layer_dims):
    ...
    return parameters 
    
def L_model_forward(X, parameters):
    ...
    return AL, caches
    
def compute_cost(AL, Y):
    ...
    return cost
    
def L_model_backward(AL, Y, caches):
    ...
    return grads
    
def update_parameters(parameters, grads, learning_rate):
    ...
    return parameters