#!/usr/bin/env python
import matplotlib.pyplot as plt

from distance_functions.dist2d import Point
from distance_functions.dist2d import (
    manhattan_distance,
    euclidean_distance,
    minkowski_distance,
    chebyshev_distance,
)

plt.style.use("tableau-colorblind10")


def main() -> None:
    """Experimenting with distance functions."""

    p1, p2 = Point(1, 2), Point(4, 6)

    manhattan_distval = manhattan_distance(p1, p2)
    euclidean_distval = euclidean_distance(p1, p2)
    minkowski_distval = minkowski_distance(p1, p2, p=3)
    chebyshev_distval = chebyshev_distance(p1, p2)

    fig, axs = plt.subplots(
        nrows=2,
        ncols=2,
        figsize=(16, 8),
        gridspec_kw={"hspace": 0.4, "wspace": 0.2},
    )

    axs[0][0].grid()
    axs[0][0].set_title("Manhattan Distance: $|x1 - x2| + |y1 - y2|$", fontsize=16)
    axs[0][0].scatter([p1.x, p2.x], [p1.y, p2.y], c="darkblue", linewidth=2.0)
    axs[0][0].annotate(f"$|1 - 4| + |2 - 6| = 3 + 4 = {manhattan_distval:.1f}$", xy=(1.125, 4.25))
    axs[0][0].plot([p1.x, p2.x], [p1.y, p2.y], c="tomato", linewidth=2.0)

    axs[0][1].grid()
    axs[0][1].set_title("Euclidean Distance: $\sqrt{(x1 - x2)^2 + (y1 - y2)^2}$", fontsize=16)
    axs[0][1].scatter([p1.x, p2.x], [p1.y, p2.y], c="darkblue", linewidth=2.0)
    axs[0][1].annotate(
        f"$\sqrt{{(1 - 4)^2 + (2 - 6)^2}} = \sqrt{{25}} = {euclidean_distval:.1f}$",
        xy=(1.125, 4.25),
    )
    axs[0][1].plot([p1.x, p2.x], [p1.y, p2.y], c="tomato", linewidth=2.0)

    axs[1][0].grid()
    axs[1][0].set_title("Minkowski Distance ($p=3$): $(|x1 - x2|^3 + |y1 - y2|)^3$", fontsize=16)
    axs[1][0].scatter([p1.x, p2.x], [p1.y, p2.y], c="darkblue", linewidth=2.0)
    axs[1][0].annotate(
        f"$(|1 - 4|^4 + |2 - 6|^4)^{{1/3}} = (3 + 4)^{{1/3}} = {minkowski_distval:.1f}$",
        xy=(1.125, 4.25),
    )
    axs[1][0].plot([p1.x, p2.x], [p1.y, p2.y], c="tomato", linewidth=2.0)

    axs[1][1].grid()
    axs[1][1].set_title("Chebyshev Distance: $\max{(|x1 - x2|, |y1 - y2|)}$", fontsize=16)
    axs[1][1].scatter([p1.x, p2.x], [p1.y, p2.y], c="darkblue", linewidth=2.0)
    axs[1][1].annotate(
        f"$\max{{(|1 - 4|, |2 - 6|)}} = \max{{(3, 4)}} = {chebyshev_distval:.1f}$",
        xy=(1.125, 4.25),
    )
    axs[1][1].plot([p1.x, p2.x], [p1.y, p2.y], c="tomato", linewidth=2.0)

    plt.savefig("image/distance_functions.png", bbox_inches="tight")


if __name__ == "__main__":
    main()
