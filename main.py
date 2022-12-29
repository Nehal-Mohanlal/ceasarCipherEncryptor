alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n','o', 'p', 'q','r', 's', 't', 'u', 'v', 'w' , 'x', 'y', 'z']

shift = 4

word = 'nehal'

wordarr = list(word)

for x in wordarr:
    y = alpha.index(x)
    t_shift = y + shift
    cipher = alpha[t_shift]
    print(cipher)