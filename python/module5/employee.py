class Employee():
	def __init__(self,first_name, last_name, salary):
		self.first_name = first_name.capitalize()
		self.last_name = last_name.capitalize()
		self.salary = int(salary)

	@property
	def full_name(self):
		return f"{self.first_name}, {self.last_name}"

	@full_name.setter
	def full_name(self,new_full_name):
		new_full_name = new_full_name.split(",")
		self.first_name = new_full_name[0].strip().capitalize()
		self.last_name = new_full_name[1].strip().capitalize()

	@property
	def email(self):
		return f"{self.first_name}_{self.last_name}@example.com".lower()
	
	@classmethod
	def from_str(cls, string):
		first_name, last_name, salary = string.split(",")
		return cls(first_name, last_name, salary)


class DevOps(Employee):
	def __init__(self, first_name, last_name, salary, skills=[]):
		super().__init__(first_name, last_name, salary)
		self.skills = [ i.lower().capitalize() for i in skills ]

	def add_skill(self,skill):
		skill = skill.lower().capitalize()
		if skill not in self.skills:
			return self.skills.append(skill)

	def remove_skill(self,skill):
		try:
			return self.skills.remove(skill.lower().capitalize())
		except:
			pass

class Manager(Employee):
	def __init__(self, first_name, last_name, salary, subordinates=[]):
		super().__init__(first_name, last_name, salary)
		self.subordinates = [ i for i in subordinates ]

	def add_subordinate(self, subordinate):
		return self.subordinates.append(subordinate)

	def remove_subordinate(self, deleted_item):
		if deleted_item in self.subordinates:
			return self.subordinates.remove(deleted_item)
		else:
			try:
				for i in self.subordinates:
					if deleted_item == i.email:
						return self.subordinates.remove(i)
			except Exception as e:
				pass
