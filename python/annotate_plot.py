"""
Annotate a plot using matplotlib text.
"""

__author__ = "Nolan Bahr"

from datetime import date

import numpy as np
import matplotlib.pyplot as plt


def annotate_plot(annotations):
    """
    Add text annotations to a plot.

    Parameters:
        annotations: dict
            Dictionary containing text labels and annotation settings.

    Returns:
        annotation_objects: list
            List of text annotation objects.
    """
    required_keys = ["position", "alignment", "fontsize"]
    annotation_objects = []

    for label, settings in annotations.items():
        for key in required_keys:
            if key not in settings:
                raise KeyError(f"Missing required annotation key: {key}")

        position = settings["position"]
        alignment = settings["alignment"]
        fontsize = settings["fontsize"]

        annotation = plt.text(
            position[0],
            position[1],
            label,
            horizontalalignment=alignment[0],
            verticalalignment=alignment[1],
            fontsize=fontsize,
            transform=plt.gca().transAxes
        )

        annotation_objects.append(annotation)

    return annotation_objects


if __name__ == "__main__":
    x_values = np.linspace(-2, 2)
    y_values = x_values**2

    plt.plot(x_values, y_values)
    plt.xlabel("x")
    plt.ylabel("y")

    today = date.today().isoformat()
    signature = f"Created by Nolan Bahr {today}"

    annotations = {
        signature: {
            "position": np.array([0.0, -0.18]),
            "alignment": ("left", "top"),
            "fontsize": 10
        }
    }

    annotation_objects = annotate_plot(annotations)
    print(f"{annotation_objects=}")

    plt.show()