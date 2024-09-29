"""Tool to generate 8va quotient continuum dyad."""


from tuningsystem.utils import plot_2d_pitch_class


def generate_plot():
    """Generate a plot showinf continuum dyad orbichord."""

    # Plotting fundamental domain
    fundamental_domain = (
        (0, 0), (0, 1), (1, 1)
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
        {"begin": [0, 0], "end": [0, 1], "color": "blue"},
        {"begin": [1, 0], "end": [1, 1], "color": "blue"},
        {"begin": [0, 0], "end": [1, 0], "color": "blue"},
        {"begin": [0, 1], "end": [1, 1], "color": "blue"},
        {"begin": [0, 0], "end": [1, 1], "color": "orange"},
    )

    # execute only if run as a script
    plot_2d_pitch_class(
        x_lim=[-2, 4],
        y_lim=[-3, 3],
        x_label="$\\mu$",
        y_label="$\\delta$",
        fundamental_domain=fundamental_domain,
        probes=probes,
        actions=actions,
        id_lines=id_lines,
        # Coordinate trasnformatiom
        transform=lambda x: (x[0]+x[1], x[1]-x[0])
    )


def main():
    """Execute script"""
    generate_plot()
