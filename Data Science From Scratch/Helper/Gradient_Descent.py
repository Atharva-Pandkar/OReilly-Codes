Vector = list[float]
def sum_of_squares(v: Vector) -> float:
    """ Computes the Sum of Squared elements in v """
    from Helper.Linear_Algebra import dot
    return dot(v,v)

from typing import Callable
def partial_difference_quotient(f: Callable[[Vector], float],
                                v: Vector,
                                i: int,
                                h: float) -> float:
    """ Returns the i-th partial difference quotient of f at v """
    w = [v_j + (h if j == i else 0) # add h to just the ith element of v
         for j, v_j in enumerate(v)]
    
    return (f(w) - f(v)) /h

def estimate_gradient( f: Callable[[Vector], float],
                      v: Vector, 
                      h: float = 0.0001):
    
    return [partial_difference_quotient(f, v, i, h) for i in range(len(v))]

from Helper.Linear_Algebra import distance, add, scalar_multiply
import random

def gradient_step(v: Vector, gradient: Vector, step_size: float) -> Vector:
    """  Moves 'step_size in the 'gradient' direction from v"""

    assert len(v) == len(gradient)
    step = scalar_multiply(step_size, gradient)
    return add(v, step)

def sum_of_squares_gradient(v: Vector) -> Vector:
    return [2 * v_i for v_i in v]

# pick a random starting point
v = [random.uniform(-10,10) for i in range(3)]
print(v)
for epoch in range(1000):
    grad = sum_of_squares_gradient(v)  # Compute the gradient at v
    v = gradient_step(v, grad, -0.01)
    print(epoch, v)

assert distance(v, [0,0,0]) < 0.001 # v should be close to 0

def linear_gradient(x: float, y:float, theta: Vector) -> Vector:
    slope, intercept = theta
    predicted = slope * x + intercept # The prediction of the model.
    error = (predicted - y)  # error is (predicted - actual)
    squared_error = error ** 2 # We will minimize the squared error
    grad = [ 2 * error * x, 2 * error] # using its gradient 
    return grad

from typing import TypeVar, List, Iterator

T = TypeVar('T')  # This allows us to type "generic" functions

def minibatches(dataset: List[T],
                batch_size: int,
                shuffle: bool = True) -> Iterator[List[T]]:
    """  Generates 'batch_size' -sized minibatches from the dataset"""
    # start indexes 0, batch_size, 2 * batch_size, .....
    batch_starts = [ start for start in range(0, len(dataset),batch_size)]

    if shuffle: random.shuffle(batch_starts) # Shuffle the batches
    for start in batch_starts:
        end = start + batch_size
        yield dataset[start:end]