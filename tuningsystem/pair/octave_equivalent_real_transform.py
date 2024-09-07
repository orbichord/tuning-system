"""Explore 8va equivalent real pair tuning system."""


from tuningsystem.utils import plot_2d_pitch_class


def generate_plot():
    """Generate a plot showinf continuum dyad orbichord."""
    # Size of the coordinates

    limit = 2

    # Plotting fundamental domain
    fundamental_domain = (
        (0, 0), (0, 1), (1, 1), (1, 0),
    )

    # Probe points
    probes = (
        {"label": "A", "x": (0.25, 0.75), "color": "black"},
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
    )

    # Identification lines
    id_lines = (
        {"begin": [0, 0], "end": [0, 1], "color": "blue"},
        {"begin": [1, 0], "end": [1, 1], "color": "blue"},
        {"begin": [0, 0], "end": [1, 0], "color": "blue"},
        {"begin": [0, 1], "end": [1, 1], "color": "blue"},
    )

    # execute only if run as a script
    plot_2d_pitch_class(
        x_lim=[-2, 4],
        y_lim=[-3, 3],
        x_label="$\\Sigma$",
        y_label="$\\Delta_{21}$",
        fundamental_domain=fundamental_domain,
        probes=probes,
        actions=actions,
        id_lines=id_lines,
        transform=lambda x: (x[0]+x[1], x[1]-x[0]),
    )


def main():
    generate_plot()
