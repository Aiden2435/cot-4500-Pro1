# Approximation Algorithm

# Initial guess and tolerance
x0 = 1.5
tol = 0.000001

def approximation_algorithm():
    iter = 0
    diff = x0
    x = x0

    # Print initial guess and iteration count
    print(f"{iter} : {x}")

    # Loop until the difference between successive approximations is below tolerance
    while diff >= tol:
        iter += 1
        y = x
        x = (x / 2) + (1 / x)
        
        # Print current iteration and approximation
        print(f"{iter} : {x}")
        
        # Calculate the difference between the new and old approximations
        diff = abs(x - y)

    # Print final result
    print(f"\nConvergence after {iter} iterations")


# Define the function whose root we want to find
def f(x):
    return x**2 - 4  # Example: f(x) = x^2 - 4, the root is at x = 2 or x = -2

def bisection_method(left, right, tol, max_iter):
    i = 0  # Iteration counter

    # Check that the root lies between left and right
    if f(left) * f(right) > 0:
        print("Function does not have opposite signs at the endpoints.")
        return None

    while abs(right - left) > tol and i < max_iter:
        i += 1
        p = (left + right) / 2  # Midpoint

        # Check if we found the root
        if f(left) * f(p) < 0:
            right = p
        else:
            left = p

    # Output the result
    return p

# Example usage:
left = 0  # Start of the interval
right = 3  # End of the interval
tol = 0.0001  # Desired tolerance
max_iter = 100  # Maximum number of iterations

root = bisection_method(left, right, tol, max_iter)
print(f"The root is approximately: {root}")


def g(p):
    return (p**2 + 4) / 2  # Example: g(p) = (p^2 + 4) / 2, a simple function for illustration

def fixed_point_iteration(p0, tol, N0):
    i = 1  # Iteration counter
    while i <= N0:
        p = g(p0)  # Apply the iteration formula

        # Check for convergence (i.e., if the difference is smaller than the tolerance)
        if abs(p - p0) < tol:
            print(f"Root found: p = {p}")
            print("SUCCESS")
            return p
        
        i += 1  # Increment the iteration counter
        p0 = p  # Update p0 for the next iteration

    # If the maximum iterations are exceeded without convergence
    print("FAILURE")
    return None


# Define the function f(x) and its derivative f'(x)
def f(x):
    return x**2 - 4  # Example: f(x) = x^2 - 4, which has roots at x = 2 and x = -2

def df(x):
    return 2*x  # Derivative of f(x) = x^2 - 4, which is f'(x) = 2x

def newton_raphson(p_prev, tol, N0):
    i = 1  # Iteration counter
    
    while i <= N0:
        # Check if the derivative is non-zero to avoid division by zero
        derivative = df(p_prev)
        if derivative != 0:
            # Update the next approximation using the Newton-Raphson formula
            p_next = p_prev - f(p_prev) / derivative

            # Check for convergence (if the difference is smaller than the tolerance)
            if abs(p_next - p_prev) < tol:
                print(f"Root found: p = {p_next}")
                print("SUCCESS")
                return p_next
            
            # Update the previous approximation for the next iteration
            p_prev = p_next
            i += 1  # Increment iteration counter
        
        else:
            # Report unsuccessful if the derivative is zero (can't divide by zero)
            print("FAILURE: Derivative is zero.")
            return None
    
    # If max iterations are exceeded without convergence
    print("FAILURE: Maximum iterations reached.")
    return None

# Example usage:
p_prev = 1.0  # Initial approximation
tol = 0.0001  # Desired error tolerance
N0 = 100  # Maximum number of iterations

root = newton_raphson(p_prev, tol, N0)





