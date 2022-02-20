import numpy as np

def mean(array):
	"""Compute mean"""
	s = 0.
	for i in range(len(array)):
		s += array[i]
	return s / len(array)	


def variance(array):
    avg = mean(array)
    s = 0.0
    for i in range(len(array)):
        s += (array[i] - avg)**2
    return s / len(array)


def std(array):
    return variance(array)**0.5


def dot(array1, array2):
	if array1.ndim == array2.ndim == 1:
		if len(array1) != len(array2):
			raise ValueError("Arrays must be of same length")

		s = 0.
		for i in range(len(array1)):
			s += array1[i] * array2[i]
		return s
	elif array1.ndim == array2.ndim == 2:
		x1, y1 = array1.shape
		x2, y2 = array2.shape
		if y1 != x2:
			raise ValueError("Shapes dont match: {} and {}".format(array1.shape, array2.shape))
		answer = np.zeros((x1, y2))
		for i in range(len(array1)):
			for j in range(len(array1[0])):
				v1 = array1[i][j]
				for y in range(len(array2[0])):
					v2 = array2[j][y]
					answer[i][y] += v1 * v2
		return answer
	else:
		if array1.ndim == 1:
			return dot(array1.reshape(1, -1), array2).reshape(-1)
		elif array2.ndim == 1:
			return dot(array1, array2.reshape(-1, 1)).reshape(-1)


def weighted_mean(weights, array):
	return dot(weights, array)

def mae(array):
	s = 0.
	avg = mean(array)
	for i in range(len(array)):
		s += abs(array[i] - avg)
	return s / len(array)

def percentile(array, value):
	pass

def correlation(x, y):
	"""
	sum of (x-x_mean) * (y-y_mean) / ((n-1) * std(x) * std(y))
	"""
	if len(x) != len(y):
		raise RuntimeError("Arrays must be of same length")
	s = 0.
	meanx = mean(x)
	meany = mean(y)
	for i in range(len(x)):
		s += (x[i] - meanx) * (y[i] - meany)
	return s / (len(x) * std(x) * std(y))

def correlation_matrix(mat1, mat2):
	pass


def invert(matrix):
	return


class lr():
	def __init__(self):
		self.A = None

	def fit(self, X, Y):
		"""
		Below is the derivation of the analytical linear regression fit.

		loss = (XA-Y)t*(XA-Y)
		= ((XA)t-Yt)*((XA) - Y)
		= (XA)t*(XA) - (XA)t*Y - Yt(XA) + YtY

		(XA)t*Y is a scalar thus
		(XA)t*Y = ((XA)t*Y)t
		= Yt*(XA)
		using identities
		(AB)t = BtAt
		and (Xt)t = X

		so substitute this in above and we get
		loss = (XA)t*(XA) - 2Yt*(XA) + YtY
		= AtXtXA - 2Yt(XA) + YYt

		d(Yt(XA)) / dA = XtY
		because of identities
		d(AX)/dX = At
		and
		(AB)t = AtBt

		d(XtAtXA)/dA = XtXA + XtXA = 2XtXA
		because of identity
		d(CtDC)/dC = DC + DtC, where D is XtX from above and C is A

		and the YtY term doesn't contribute to the derivative
		with respect to A

		thus we can substitute to get
		dloss / dA = 2XtXA - 2XtY

		and we can solve for dloss/dA = 0 with
		2XtXA-2XtY = 0 --->
		XtXA = XtY -->
		A = (XtX)^-1 * XtY.  This is our solution.
		"""
		self.A = dot(invert(dot(X.T, X)), dot(X.T, Y))
		import pdb;pdb.set_trace()


	def predict(self, X):
		return dot(self.A, X)
