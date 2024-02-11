
Vector = list[float]
def add(v: list[float], w: list[float]) -> list[float]:
    """ Add corresponding elements"""
    assert len(v) == len(w) # Vectors must be of the same length
    return [v_i + w_i for v_i , w_i in zip(v,w)]

def sub(v: list[float], w: list[float]) -> list[float]:
    """ Subtract corresponding elements """
    assert len(v) == len(w) # Vectors must be of same length 
    return [v_i - w_i for v_i,w_i in zip(v,w)]

def vector_sum(vectors  : list[list[float]]) -> list[float]:
    """ Sums all the corresponding elements  """
    # Check if vectors is empty or not
    assert vectors, "no Vectors provided!"

    # Check if all Vectors are of same size 
    num_elemnts = len(vectors[0])
    assert all( len(v) == num_elemnts for v in vectors), "Different size vectors provided"

    # For i-th element of the result is the sum of every vector[i]
    return [sum(vector[i] for vector in vectors) 
            for i in range(num_elemnts)]

def scalar_multiply( c: float, v:list[float]) -> list[float]:
    """ Multiplies every element by c"""

    # Check if vector is empty
    assert v, "Vector is empty!"

    return [c * v_i for v_i in v]

def vector_mean( vectors: list[list[float]]) -> list[float]:
    """ Computes the element-wise average"""
    n = len(vectors)
    return scalar_multiply(1/n,vector_sum(vectors))

def dot(v:list[float], w:list[float]) -> float:
    """  Computes the dot product for 2 vectors"""
    assert len(v) == len(w), "Vectors are not of same size!"

    return sum( v_i * w_i for v_i, w_i in zip(v,w))

def sum_of_squares(v:list[float]) -> float:
    """ Calculates the sum of squares for a given Vector"""
    return dot(v,v)

def magnitude(v:list[float]) ->float:
    """ Returns the magnitude or the length of v"""
    import math
    return math.sqrt(sum_of_squares(v))

def squared_distance(v: list[float] , w: list[float]) -> float:
    """ Computes (v_1 - w_1) **2 + .... (v_n -w_n) **2"""
    return sum_of_squares(sub(v,w))

def distance(v: list[float], w:list[float]) -> float:
    """ Computes the distance between v and w """
    import math
    return math.sqrt(squared_distance(v,w))

def distance_better(v:list[float],w:list[float]) -> float:
    """ Computes the distance between v and w """
    return magnitude(sub(v,w))