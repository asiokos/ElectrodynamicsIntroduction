import numpy as np
import matplotlib.pyplot as plt

# Constants
e0 = 8.854187817e-12  # Vacuum permittivity in F/m
q = 1e-9 
d = 1.0
y = 2.0

x1 = -d/2
x2 = d/2

y1 = y2 = 0

P = np.array([0, y])

def electric_field(q, r1, r2):
    r = np.linalg.norm(r2 - r1)
    r_unit = (r2 - r1) / r
    E = (1 / (4 * np.pi * e0)) * (q / r**2) * r_unit
    return E

E1 = electric_field(q, np.array([x1, y1]), P)
E2 = electric_field(q, np.array([x2, y2]), P)
E_net = E1 + E2

print(f"Electric field at point P({P[0]}, {P[1]}) due to charge 1: {E1}")
print(f"Electric field at point P({P[0]}, {P[1]}) due to charge 2: {E2}")
print(f"Net electric field at point P({P[0]}, {P[1]}): {E_net}")

# Plotting the electric field vectors
fig, ax = plt.subplots()

# Plot the charges
ax.scatter([x1, x2], [y1, y2], color='red', s=100, label='Charges')

# Plot the point of observation
ax.scatter(P[0], P[1], color='blue', s=100, label='Observation Point')

# Plot the vector of the electric field at the observation point
ax.quiver(P[0], P[1], E_net[0], E_net[1], angles='xy', scale_units='xy', scale=1, color='green', label='Total Electric Field')

# Set plot limits and labels
ax.set_xlim(-d, d)
ax.set_ylim(0, y + 1)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.legend()
plt.title("Electric Field Visualization (2D)")
plt.grid(True)
plt.show()