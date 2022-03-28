import copy
import itertools

def get_shape_from_lists(data):
	shape = []

	size = len(data)
	shape.append(size)

	while True:
		if not data:
			break
		if isinstance(data[0], int) or isinstance(data[0], float):
			break
		else:
			if not all([isinstance(x, list) for x in data]):
				raise ValueError("all elements must be a list")
			sizes = [len(x) for x in data]
			if not len(set(sizes)) == 1:
				raise ValueError("All entries must be the same length.")
			shape.append(len(data[0]))
			data = data[0] # we are not doing multi-level checks to determine if sizes are consistent
			# above should be fixed eventually.  Current check only goes to depth=1.
	return tuple(shape)

def veryclose(a, b, tol=10**-9):
	return abs(a-b) < tol

def tensor_list_to_dict(values, shape):
	count = 1
	for x in shape:
		count *= x

	data = {}
	for i in range(count):
		coord = []
		for x in shape:
			coord.append(i % x)
			i -= i % x
			i /= x
		data[tuple(coord)] = v

def get_shape_from_keys(keys):
	dims = len(next(iter(keys)))
	shape = [0] * dims
	for k in keys:
		for i in range(len(k)):
			shape[i] = max(shape[i], k[i] + 1)
	return tuple(shape)

def nested_list_lookup(llist, coords):
	if len(coords) == 1:
		return llist[coords[0]]
	return nested_list_lookup(llist[coords[0]], coords[1:])

def nested_list_modify(llist, key, value):
	rets = []
	for n, x in enumerate(llist):
		if n != key[0]:
			rets.append(x)
		else:
			if len(key) == 1:
				rets.append(value)
			else:
				rets.append(nested_list_modify(x, key[1:], value))
	return rets

class Tensor(object):
	def __init__(self, values=None):
		if not isinstance(values, list):
			raise ValueError("Values must be a list")

		if values is None:
			values = []
		self.shape = get_shape_from_lists(values)
		self.dims = len(self.shape)
		self.values = values
		self.num_elements = 1
		for x in self.shape:
			self.num_elements *= x

	def check_shape_with_other(self, other):
		if not self.shape == other.shape:
			raise ValueError("Shapes of tensors aren't equal: {} vs {}".format(
				self.shape, other.shape))

	def all_coords(self): # todo make this return an iterable
		coord_count = 1
		for x in self.shape:
			coord_count *= x

		coords = []
		for i in range(coord_count):
			# convert the integer to a coord in the space
			coord = []
			j = copy.copy(i)
			for dim_size in self.shape:
				if dim_size == 0:
					break
				coord.append(int(j%dim_size))
				j -= j%dim_size
				j /= dim_size

			coords.append(tuple(coord))
		return coords

	def __repr__(self):
 		return "Tensor <num_elements={}, shape={}>".format(self.num_elements, self.shape)

	def __len__(self):
		return self.shape[0]

	def __eq__(self, other):
		if self.shape != other.shape:
			return False
		for k in self.all_coords():
			if not veryclose(self[k], other[k]):
				return False
		return True

	def __add__(self, other):
		"""Add to another tensor or scalar value"""
		if isinstance(other, Tensor):
			self.check_shape_with_other(other)
			newtensor = copy.deepcopy(self)
			for k in self.all_coords():
				newtensor[k] = newtensor[k] + other[k]
		elif isinstance(other, int) or isinstance(other, float):
			newtensor = copy.deepcopy(self)
			for k in self.all_coords():
				newtensor[k] = newtensor[k] + other
		return newtensor

	def __radd__(self, other):
		return self + other

	def __sub__(self, other):
		return self + (-1 * other)

	def __rsub__(self, other):
		return self - other

	def __mul__(self, other):
		"""
		Multiply a tensor by a scalar
		or *elementwise* by another tensor with
		the same shape.
		"""
		if isinstance(other, int) or isinstance(other, float):
			newtensor = copy.deepcopy(self)
			for k in self.all_coords():
				newtensor[k] *= other
			return newtensor
		elif isinstance(other, Tensor):
			self.check_shape_with_other(other)
			newtensor = copy.deepcopy(self)
			for k in self.all_coords():
				newtensor[k] = self[k] * other[k]
			return newtensor
		else:
			raise ValueError("This type not accepted.")

	def __rmul__(self, other):
		return self * other

	def __truediv__(self, other):
		"""
		TrueDivide our tensor by a scalar
		or elementwise by another tensor
		of the same shape
		"""
		if isinstance(other, int) or isinstance(other, float):
			newtensor = copy.deepcopy(self)
			for k in self.all_coords():
				newtensor[k] = self[k] / other
			return newtensor
		elif isinstance(other, Tensor):
			self.check_shape_with_other(other)
			newtensor = copy.deepcopy(self)
			for k in self.all_coords():
				if other[k] == 0:
					raise ValueError("Cannot divide by zero.")
				newtensor[k] = self[k] / other[k]
			return newtensor
		else:
			raise ValueError("This type is not accepted.")

	def __pow__(self, other):
		"""
		Elementwise power operations
		"""
		if not (isinstance(other, int) or isinstance(other, float)):
			raise ValueError("Exponentiation must be by a scalar.")
		newtensor = copy.deepcopy(self)
		for k in self.all_coords():
			newtensor[k] = self[k] ** other
		return newtensor

	def __mod__(self, other):
		"""
		Modulo our tensor by a scalar
		or elementwise by another tensor of the same shape.
		"""
		newtensor = copy.deepcopy(self)
		if isinstance(other, int) or isinstance(other, float):
			for k in self.all_coords():
				newtensor[k]= self[k] % other
			return newtensor
		elif isinstance(other, Tensor):
			self.check_shape_with_other(other)
			for k in self.all_coords():
				if other[k] == 0:
					raise ValueError("Cannot mod elementwise by zero.")
				newtensor[k] = self[k] % other[k]
			return newtensor
		else:
			raise ValueError("This type is not accepted.")

	def __setitem__(self, k, v):
		self.values = nested_list_modify(self.values, k, v)

	def __getitem__(self, k):
		if isinstance(k, int):
			data = self.values[k]
			if isinstance(data, int) or isinstance(data, float):
				return data
			else:
				return Tensor(data) # todo make this an array or matrix when appropriate, aesthetic change only
		elif isinstance(k, tuple):
			res = nested_list_lookup(self.values, k)
			if isinstance(res, int) or isinstance(res, float):
				return res
			return Tensor(res) # same as above, should be a matrix or array when appropriate.

	def dot(self, other):
		dim1 = self.dims
		dim2 = other.dims
		if not (dim1 in [1, 2] and dim2 in [1, 2]):
			# it would be better to generalize to arbitrary dims but not now.
			raise ValueError("Dot product only supported for 1D and 2D Tensors for now.")
		raise NotImplementedError("")

	def mean(self):
		s = 0.
		n = 0
		for k in self.all_coords():
			s += self[k]
			n += 1
		return s/n

	def std(self):
		return self.var() ** 0.5

	def var(self):
		s = 0.
		n = 0.
		avg = self.mean()
		for k in self.all_coords():
			s += (self[k] - avg)**2
			n += 1
		return s / n


class Matrix(Tensor):
	def __init__(self, values=None):
		Tensor.__init__(self, values=values)
		if self.dims != 2:
			raise ValueError("Matrices must be 2D, found shape: {}".format(self.shape))

class Array(Tensor):
	def __init__(self, values=None):
		Tensor.__init__(self, values=values)
		if self.dims != 1:
			raise ValueError("Arrays must be 1D, found shape: {}".format(self.shape))

