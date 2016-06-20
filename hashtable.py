class hashtable():
	def __init__(self):
		self.size = 11
		self.slots = [None]* 11
		self.value = [None]* 11

	def put(self,key,data):
		hashvalue = self.hashfunction(key,self.size)

		if self.slots[hashvalue] == None:
			self.slots[hashvalue] = key
			self.value[hashvalue] = data

		else:
			if self.slots[hashvalue] == key:
				self.value[hashvalue] = data

			else:
				nextslot = self.rehash(hashvalue,self.size)
				while self.slots[nextslot] != None and self.slots[nextslot] != key:
					nextslot = self.rehash(nextslot,self.size)

				if self.slots[nextslot] == None:
					self.slots[nextslot] = key
					self.value[nextslot] = data
				else:
					self.value[nextslot] = data

	def hashfunction(self,key,size):
		return key%size
	def rehash(self,oldhash,size):
		return (oldhash+1)%size

	def get(self,key):
		startslot = self.hashfunction(key,self.size)

		data,stop,found = None, False, False

		position = startslot

		while self.slots[position] != None and not found and not stop:
			
			if self.slots[position] == key:
				found = True
				data = self.value[position]
			else:
				position = self.rehash(position,self.size)
				if position == startslot:
					stop = True

		return data

	def __getitem__(self,key):
		return self.get(key)

	def __setitem__(self,key,data):
		return self.put(key,data)

h = hashtable()
h[12] = "Goat"
h[12] = "dog"
print h[12]
h[100] = "tomato"
print h[100]

