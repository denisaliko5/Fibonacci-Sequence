while True:
  try:
    n = int(input("Enter an integer: "))
    break
  except:
    print("Input must be integer!")
seq  = [1,1]
for i in range(n-2): 
  seq.append(seq[-1] + seq[-2])
print(seq)