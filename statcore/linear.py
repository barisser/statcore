
from .tensor import Tensor, Array

class LinearRegressor(object):
	def __init__(self):
		self.coefficients = Array()
		pass

	def train(self, X, Y, loss='MSE'):
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
		return

	def predict(self, X):
		return self.coefficients.dot(X)
