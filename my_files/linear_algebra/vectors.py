
from typing import List
import math

Vector = List[float]

height_weight_age = [70, 170, 40]
grades = [95, 80, 75, 62]

def add(v: Vector, w:Vector):
    """Adds corresponding elements"""
    assert(len(v) == len(w)), "Vector must be same length"
    return [v_i + w_i for v_i, w_i in zip(v,w)]


def subtract(v:Vector, w: Vector) -> Vector:
    """Subtracts corresponding elements"""
    assert(len(v) == len(w))
    return [v_i - w_i for v_i, w_i in zip(v,w)]


def vector_sum(vectors: List[Vector]) -> Vector:
    """Sums all corresponding elements"""
    num_elements = len(vectors[0])
    assert all(len(v) == num_elements for v in vectors)
    return [sum(vector[i] for vector in vectors)
            for i in range(num_elements)]

def scalar_multiply(s:float, v:Vector) -> Vector:
    """Multiply a vector by a scalar"""
    return [s * v_i for v_i in v]

def vector_mean(vectors: List[Vector]) -> Vector:
    """Takes the average of a list of vectors."""
    num_elements = len(vectors[0])
    assert all(len(v) == num_elements for v in vectors), \
    "Vectors must be the same length"
    n = len(vectors)
    return scalar_multiply(1/n, vector_sum(vectors))



def dot_product(v:Vector, w: Vector) -> float:
    """Computes v_1 * w_1 + ... + v_n + w_n
        also know as the dot product. """
    assert(len(v) == len(w)), "Vectors must be the same length"
    return sum(v_i * w_i for v_i, w_i in zip(v,w))


def sum_of_squares(v: Vector) -> float:
    """Return v_1 * v_1 + ... + v_n * w_n"""
    return dot_product(v, v)

#magnitude = length
def magnitude(v: Vector) -> float:
    """Returns the magnitude(length) of a vector"""
    return math.sqrt(sum_of_squares))


v1 = [2,3,4]
v2 = [4,5,6]
v3 = [7,8,9,10]
v4 = [7,8,9]
print(add(v1,v2))
print(subtract(v1, v2))
# print(vector_mean([v1,v2,v3]))
print(vector_mean([v1,v2,v4]))
assert(add(v1,v2) == [6,8,10])
