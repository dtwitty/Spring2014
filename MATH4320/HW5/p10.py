max_degree = 2
mod = 5

class Polynomial:
	def __init__(self, tup):
		tup = tuple(i % mod for i in tup)
		while tup[-1] == 0 and len(tup) > 1:
			tup = tup[:-1]
		self.coeffs = tup
		self.degree = len(tup) - 1
	def __getitem__(self, index):
		if index < len(self.coeffs):
			return self.coeffs[index]
		else:
			return 0
	def __add__(self, other):
		base, op = self, other
		if self.degree < other.degree:
			base, op = other, self
		l = list(base.coeffs)
		for i in xrange(op.degree + 1):
			l[i] += op[i]
		return Polynomial(tuple(l))
	def __mul__(self, other):
		l = [0] * (self.degree + other.degree + 1)
		for i in xrange(self.degree + 1):
			for j in xrange(other.degree + 1):
				l[i + j] += self[i] * other[j]
		return Polynomial(tuple(l))
	def __str__(self):
		return str(self.coeffs)
	def __repr__(self):
		return str(self)
	def __eq__(self, other):
		return self.coeffs == other.coeffs

def combos(d):
	if d == 0:
		for i in xrange(mod):
			yield (i,)
	else:
		for k in combos(d - 1):
			for i in xrange(mod):
				yield (i,) + k

def all_poly(n = max_degree):
	for tup in combos(n):
		yield Polynomial(tup)

def reducible(poly):
	for p in all_poly(max_degree):
		for q in all_poly(poly.degree - p.degree):
			if p * q == poly:
				if p.degree > 0 and q.degree > 0:
					# print p, q, poly
					return True
	return False

for poly in all_poly():
	if poly.degree == 2 and poly[-1] == 1:
		if not reducible(poly):
			ord1 = "+ %dx" % poly[1] if poly[1] else ""
			ord0 = "+ %d" % poly[0] if poly[0] else ""
			print "x^2%s%s" % (ord1, ord0)
