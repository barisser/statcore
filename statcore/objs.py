


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
		self.check_shapes(other)
		summed_values = []
		for i in range(len(self.values)):
			summed_values.append(self.values[i] + other.values[i])

		return Array(summed_values)

	def __sub__(self, other):
		self.check_shapes(other)
		new_values = []
		for i in range(len(self.values)):
			new_values.append(self.values[i] - other.values[i])
		return Array(new_values)