import numpy as np

def calculate_angle(A, B):
    dot_product = np.dot(A, B)
    norm_product = np.linalg.norm(A) * np.linalg.norm(B)
    cos_theta = dot_product / norm_product
    angle = np.arccos(np.clip(cos_theta, -1.0, 1.0))
    return np.degrees(angle)

#problem 1.2
A = np.array([1, 0, 1])
B = np.array([0, 1, 1])

angle = calculate_angle(A, B)

print(f"The angle between the face diagonals A and B is {angle:.2f} degrees.")

#problem 1.3
A2 = np.array([1, 1, 1])
B2 = np.array([1,1,-1])

angle2 = calculate_angle(A2, B2)

print(f"The angle between the body diagonals A2 and B2 is {angle2:.2f} degrees.")

#problem 1.4
A3 = np.array([-1, 0, 3])
B3 = np.array([-1, 2, 0])

cross_vector = np.cross(B3, A3)
cross_magnitude = np.linalg.norm(cross_vector)

print(f"Cross product of {A3} and {B3} is {cross_vector} with magnitude {cross_magnitude}")