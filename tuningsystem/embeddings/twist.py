"""Example of quotient T^3/S_3 (twisted prism) embedded 3D."""

import numpy as np
import matplotlib.pyplot as plt

M = 40
N = 3*(M-1)


def prism(m):
    """Generate prism."""
    p = np.zeros((N, N))
    q = np.zeros((N, N))
    for i in range(N):
        # center
        p0 = 0.
        q0 = 0.
        # angle
        angle = 2.*np.pi*i/(3*N)
        for j in range(m-1):
            x = j/(m-1)
            y = 0
            p[i][j] = x * np.cos(angle) - y * np.sin(angle)
            q[i][j] = x * np.sin(angle) + y * np.cos(angle)
            p0 += p[i][j]
            q0 += q[i][j]

        for j in range(m):
            x = 0.5*((m-j-1)/(m-1)+1)
            y = 0.866025*j/(m-1)
            p[i][j+m-1] = x * np.cos(angle) - y * np.sin(angle)
            q[i][j+m-1] = x * np.sin(angle) + y * np.cos(angle)
            p0 += p[i][j+m-1]
            q0 += q[i][j+m-1]

        for j in range(m-1):
            x = 0.5*(1-j/(m-1))
            y = 0.866025*(m-j-1)/(m-1)
            p[i][j+2*m-2] = x * np.cos(angle) - y * np.sin(angle)
            q[i][j+2*m-2] = x * np.sin(angle) + y * np.cos(angle)
            p0 += p[i][j+2*m-2]
            q0 += q[i][j+2*m-2]

        p[i] -= p0/N
        q[i] -= q0/N

    return p, q


def main():
    """Execute script."""

    theta = np.linspace(0, 2.*np.pi, N)
    phi = np.linspace(0, 2.*np.pi, N)
    theta, phi = np.meshgrid(theta, phi)
    px, py = prism(M)

    c, a = 2.5, 1
    x = (c + a*px) * np.cos(phi)
    z = (c + a*px) * np.sin(phi)
    y = a * py

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_ylim(-3, 3)
    ax.plot_surface(x, y, z, rstride=3, cstride=3, cmap='viridis')
    ax.view_init(36, 26)
    plt.show()
