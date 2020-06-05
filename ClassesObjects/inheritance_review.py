class SortedList(list):
  def __init__(self, lst):
    super().__init__(lst)
    self.sort()

  def append(self, value):
    super().append(value)
    self.sort()

new_list = SortedList([4, 1, 5])
new_list.append(3)
print(new_list)

class DefaultDictionary(dict):
  def __init__(self, my_dict, default):
    super().__init__(my_dict)
    self.default = default
    
  def __getitem__(self, key):
    if key in self:
      return super().__getitem__(key)
    return self.default

test = DefaultDictionary({"Sveta": 2, "Dima": 3}, 4)
print(test["Sveta"])
print(test["Ira"])

