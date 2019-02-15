

class MySet:
	def __init__(self, *args):
		self._dict = {}
		for arg in args:
			self.add(arg)

	def add(self, item):
		self._dict[item] = item

	def remove(self, item):
		for i in self:
			if item.equals(i):		
				del self._dict[i]
				break;

	def __iter__(self):
		return iter(self._dict.copy(  ))

	def __len__(self):
		return len(self._dict)

	def __copy__(self):
		return Set(self)

	def issubsetof(self,s):
		for i in self:
			for j in s:
				if i.equals(j):
					break
			else:
				return False
		return True


	def equals(self, s):
		return (self.issubsetof(s) and s.issubsetof(self))
	
	def union(self, s2):
		for item in s2:
			self.add(item)

