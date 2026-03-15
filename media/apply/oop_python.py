"""Simple OOP examples: function, classes and inheritance.

This module provides:
- a free function `compute_area` for rectangles
- a base class `Shape` (abstract-ish)
- `Rectangle` that inherits from `Shape`
- `Square` that inherits from `Rectangle` to demonstrate multi-level inheritance

Run this file directly to see a short demo.
"""

from __future__ import annotations
from typing import Any


def compute_area(width: float, height: float) -> float:
	"""Compute and return the area of a rectangle.

	Raises ValueError for non-positive dimensions.
	"""
	if width <= 0 or height <= 0:
		raise ValueError("width and height must be positive numbers")
	return width * height


class Shape:
	"""Base shape class.

	This class defines a minimal interface for shapes. Subclasses should
	implement the `area` method.
	"""

	def __init__(self, name: str = "Shape") -> None:
		self.name = name

	def area(self) -> float:
		"""Return the area of the shape.

		Subclasses must override this method.
		"""
		raise NotImplementedError("Subclasses must implement area()")

	def __repr__(self) -> str:
		return f"<{self.__class__.__name__} name={self.name!r}>"


class Rectangle(Shape):
	"""Rectangle shape implementing area and perimeter.

	Attributes:
		width: rectangle width (float > 0)
		height: rectangle height (float > 0)
	"""

	def __init__(self, width: float, height: float, name: str = "Rectangle") -> None:
		super().__init__(name=name)
		if width <= 0 or height <= 0:
			raise ValueError("width and height must be positive numbers")
		self.width = float(width)
		self.height = float(height)

	def area(self) -> float:
		return self.width * self.height

	def perimeter(self) -> float:
		return 2 * (self.width + self.height)

	def __repr__(self) -> str:
		return (
			f"<{self.__class__.__name__} width={self.width} height={self.height}"
			f" name={self.name!r}>"
		)


class Square(Rectangle):
	"""Square is a special Rectangle where width == height.

	Demonstrates inheritance from Rectangle -> Shape.
	"""

	def __init__(self, side: float, name: str = "Square") -> None:
		super().__init__(side, side, name=name)

	# no need to override area() — it inherits the correct behavior


def _demo() -> None:
	"""Small demo that creates shapes and prints values."""
	shapes: list[Shape] = []

	r = Rectangle(3, 4, name="MyRect")
	s = Square(5, name="MySquare")

	shapes.append(r)
	shapes.append(s)

	print("Demo: shapes and computed values")
	for sh in shapes:
		print(repr(sh))
		print(" area:", sh.area())
		if isinstance(sh, Rectangle):
			print(" perimeter:", sh.perimeter())
		print("---")


if __name__ == "__main__":
	# quick interactive demo when running the module directly
	_demo()

  



