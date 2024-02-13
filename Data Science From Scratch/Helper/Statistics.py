def _median_odd(xs : list[float]) -> float:
    """ 
    This function is not supposed to be called by other user's but the program itself
    Takes in the list and returns the median. 
    The median would be the middle value
    """
    return sorted(xs)[len(xs)//2]

def _median_even(xs : list[float]) -> float:
    """
    This function is not supposed to be called by other user's but the program itself
    Takes in the list and returns the median. 
    The median would be the average of the middle two values
    """
    hi_midpoint = len(xs) //2
    return (sorted(xs)[hi_midpoint -1] + sorted(xs)[hi_midpoint])/2

def median( v : list[float]) -> float:
    """ 
    This Function calculates the meadian irrespectative of wether It has odd numbers or elements or even
    """
    return _median_even(v) if len(v) % 2 ==0 else _median_odd(v)

def quantile(xs : list[float], p:float) -> float:
    """ 
    This function returns the Pth Percentile value in a list x
    """
    p_index = int(p * len(xs))
    return sorted(xs)[p_index]

def mode(xs: list[float]) -> float:
    """ 
    Returns the mode of the given list xs
    """
    from collections import Counter
    counts = Counter(xs)
    max_count = max(counts.values())
    return [x_i for x_i, count in counts.items() if count == max_count]

def mean(xs: list[float]) -> float:
    """ Calculate the mean for a given list """
    return sum(xs) / len(xs)

def de_mean(xs: list[float]) -> float:
    """ Translate xs by subtracting its mean (so the result has 0 mean) """
    x_bar = mean(xs)
    return [x - x_bar for x in xs]

def variance(xs: list[float]) -> float:
    """ Almost the average squared deviations from the mean """
    assert len(xs) >= 2," Variance at least require 2 elements "
    from Helper.Linear_Algebra import sum_of_squares
    n = len(xs)
    deviations = de_mean(xs)
    return sum_of_squares(deviations) / (n-1)

def standard_deviations(xs: list[float]) -> float:
    """ The standard deviations is the square root of the variance """
    import math
    return math.sqrt(variance(xs))

def interquartile_range(xs: list[float]) -> float:
    """ Returns the difference between the 75%-ile & the 25%-ile """
    return quantile(xs,0.75) - quantile(xs,0.25)

def covariance(xs: list[float], ys: list[float]) -> float:
    assert len(xs) == len(ys), "The length of both List should be the same"
    import Linear_Algebra
    return Linear_Algebra.dot(de_mean(xs),de_mean(ys))/ (len(xs)-1)

def correlations(xs:list[float], ys:list[float] ) -> float:
    """ Measures how much xs & ys vary in tandem about their means """
    stdev_x = standard_deviations(xs)
    stdev_y = standard_deviations(ys)

    if stdev_x > 0 and stdev_y >0:
        return covariance(xs,ys) /stdev_x/stdev_y
    else:
        return 0 # If no relation, Covariance is 0