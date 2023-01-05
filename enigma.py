import rotors

class Enigma():

	Plugboard = rotors.plugboard

	def __init__(self, rotor="I V II", reflector='C', plugs='',window="Y K D",model='enigma1'):
		self.set_rotors(rotor,reflector,model)
		self.set_windows(window)
		self.plug(plugs)
		self.excludes = ['\n', ' ', '.', ',', '!']

	def handle(self, inp_string, IN=False):
		if IN:
			inp_string = inp_string.upper()
			out = []
			for letter in inp_string:
				if letter in self.excludes:
					out.append(letter)
				else:
					out.append(ord(letter)-65)
			return out
		else:
			out = ''.join(inp_string)
			return out

	def plug(self, plugs):
		plugs = plugs.upper()
		if plugs.isnumeric():
			raise Exception("The string should be alphabetic")
		for char in plugs:
			if char == " ":
				continue
			if plugs.count(char) != 1:
				print(f"'{char}' is repeated")
				raise Exception("None of the letters should be repeated!")
		if plugs == '':
			return
		plugs = plugs.split(' ')
		for i in plugs:
			if len(i)>2:
				print(f'{i} not valid!')
				raise Exception("Only groups of two allowed")
			else:
				self.Plugboard[ord(i[0])-65] = ord(i[1])-65
				self.Plugboard[ord(i[1])-65] = ord(i[0])-65

	def set_rotors(self, sets, reflector, model='enigma1'):
		model = model.lower()
		reflector = reflector.upper()
		if not (model in rotors.Models):
			raise Exception("Model does not exist")
		if not (reflector in eval(f'rotors.{model}().rotors')):
			raise Exception("Invalid Reflector")
		sets = sets.split(" ")
		if len(sets) > 3:
			raise TypeError
		for i in sets:
			ind = sets.index(i)
			sets[ind] = eval(f"rotors.{model}.{i}")
		self.RotorL, self.Rotorl = sets[0]
		self.RotorM, self.Rotorm = sets[1]
		self.RotorR, self.Rotorr = sets[2]
		self.Reflector = eval(f'rotors.{model}.{reflector}')

	def set_windows(self, win):
		if isinstance(win, str):
			self.WindowL, self.WindowM, self.WindowR = [ord(x)-65 for x in win.split(" ")]
		else:
			for i in win:
				if i > 26:
					raise TypeError 
			self.WindowL, self.WindowM, self.WindowR = [x-1 for x in win]

	def show_windows(self, arg=False):
		if arg:
			return f'{chr(self.WindowL+65)} {chr(self.WindowM+65)} {chr(self.WindowR+65)}'
		else:
			return [self.WindowL+1, self.WindowM+1, self.WindowR+1]

	def sequence(self, key):
		self.WindowR +=1
		self.WindowR %= 26
		if self.RotorR['N'] == self.WindowR-1:
			self.WindowM += 1
			self.WindowM %= 26
		elif self.RotorM['N'] == self.WindowM:
			self.WindowL += 1
			self.WindowL %= 26
			self.WindowM += 1
			self.WindowM %= 26
		f = (self.Rotorr[(self.Rotorm[(self.Rotorl[(self.Reflector[(self.RotorL[(self.RotorM[(self.RotorR[(self.Plugboard[key] + self.WindowR)%26] - self.WindowR + self.WindowM)%26] - self.WindowM + self.WindowL)%26] - self.WindowL)%26] + self.WindowL)%26] + self.WindowM - self.WindowL)%26] + self.WindowR - self.WindowM)%26] - self.WindowR)%26
		return self.Plugboard[f]

	def encrypt(self, key):
		enc = self.sequence(key)
		return (chr(enc+65))

	def decrypt(self, key):
		dec = self.sequence(key)
		return (chr(dec+65))

	def encrypt_str(self, message):
		message = self.handle(message,True)
		encrypted = []
		for enc in message:
			if enc in self.excludes:
				encrypted.append(enc)
			else:
				encrypted.append(self.encrypt(enc))
		return self.handle(encrypted)

	def decrypt_str(self, message):
		message = self.handle(message,True)
		decrypted = []
		for enc in message:
			if enc in self.excludes:
				decrypted.append(enc)
			else:
				decrypted.append(self.decrypt(enc))
		return self.handle(decrypted)
