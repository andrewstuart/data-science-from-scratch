def v_add(v, w):
    """Add two vectors

    :v: List 2
    :w: List 1
    :returns: A new vector

    """
    if len(v) != len(w):
        raise Exception('Illegal vector addition')

    return [vi + wi
            for vi, wi in zip(v, w)]


def v_sub(v, w):
    """Subtracts two vectors

    :v: List 1
    :w: List 2
    :returns: List of subtracted vectors

    """
    return [vi - wi
            for vi, wi in zip(v, w)]

def v_sum(vectors):
    """Sums some vectors

    :vectors: A list of vectors.
    :returns: A single reduced vector.

    """
    result = vectors[0]
    for v in vectors[1:]:
        result = v_add(result, v)

    return result

def scalar_multiply(v, s):
    """Multiply a vector by a scalar

    :v: @todo
    :s: @todo
    :returns: @todo

    """
    return [vi * s for vi in v]

def v_mean(vectors):
    """Compute the vector whos ith element is the mean of the ith elements of
    the input vectors

    :v: List of vectors
    :returns: list

    """

    n = len(vectors)
    return scalar_multiply(v_sum(vectors), 1/n)
