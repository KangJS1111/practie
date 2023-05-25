
def get_price(is_vip=False,
              is_birthday=False,
              is_membership=False,
              card=False,
              review=False,
              first_time=False):
    if is_vip == True:
        return 10000
    elif is_birthday == True:
        return 12000
    elif is_membership == True:
        return 13000
    elif card == True:
        return 14000
    elif review == True:
        return 11000
    elif first_time == True:
        return 10000
    else :
        return 15000
    
price = get_price(review=True)
print(f'손님께서 결제할 금액은 {price}원 입니다')