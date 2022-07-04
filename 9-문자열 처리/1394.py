# bc = b*암호의 길이+c의 순서 
# bcb = bc*암호의 길이 + b의 순서 
# bcbb = bcb*암호의길이 + b의 순서
arr = input()
pw = input()


key = arr.find(pw[0]) + 1

for i in range(1,len(pw)):
    print(i, key, len(arr), (arr.find(pw[i]) + 1))
    key = key*len(arr) + (arr.find(pw[i]) + 1)
print(key % 900528)