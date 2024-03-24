def get_integer(prompt):
    won=int(input(prompt))
    return won
def exchange():
    won500=won//500
    won100=(won-(won500*500))//100
    won50=(won-(won500*500)-(won100*100))//50
    won10=(won-(won500*500)-(won100*100)-(won50*50))//10
    print("500원 동전의 개수:",won500)
    print("100원 동전의 개수:",won100)
    print("50원 동전의 개수:",won50)
    print("10원 동전의 개수:",won10)
won=get_integer("동전으로 교환하고자 하는 금액은?")
exchange()
