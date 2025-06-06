import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np


def extrude_polygon(polygon, height=3):
    """Create a simple 3D extruded model from a 2D floor plan."""
    bottom = np.array([[x, y, 0] for x, y in polygon])
    top = bottom + np.array([0, 0, height])
    faces = []

    # bottom and top faces
    faces.append(bottom)
    faces.append(top)

    # side faces
    for i in range(len(polygon)):
        j = (i + 1) % len(polygon)
        faces.append([bottom[i], bottom[j], top[j], top[i]])

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    poly3d = Poly3DCollection(faces, facecolors='cyan', linewidths=1, edgecolors='r', alpha=0.5)
    ax.add_collection3d(poly3d)

    max_range = np.array([bottom[:,0].max()-bottom[:,0].min(),
                          bottom[:,1].max()-bottom[:,1].min(),
                          height]).max() / 2.0

    mid_x = (bottom[:,0].max()+bottom[:,0].min()) * 0.5
    mid_y = (bottom[:,1].max()+bottom[:,1].min()) * 0.5
    mid_z = height / 2.0

    ax.set_xlim(mid_x - max_range, mid_x + max_range)
    ax.set_ylim(mid_y - max_range, mid_y + max_range)
    ax.set_zlim(0, height)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    # Simple demo floor plan: a rectangle 10x6 units
    floor_plan = [(0, 0), (10, 0), (10, 6), (0, 6)]
    extrude_polygon(floor_plan, height=5)
