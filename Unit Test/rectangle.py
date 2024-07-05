# def area(width, height):
#     """
#     Calculates the area of a rectangle.

#     :param width: The width of the rectangle.
#     :param height: The height of the rectangle.
#     :return: The area of the rectangle.
#     """
#     return width * height


# def perimeter(width, height):
#     """
#     Calculates the perimeter of a rectangle.

#     :param width: The width of the rectangle.
#     :param height: The height of the rectangle.
#     :return: The perimeter of the rectangle.
#     """
#     return 2 * (width + height)


# def area(width, height):
#     """
#     Calculates the area of a rectangle.

#     :param width: The width of the rectangle.
#     :param height: The height of the rectangle.
#     :return: The area of the rectangle.
#     """
#     if not isinstance(width, (int, float)) or not isinstance(height, (int, float)):
#         raise TypeError("Width and height must be numeric.")
#     return width * height


# def perimeter(width, height):
#     """
#     Calculates the perimeter of a rectangle.

#     :param width: The width of the rectangle.
#     :param height: The height of the rectangle.
#     :return: The perimeter of the rectangle.
#     """
#     if not isinstance(width, (int, float)) or not isinstance(height, (int, float)):
#         raise TypeError("Width and height must be numeric.")
#     return 2 * (width + height)

# ========================


def area(width, height):
    """
    Calculates the area of a rectangle.

    :param width: The width of the rectangle.
    :param height: The height of the rectangle.
    :return: The area of the rectangle.
    :raises ValueError: If width or height is non-positive.
    """
    if not isinstance(width, (int, float)) or not isinstance(height, (int, float)):
        raise TypeError("Width and height must be numeric.")
    if width <= 0 or height <= 0:
        raise ValueError("Width and height must be positive.")
    return width * height


def perimeter(width, height):
    """
    Calculates the perimeter of a rectangle.

    :param width: The width of the rectangle.
    :param height: The height of the rectangle.
    :return: The perimeter of the rectangle.
    :raises ValueError: If width or height is non-positive.
    """
    if not isinstance(width, (int, float)) or not isinstance(height, (int, float)):
        raise TypeError("Width and height must be numeric.")
    if width <= 0 or height <= 0:
        raise ValueError("Width and height must be positive.")
    return 2 * (width + height)
