from dataclasses import dataclass


@dataclass
class Point:
    x: float
    y: float


def manhattan_distance(p1: Point, p2: Point) -> float:
    """Computes the Manhattan Distance between two 2D points."""

    return abs(p1.x - p2.x) + abs(p1.y - p2.y)


def euclidean_distance(p1: Point, p2: Point) -> float:
    """Computes the Euclidean Distance between two 2D points."""

    return ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** 0.5


def minkowski_distance(p1: Point, p2: Point, p: float) -> float:
    """Computes the Minkowski Distance between two 2D points."""

    return (abs(p1.x - p2.x) ** p + abs(p1.y - p2.y) ** p) ** (1 / p)


def chebyshev_distance(p1: Point, p2: Point) -> float:
    """Computes the Chebyshev Distance between two 2D points."""

    return max(abs(p1.x - p2.x), abs(p1.y - p2.y))
