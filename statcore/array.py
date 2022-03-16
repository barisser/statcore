


class Array(object):
	def __init__(self, values=None):
		if not isinstance(values, list):
			raise TypeError("Wrong values type passed.")

		self.values = values

	def __repr__(self):
		data_string_length = min(6, len(self.values))
		data_string = "{}".format(self.values[:data_string_length])
		return "Array [{}]".format(data_string)

	def __len__(self):
		return len(self.values)

	def __eq__(self, other):
		return self.values == other.values

	def shape(self):
		return (len(self.values),)

	def check_shapes(self, other):
		shape1 = self.shape()
		shape2 = other.shape()
		if shape1 != shape2:
			raise ValueError("Shapes do not match {} vs {}".format(shape1, shape2))

	def __add__(self, other):
		"""
		Add another array elementwise, or add a scalar to all values.
		"""
		summed_values = []
		
		if isinstance(other, Array):
			self.check_shapes(other)
			for i in range(len(self.values)):
				summed_values.append(self.values[i] + other.values[i])
		elif isinstance(other, int) or isinstance(other, float):
			summed_values = [self.values[i] + other for i in range(len(self.values))]

		return Array(summed_values)

	def __sub__(self, other):
		"""
		Subtract another array elementwise, or subtract a scalar to all values.
		"""
		return self.__add__(other * -1)

	def __mul__(self, other):
		"""
		Elementwise vector multiplication
		or multiply all values by a scalar
		"""
		if isinstance(other, Array):
			self.check_shapes(other)
			new_values = []
			for i in range(len(self.values)):
				new_values.append(self.values[i] * other.values[i])
		elif isinstance(other, int) or isinstance(other, float):
			new_values = [self.values[i] * other for i in range(len(self.values))]
		return Array(new_values)

	def __rmul__(self, other):
		"""Ensure commutative multiplication"""
		return self * other

	def __radd__(self, other):
		"""Ensure commutative addition"""
		return self + other

	def __rsub__(self, other):
		"""Ensure commutative subtraction"""
		return self - other

	def __rtruediv__(self, other):
		"""
		Ensure commutative division
		A*B = (1/B) * A
		"""
		return self ** (-1) * other

	def __pow__(self, other):
		"""
		Array exponentatiation.  Must be a scalar.
		"""
		if not (isinstance(other, int) or isinstance(other, float)):
			raise ValueError("Exponentiation must be by a scalar.")
		return Array([self.values[i]**other for i in range(len(self.values))])

	def __truediv__(self, other):
		"""
		Elementwise vector division
		or divide all values by a scalar
		"""
		if isinstance(other, Array):
			self.check_shapes(other)
			return Array([self.values[i] / other.values[i] for i in range(len(self.values))])
		elif isinstance(other, int) or isinstance(other, float):
			if other == 0:
				raise ValueError("Cannot divide by zero.")
			return self * (1./other)

	def __mod__(self, other):
		"""
		Elementwise vector mod
		or mod all values by a scalar
		"""
		if isinstance(other, Array):
			self.check_shapes(other)
			return Array([self.values[i] % other.values[i] for i in range(len(self.values))])
		elif isinstance(other, int) or isinstance(other, float):
			if other == 0:
				raise ValueError("Cannot mod by zero")
			return Array([self.values[i] % other for i in range(len(self.values))])
