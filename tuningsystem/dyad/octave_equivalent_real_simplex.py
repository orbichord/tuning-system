"""Generate 8va quivalent dyad showing T^2/S_2 simplex."""


from tuningsystem.utils import plot_2d_pitch_class


#pylint: disable=invalid-name
def simplex(x):
    """Implement 2D simplex transformation."""
    x1, x2 = sorted((x[0], x[1]))
    while x1+x2 >= 1:
        tmp = x1
        x2 -= 1
        x1 = x2
        x2 = tmp
    return x1, x2


def generate_plot():
    """Generate a plot showinf continuum dyad orbichord."""

    # Plotting fundamental domain
    fundamental_domain = (
        (0.0, 0.0),
        (0.49, 0.49),
        (0.0, 0.98),
        (0.51, 0.51),
    )

    # Probe points
    probes = (
        {"label": "A", "x": (0.25, 0.75), "color": "black"},
        {"label": "B", "x": (0.50, 0.75), "color": "darkslategray"},
        {"label": "C", "x": (0.00, 0.50), "color": "red"},
        {"label": "D", "x": (0.25, 0.50), "color": "green"},
    )

    # Actions over probes
    actions = (
        (
            lambda x: (x[0], x[1]),
            lambda x: (x[0] + 1, x[1]),
            lambda x: (x[0], x[1] + 1),
            lambda x: (x[0] + 1, x[1] + 1),
            lambda x: (x[0] - 1, x[1]),
            lambda x: (x[0] - 1, x[1] + 1),
            lambda x: (x[0] - 1, x[1] - 1),
            lambda x: (x[0], x[1] - 1),
            lambda x: (x[0] + 1, x[1] - 1),
        ),
        (
            lambda x: (x[0], x[1]),
            lambda x: (x[1], x[0])
        ),
    )

    # Identification lines
    id_lines = (
        {"begin": [0, 0], "end": [0.48, 0.48], "color": "orange"},
        {"begin": [0.48, 0.48], "end": [0.96, 0], "color": "blue"},
        {"begin": [0.5, 0.5], "end": [0.98, 0.98], "color": "orange"},
        {"begin": [0.5, 0.5], "end": [1, 0], "color": "blue"},
    )

    # execute only if run as a script
    plot_2d_pitch_class(
        x_lim=[-2, 3],
        y_lim=[-3, 3],
        x_label="$\\mu$",
        y_label="$\\delta$",
        fundamental_domain=fundamental_domain,
        probes=probes,
        simplex=simplex,
        actions=actions,
        id_lines=id_lines,
        # Coordinate trasnformatiom
        transform=lambda x: (x[0]+x[1], x[1]-x[0])
    )


def main():
    """Execute script"""
    generate_plot()
