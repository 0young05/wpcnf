def buy(lst):
    print("[구입]")
    item = input("상품명? ")
    if item == '':
        return False
    if item not in lst:
        count = int(input("수량은? "))
        lst[item] = count
        print(f"장바구니에 {item} {count}개가 담겼습니다.\n")
def show(lst):
    print(f">>> 장바구니 보기: {lst}\n")
def find(lst):
    print("[검색]")
    ft=input("장바구니에서 확인하고자 하는 상품은? ")
    if ft in lst:
        print(f"{ft}은(는) {lst[ft]}개 담겨 있습니다.")
    else:
        print(f"장바구니에 {ft}은(는) 없습니다.")
shopping_bag = {}
while True:
    if buy(shopping_bag) == False:
        break
show(shopping_bag)
find(shopping_bag)
