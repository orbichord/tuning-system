"""Tool to generate real dyad."""


from tuningsystem.utils import plot_2d_pitch_class


def generate_plot():
    """Generate a plot showinf continuum dyad orbichord."""
    # Size of the coordinates
    limit = 2

    # Plotting fundamental domain
    fundamental_domain = (
        (-limit, -limit),
        (-limit, limit),
        (limit, limit),
    )

    # Probe points
    probes = (
        {
            "label": "A",
            "x": (0.25, 0.75),
            "color": "black"
        },
    )

    # Action over probes
    actions = ((lambda x: (x[0], x[1]), lambda x: (x[1], x[0])),)

    # Identification lines
    id_lines = ({"begin": [-limit, -limit], "end": [limit, limit], "color": "blue"},)

    # execute only if run as a script
    plot_2d_pitch_class(
        x_lim=[-limit, limit],
        y_lim=[-limit, limit],
        x_label="$g_1$",
        y_label="$g_2$",
        fundamental_domain=fundamental_domain,
        probes=probes,
        actions=actions,
        id_lines=id_lines,
    )


def main():
    """Execute script"""
    generate_plot()
