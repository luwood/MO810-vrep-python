from math import pi
from math import isclose

limit = 2 * pi


def calculateDelta(start, end, spinRightOrientation: bool = True):
    """
    Given a start position, an end position and the orientation of the spin, calculates the absolute delta angle.
    Note: only able to calculate delta in 360 universe. 
    :param start: the start position in radians [180, -180[
    :param end: the end position in radians [180, -180[
    :param spinRightOrientation: if the spin is turning right this should be True
    :return: the absolute delta difference
    """
    if isclose(end, start, abs_tol=0.1):
        return 0

    end = convertNegativePiUniverseTo360(end)
    start = convertNegativePiUniverseTo360(start)

    ans = abs(end - start)
    if spinRightOrientation:
        if start < end:
            return limit - ans
        return ans
    if start > end:
        return limit - ans
    return ans


def addDelta(start, delta):
    """
    Given a start position and a delta, calculates the end position in the universe [180,-180[. 
    :param start: the start position in radians [180,-180[
    :param delta: the delta in radians
    :return: the end position in radians [180,-180[
    """
    ans = (start + delta) % limit
    if ans > pi:
        return ans - limit
    return ans


def convertNegativePiUniverseTo360(angle):
    return (limit + angle) % limit