from random import shuffle
from itertools import permutations

num_agents = 4

class PreferenceList:
	def __init__(self):
		self.prefs = range(num_agents)
	def __getitem__(self, key):
		return self.prefs[key]
	def __str__(self):
		l = list(enumerate(self.prefs))
		l.sort(key = lambda (a, b): b)
		return " \succ ".join(["m_" + str(a + 1) for a,b in l])
	def __repr__(self):
		return str(self)
	def shuffle(self):
		shuffle(self.prefs)
	def prefers(self, a, b):
		return self[a] < self[b]

class MarriageMatch:
	def __init__(self, match):
		self.men = [0] * num_agents
		self.women = [0] * num_agents
		self.match = match
		for (m, w) in match:
			self.men[m] = w
			self.women[w] = m
	def __str__(self):
		return str(self.match)
	def __repr__(self):
		return str(self)

def all_matches():
	men = range(num_agents)
	for perm in permutations(men):
		yield MarriageMatch(zip(men, perm))

class MarriageMarket:
	def __init__(self):
		self.men = [PreferenceList() for i in xrange(num_agents)]
		self.women = [PreferenceList() for i in xrange(num_agents)]
	def display(self):
		print "men:"
		print "\n".join(map(str, self.men))
		print "women:"
		print "\n".join(map(str, self.women))
	def shuffle(self):
		for i in self.men:
			i.shuffle()
		for i in self.women:
			i.shuffle()
	def blocking_pair(self, match, m, w):
		w_curr = match.men[m]
		m_curr = match.women[w]
		return self.men[m].prefers(w, w_curr) and self.women[w].prefers(m, m_curr)

	def is_stable(self, match):
		for i in xrange(num_agents):
			for j in xrange(num_agents):
				if self.blocking_pair(match, i, j):
					return False
		return True

	def stable_matches(self):
		return filter(self.is_stable, all_matches())

	def double_non_comp(self, match1, match2):
		men_diff = women_diff = 0
		for i in xrange(num_agents):
			w1 = match1.men[i]
			w2 = match2.men[i]
			if self.men[i].prefers(w1, w2):
				men_diff += 1
			else:
				men_diff -= 1
			m1 = match1.women[i]
			m2 = match2.women[i]
			if self.women[i].prefers(m1, m2):
				women_diff += 1
			else:
				women_diff -= 1
		return abs(men_diff) < num_agents and abs(women_diff) < num_agents






# men = [range(num_agents) for i in range(num_agents)]
# women = [range(num_agents) for i in range(num_agents)]

# def random_market():
# 	for l in men:
# 		shuffle(l)
# 	for l in women:
# 		shuffle(l)

# def prefers(l, a, b):
# 	return l.index(a) < l.index(b)

# def blocking_pair(match, m1, w1):
# 	for (m2, w2) in match:
# 		if prefers(men[m1], w2, w1) and prefers(women[w2], m1, m2):
# 			return True
# 		if prefers(men[m2], w1, w2) and prefers(women[w1], m2, m1):
# 			return True
# 	return False

# def is_stable(match):
# 	for i in xrange(num_agents):
# 		for j in xrange(num_agents):
# 			if blocking_pair(match, i, j):
# 				return False
# 	return True


# def all_stable_matches():
# 	return filter(is_stable, all_matches())

M = MarriageMarket()
while 1:
	M.shuffle()
	l = M.stable_matches()
	if len(l) > 1:
		for i in xrange(len(l)):
			for j in xrange(i + 1, len(l)):
				if M.double_non_comp(l[i], l[j]):
					print l, i, j
					M.display()
					exit()


