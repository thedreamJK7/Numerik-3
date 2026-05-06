# Homework 03 — Finite Difference Method for the 1D Poisson Equation

Numerical solution of the boundary value problem:

$$-u''(x) = f(x), \quad x \in (0,1), \qquad u(0) = u(1) = 0$$

## Files

- `numerics3_homework03.ipynb` — main notebook with exercises and plots
- `numerics3_homework03.py` — standalone Python script with the same implementation

## What it does

1. Builds a uniform grid of `N` interior points on `(0, 1)`
2. Assembles the tridiagonal finite difference matrix `A`
3. Solves the linear system `A * u_h = f(x_h)` using `numpy.linalg.solve`
4. Compares the numerical solution against the exact solution `u(x) = sin(πx)`
5. Runs a convergence study for `N = 10, 20, 40, 80, 160, 320` and confirms second-order accuracy

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install numpy matplotlib
```

Then open `numerics3_homework03.ipynb` in VS Code or Jupyter and run all cells top to bottom.
