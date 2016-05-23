import numpy as np
import math


def jacobi(A, N=100, eps=10e-3):

	dim = A.shape[0]

	ev = np.matrix(np.identity(dim))
	n = N

	while(True):
		absA = np.abs(A)

		absA = absA - np.diagflat(np.diag(absA))

		axis = np.argmax(absA)
		p = axis // dim
		q = axis % dim

		if abs(A[p,q]) < eps:
			break

		if not p > q:
			pp = p
			p = q
			q = pp


		alpha = (A[p,p] - A[q,q])
		beta = - A[p,q]
		gamma = abs(alpha) / math.sqrt(alpha * alpha + beta * beta)

		cos = math.sqrt((1 + gamma) / 2)
		sin = math.copysign(math.sqrt((1 - gamma) / 2), alpha * beta)

		a = A.copy()

		for i in range(dim):
			a[p,i] = cos * A[p,i] - sin * A[q,i]
			a[q,i] = sin * A[p,i] + cos * A[q,i]
			a[i,q] = cos * A[i,p] - sin * A[i,q]
			a[i,q] = sin * A[i,p] + cos * A[i,q]

		a[p,q] = 0
		a[q,p] = 0

		A = a.copy()

		n -= 1
		if n < 0:
			break

	return A

if __name__ == '__main__':
	A = np.array([1., 0], [0, 1])
