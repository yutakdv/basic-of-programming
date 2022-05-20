def digit_frequencies(filename):
    infile = open(filename, 'r')
    text = infile.readline().rstrip()

    digits_count = [0 for _ in range(10)]
    for d in text:
        digits_count[int(d)] += 1
    paired = []
    i = 0
    for dc in digits_count:
        paired.append((str(i), dc))
        i += 1
    paired.sort(key = lambda x: x[1], reverse = True)
    infile.close()
    return paired

def digit_ranking_board(filename):
    outfile = open('ranking.txt', 'w')
    paired = digit_frequencies(filename)
    
    sum_total_num = 0
    for i in range(len(paired)):
        sum_total_num += paired[i][1]
    
    percent = []
    for i in range(len(paired)):
        percent.append(paired[i][1] / sum_total_num * 100)
    
    for i in range(len(paired)):
        data = str(paired[i][0]) + " " + str(paired[i][1]) + " " + str(round(percent[i], 1)) + '%' + '\n'
        outfile.write(data)
    
    outfile.close()


print(digit_ranking_board("digits.txt"))
