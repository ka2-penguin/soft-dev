
def string_times(str, n):
  return str*n

print(string_times('Hi', 2))

def string_bits(str):
  new_str = ''
  for i in range(0,len(str),2):
    new_str += str[i:i+1]
  return new_str

print(string_bits('Hello'))

def string_splosion(str):
  new_str = ''
  for i in range(len(str)):
    new_str+=str[:i+1]
  return new_str

print(string_splosion('jerry'))
