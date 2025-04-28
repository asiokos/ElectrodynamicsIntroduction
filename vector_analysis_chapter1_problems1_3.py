import sympy as sp

x, y, z = sp.symbols('x y z')

#example 1.3
f = x**2 + y**3 + z**4

gradient_of_f = [sp.diff(f,var) for var in (x,y,z)]

print("Gradient of f(x, y, z):")
for i, g in zip(('x', 'y', 'z'), gradient_of_f):
    print(f"∂f/∂{i} = {g}")


#problem 1.11
f1 = (x**2 + y**2 + z**2)**(1/2)

gradient_of_f = [sp.diff(f1,var) for var in (x,y,z)]

print("Gradient of f(x, y, z):")
for i, g in zip(('x', 'y', 'z'), gradient_of_f):
    print(f"∂f/∂{i} = {g}")
