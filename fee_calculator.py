def calc_fee(total, paid, second_pay):
    reg_fee = 4000
    tution_fee = total - reg_fee
    need_to_pay = 0
    dict = {}
    j = 3
    #1st_installment --> 1/4th of tution fee + reg_fee
    #2nd, 3rd, 4th installment --> 1/4th of tution fee
    for i in range(4):
        if i == 0 and paid >= (tution_fee/4+reg_fee):
            need_to_pay = total-paid
            dict[i+1] = (paid, need_to_pay)
            continue
        temp = round(need_to_pay/j, 2)
        need_to_pay -= temp
        dict[i+1] = (temp, need_to_pay)
        j-=1
    to_pay_after_2nd = f'Need to pay after 2nd installment: {total-(dict[1][0]+second_pay)}'
    return [dict, to_pay_after_2nd]


print(i for i in calc_fee(29000, 11500, 5500))