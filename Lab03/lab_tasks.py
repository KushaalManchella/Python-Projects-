def filter_by_letter(sentence, c):
    sentence = "the power of this engine matches that of the one we had last year"

    ans = []
    str = 0
    i = 0
    words = sentence.split(" ")
    print(words)


    for i in words:
        if i[0] == c or i[len(i)-1] == c:
            if i not in ans:
                ans.append(i)

    #print(ans)
    return(ans)

def get_cumulative_sum():

    ans = []
    i = 1
    sum = 0
    while i <= 100:
        sum += i
        i += 1
        ans.append(sum)



    #print(ans)
    return(ans)




if __name__ == '__main__':
    filter_by_letter("the power of this engine matches that of the one we had last year","t")
    get_cumulative_sum()