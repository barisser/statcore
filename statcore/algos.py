import numpy as np

def l1norm(tensor1, tensor2):
	return np.sum(np.abs(tensor2 - tensor1))

def l2norm(tensor1, tensor2):
	t3 = tensor2 - tensor1
	return np.sum(t3**2)

class KMeans(object):
	"""
	Class that implements K-means clustering fitting and prediction.
	Currently extremely slow.
	"""
	def __init__(self, clusters_n, distance_norm='l2'):
		self.clusters_n = clusters_n

		if distance_norm == 'l2':
			self.dist_func = l2norm
		elif distance_norm == 'l1':
			self.dist_func = l1norm
		else:
			raise Exception("Invalid distance norm selected")

		self.centroids = dict([(k, [None, 0]) for k in range(clusters_n)])


	def fit(self, tensor, n=1):
		bestsumdist = 10**64
		for i in range(n):
			centroids, sumdist = self.fit_once(tensor)
			if sumdist < bestsumdist:
				bestsumdist = sumdist
				bestroids = centroids
		self.centroids = bestroids


	def fit_once(self, tensor):
		"""
		Algo description
		start by randoming assignigng a cluster to each data point.
		Compute cluster centroid.  Assign all closest points.  Repeat.
		When cluster assignments stop changing, stop.

		This implementation does not standardize or center values in the tensor.  That should occur upstream.
		This implementation alos does not run multiple iterations to find the best output (since solutions are local optima).

		First axis of input tensor is index of data points (so data points are tensor[0], tensor[1], etc...)
		"""
		assignments = np.random.randint(self.clusters_n, size=len(tensor))

		changed = True

		while changed:
			changed = False
			sumdist = 0
		
			# centroids is dict with key=cluster_n and value = (centroid center coord, number of points)
			# reset centroids
			centroids = dict([(k, [np.zeros(tensor[0].shape), 0]) for k in range(self.clusters_n)])
			# compute centroids
			for i in range(len(tensor)):
				current_cluster = assignments[i]
				point_coord = tensor[i]
				centroids[current_cluster][0] += point_coord # add N-1 dimensional point
				centroids[current_cluster][1] += 1 # count points
			for i in range(self.clusters_n):
				if centroids[i][1] > 0:
					centroids[i][0] /= centroids[i][1] # normalize
		
			
			# re-assign all points to closest centroids
			for i in range(len(tensor)):
				point = tensor[i]
				mindist = np.finfo(float).max
				bestcentroid = -1
				for k, (ca, _) in centroids.items():
					dist = self.dist_func(point, ca)
					if dist < mindist:
						bestcentroid = k
						mindist = dist
				newcentroid = bestcentroid
				oldcentroid = assignments[i]
				sumdist += mindist
				if newcentroid != oldcentroid:
					changed = True
					assignments[i] = newcentroid

		return dict([(k, v[0]) for k, v in centroids.items()]), sumdist

	def predict(self, tensor):
		assignments = np.zeros(len(tensor))
		for i in range(len(tensor)):
			point = tensor[i]
			mindist = np.finfo(float).max
			bestcentroid = -1
			for k, ca in self.centroids.items():
				dist = self.dist_func(point, ca)
				if dist < mindist:
					bestcentroid = k
					mindist = dist
			newcentroid = bestcentroid
			oldcentroid = assignments[i]
			if newcentroid != oldcentroid:
				assignments[i] = newcentroid
		return assignments

