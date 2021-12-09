arr = ['asfasbadlkrekj fkksdke mmfke mmekke',
       'dskfjeo tmkfdk abacabababagun']

for i in range(len(arr)):
    new = arr[i].split()
    for k in range(len(new)):
         new[k] = ''.join(sorted(list(new[k])))
    print(' '.join(new))

new = [''.join(*list(map(sorted, list(map(list, i.split()))))) for i in arr]
print(new)