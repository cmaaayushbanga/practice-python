with open('sample.txt', 'a') as f:
  f.write('Hello World3!')
  f.truncate(5)

with open('sample.txt', 'r') as f:
  print(f.read())