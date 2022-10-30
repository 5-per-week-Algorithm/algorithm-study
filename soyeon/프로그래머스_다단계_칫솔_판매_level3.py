def solution(enroll, referral, seller, amount):
    dict = {}
    pay = {}
    pay['-'] = 0
    for e,r in zip(enroll, referral):
        dict[e] = r
        pay[e] = 0
    for s,a in zip(seller, amount):
        tot = a*100
        while s != '-':
            give = int(tot*0.1)
            mine = tot - give
            if give < 1:
                pay[s] += tot
                break
            pay[s] += mine
            s = dict[s]
            tot = give
    result = []
    for k in pay.keys():
        result.append(pay[k])
    result.pop(0)
    return result
            
            
            
        