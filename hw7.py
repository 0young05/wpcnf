shopping_bag={}
print("[구입]")
while True:
    item=input("상품명? ")
    if item == '':
        break
    if item not in shopping_bag:
        pd=int(input("수량은? "))
        shopping_bag[item]=pd
        print(f'장바구니에 {item} {pd}개가(이) 담겼습니다.')
print(f'\n>>> 장바구니 보기: {shopping_bag}')
print("\n[검색]")
search=input("장바구니에서 확인하고자 하는 상품은? ")
print(f'{search}은(는) {shopping_bag[search]}개 담겨있습니다.')
