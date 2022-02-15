import numpy as np
import time

import statcore

def test_std():
	arr = np.random.random(10000)
	start1 = time.time()
	npanswer = arr.std()
	nptime = time.time() - start1

	start2 = time.time()
	myanswer = statcore.std(arr)
	mytime = time.time() - start2
	assert np.isclose(npanswer, myanswer)
	print("{}".format(mytime / nptime))
