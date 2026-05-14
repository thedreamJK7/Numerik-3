import numpy as np
import matplotlib.pyplot as plt

def f(x):
    """Right-hand side of the PDE."""
    return np.pi**2 * np.sin(np.pi * x)

def u(x):
    """Exact solution."""
    return np.sin(np.pi * x)

def grid_points(N):
	"""Return the N interior grid points for the interval (0, 1)."""
	"""We are excluding the grid points on the boundary"""
	return np.linspace(0, 1, N + 1, endpoint=False)[1:]

def build_matrix(N):
	"""Return the finite-difference matrix for -u'' on (0, 1) with zero Dirichlet data."""
	h = 1 / (N + 1)
	return (2 * np.eye(N) - np.eye(N, k=1) - np.eye(N, k=-1)) / (h**2)

def solve_pde(f, N):
    """Solve -u'' = f on (0, 1) with u(0)=u(1)=0 using N interior grid points."""
    x_h = grid_points(N)
    A = build_matrix(N)
    b = f(x_h)
    u_h = np.linalg.solve(A, b)
    return u_h

def main():
    # Let this cell run to check your grid point implementation

	N = 10
	"""x_h = grid_points(N)
	assert x_h.shape == (N,), "Grid must be of shape (N,)."

	# Test build_matrix
	A = build_matrix(N)
	print(A)
	assert A.shape == (N,N), "A has to be of shape (N,N)"
	plt.figure(figsize=(10, 2))

	# basic usage of the solver"""
	u_h = solve_pde(f, N) 

	assert u_h.shape == (N,), "u_h must have shape (N,)"
	# axis
	"""plt.hlines(0, 0, 1, color="black")

	# boundary points
	plt.plot(0, 0, "ks", label="boundary points")
	plt.plot(1, 0, "ks")

	# grid points
	plt.plot(x_h, np.zeros_like(x_h), "o", label="grid points")
	plt.text(0, -0.08, "0", ha="center")
	plt.text(1, -0.08, "1", ha="center")

	plt.xlabel("x_i")
	plt.yticks([])
	plt.title("grid points")
	plt.legend()
	plt.ylim(-0.2, 0.2)
	plt.grid(False)
	plt.show()"""
	x_h = grid_points(N)
	u_h = solve_pde(f, N)

	# 2. Haqiqiy yechim uchun "zichroq" nuqtalar (silliq chiziq uchun)
	x_fine = np.linspace(0, 1, 100)
	u_exact = u(x_fine) # haqiqiy yechim funksiyasi

	# 3. Grafikni yaratish
	plt.figure(figsize=(8, 5))

	# Raqamli yechimni nuqtalar (dots) bilan chizamiz
	plt.plot(x_h, u_h, 'ro', label=f'Numerical solution (N={N})')

	# Haqiqiy yechimni silliq chiziq bilan chizamiz
	plt.plot(x_fine, u_exact, 'b-', label='Exact solution')

	# Grafik bezaklari
	plt.title("Poisson Equation: Numerical vs Exact Solution")
	plt.xlabel("x")
	plt.ylabel("u(x)")
	plt.legend()
	plt.grid(True)
	plt.show()

if __name__=="__main__":
	main()
