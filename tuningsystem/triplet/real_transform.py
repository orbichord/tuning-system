"""Tool to generate a real triple cut."""


from tuningsystem.utils import plot_2d_pitch_class


def generate_plot():
    """Generate a plot showing expmap orbichord
    after applying affine transformation.
    """
    # Size of the coordinates
    limit = 4

    # Plotting fundamental domain
    fundamental_domain = (
        (0, 0, 0),
        (0, 0, limit),
        (-limit, 0, limit),
        (0, limit, limit),
    )

    # Probe points
    probes = (
        {
            "label": "A",
            "x": (0.5, 1.0, 2.0),
            "color": "black",
        },
    )

    # Action over probes
    actions = ((
        lambda x: (x[0], x[1], x[2]),
        lambda x: (x[1], x[0], x[2]),
        lambda x: (x[0], x[2], x[1]),
        lambda x: (x[2], x[1], x[0]),
        lambda x: (x[2], x[0], x[1]),
        lambda x: (x[1], x[2], x[0]),
    ),)

    # execute only if run as a script
    plot_2d_pitch_class(
        x_lim=(-limit, limit),
        y_lim=(-limit, limit),
        x_label="$\\delta_{21}$",
        y_label="$\\delta_{32}$",
        fundamental_domain=fundamental_domain,
        probes=probes,
        actions=actions,
        transform=lambda x: (x[1]-x[0], x[2]-x[1])
    )


def main():
    """Execute script"""
    generate_plot()
