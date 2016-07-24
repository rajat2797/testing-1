def vowel(str2):
    count=0
    for c in str2:
        if c in 'aeiou':
            count+=1
    return count

if __name__=='__main__':
    #when directly running
    a=raw_input()
    print vowel(a)

