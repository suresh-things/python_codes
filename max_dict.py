n=int(input())
arr=[int(input()) for i in range(n)]
s=list(set(arr))
dict={}
for i in range(n):
    if arr[i] in dict.keys():
        dict[arr[i]]+=1
    else:
        dict[arr[i]]=1
for i in s:
    if dict[i]==max(dict.values()):
        print(i,":",max(dict.values()))
        break
