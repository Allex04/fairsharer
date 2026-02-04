def fair_sharer(values, num_iterations, share=0.1):
    """
    Runs num_iterations of a fair sharing algorithm.

    In each iteration, the highest value in "values" gives a fraction (share)
    of its value to both the left and right neighbor.
    The array is circular: the left neighbor of index 0 is the last element,
    and the right neighbor of the last element is index 0.

    Examples:
        fair_sharer([0, 1000, 800, 0], 1) -> [100, 800, 900, 0]
        fair_sharer([0, 1000, 800, 0], 2) -> [100, 890, 720, 90]

    Args:
        values (list): 1D list of numeric values
        num_iterations (int): number of iterations
        share (float): fraction to distribute to neighbors

    Returns:
        list: updated values after redistribution
    """
    values = list(values)

    n = len(values)

    for _ in range(num_iterations):
        max_index = values.index(max(values))
        amount = values[max_index] * share

        left = (max_index - 1) % n
        right = (max_index + 1) % n

        new_values = values.copy()
        new_values[max_index] -= 2 * amount
        new_values[left] += amount
        new_values[right] += amount

        values = new_values

    return values
