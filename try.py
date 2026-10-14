def risky_operation():
    # Code that might cause an error
    raise ValueError("Something went wrong")


try:
    # Code that might cause an error
    risky_operation()
except ValueError as e:
    # Code that runs if there's an error
    print("Something went wrong")
    print(f"Error: {e}")
