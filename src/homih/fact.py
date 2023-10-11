class InvalidFactorialError(RuntimeError):
    """Error generated if an invalid factorial input is given."""

    def __init__(self, number: int) -> None:
        super().__init__(f"{number} is negative")


def factorial(n: int) -> int:
    """Computes the factorial through a recursive algorithm.

    Args:
        n: A positive input value.

    Raises:
        InvalidFactorialError: If n is less than 0.

    Returns:
        Computed factorial.
    """
    if n < 0:
        raise InvalidFactorialError(n)
    elif n == 0:
        return 1

    return n * factorial(n - 1)
