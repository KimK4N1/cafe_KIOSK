from tkinter import *

WHITE = (255, 255, 255)

total_price = 0
payment_type = 0
coupon_list = [
    'asdf',
    'qwerty'
]

#금액추가
def americano_add():
    price_add(3500)
def cappuccino_add():
    price_add(4000)
def latte_add():
    price_add(4500)
def lemon_add():
    price_add(3500)
def grapefruit_add():
    price_add(3500)
def peach_add():
    price_add(3000)
def chococake_add():
    price_add(5500)
def strowberryrollcake_add():
    price_add(5000)
def cookies_add():
    price_add(2500)

#금액계산
def price_add(price):
    global total_price
    total_price += price
    total_price_label["text"] = f"{total_price}원"

#메뉴선택
def coffee():
    init()
    basic_button.place(x=10, y=10)
    main_label["text"] = "커피"
    main_label.place(x=wid/2-30, y=70)
    americano_button.place(x=(wid/3-50), y=(hei/3-50))
    americano_price.place(x=(wid/3-50)*3, y=(hei/3-50))
    cappuccino_button.place(x=(wid/3-50), y=(hei/3-50)*2)
    cappuccino_price.place(x=(wid/3-50)*3, y=(hei/3-50)*2)
    latte_button.place(x=(wid/3-50), y=(hei/3-50)*3)
    latte_price.place(x=(wid/3-50)*3, y=(hei/3-50)*3)

def drink():
    init()
    basic_button.place(x=10, y=10)
    main_label["text"] = "음료"
    main_label.place(x=wid/2-30, y=70)
    lemon_button.place(x=(wid/3-50), y=(hei/3-50))
    lemon_price.place(x=(wid/3-50)*3, y=(hei/3-50))
    grapefruit_button.place(x=(wid/3-50), y=(hei/3-50)*2)
    grapefruit_price.place(x=(wid/3-50)*3, y=(hei/3-50)*2)
    peach_button.place(x=(wid/3-50), y=(hei/3-50)*3)
    peach_price.place(x=(wid/3-50)*3, y=(hei/3-50)*3)

def dessert():
    init()
    basic_button.place(x=10, y=10)
    main_label["text"] = "디저트"
    main_label.place(x=wid/2-45, y=70)
    chococake_button.place(x=(wid/3-50), y=(hei/3-50))
    chococake_price.place(x=(wid/3-50)*3, y=(hei/3-50))
    strowberryrollcake_button.place(x=(wid/3-50), y=(hei/3-50)*2)
    strowberryrollcake_price.place(x=(wid/3-50)*3, y=(hei/3-50)*2)
    cookies_button.place(x=(wid/3-50), y=(hei/3-50)*3)
    cookies_price.place(x=(wid/3-50)*3, y=(hei/3-50)*3)

#화면 초기화
def init():
    for i in range(len(button_list)):
        button_list[i].place_forget()
    for i in range(len(label_list)):
        label_list[i].place_forget()
    entry.place_forget()

#처음화면
def basic():
    init()
    main_label["text"] = "메뉴"
    main_label.place(x=wid/2-30, y=100)
    coffee_button.place(x=wid/3-50, y=hei/3)
    drink_button.place(x=(wid/3-50)*2, y=hei/3)
    dessert_button.place(x=(wid/3-50)*3, y=hei/3)
    payment_display_button.place(x=wid/2-40, y=hei-50)

#결제 화면
def payment_display():
    init()
    basic_button.place(x=10, y=10)
    main_label["text"] = "결제수단"
    main_label.place(x=wid/2-60, y=100)
    payment_display_button.place_forget()
    cash_button.place(x=wid/2-20, y=(hei/6)*2)
    card_button.place(x=wid/2-20, y=(hei/6)*3)
    coupon_button.place(x=wid/2-20, y=(hei/6)*4)

#결제
def cash_payment():
    global payment_type
    payment_type = 1
    init()
    main_label["text"] = "현금을 넣어주세요"
    main_label.place(x=wid/2-135, y=100)
    entry.place(x=wid/2-100, y=hei/4)
    payment_button.place(x=wid/2-50, y=hei/4+50)

def card_payment():
    global payment_type
    payment_type = 2
    init()
    main_label["text"] = "카드를 넣어주세요"
    main_label.place(x=wid/2-135, y=100)
    payment_button.place(x=wid/2-50, y=hei/4+50)

def coupon_payment():
    global payment_type
    payment_type = 3
    init()
    main_label["text"] = "쿠폰을 입력하세요"
    main_label.place(x=wid/2-135, y=100)
    entry.place(x=wid/2-100, y=hei/4)
    payment_button.place(x=wid/2-50, y=hei/4+50)

def payment():
    global total_price
    total_price_label.place_forget()
    main_label["font"] = ("돋움", 13)
    if payment_type == 1:
        if int(entry.get()) >= total_price:
            main_label["text"] = f"결제가 완료되었습니다.\n잔돈은 {int(entry.get())-total_price}원 입니다."
            payment_button.place_forget()
            entry.place_forget()
        else:
            total_price = total_price - int(entry.get())
            main_label["text"] = f"결제 완료까지 {total_price}원 남았습니다."
    elif payment_type == 2:
        main_label["text"] = "결제가 완료되었습니다."
        payment_button.place_forget()
        entry.place_forget()
    elif payment_type == 3:
        for i in range(len(coupon_list)):
            if entry.get() == coupon_list[i]:
                main_label["text"] = "결제가 완료되었습니다."
                payment_button.place_forget()
                entry.place_forget()
    main_label.place(x=wid/2-135, y=100)
    

wid = 400
hei = 600

root = Tk()

root.title("login page")
root.geometry(f"{wid}x{hei}")

main_label = Label(text="메뉴", font=("돋움", 20))
main_label.place(x=wid/2-30, y=100)

total_price_label = Label(text="0원", font=("돋움", 20))
total_price_label.place(x=wid/2-20, y=hei-100)

coffee_button = Button(text="커피", font=("바탕", 12), command=coffee)
coffee_button.place(x=wid/3-50, y=hei/3)

drink_button = Button(text="음료", font=("바탕", 12), command=drink)
drink_button.place(x=(wid/3-50)*2, y=hei/3)

dessert_button = Button(text="디저트", font=("바탕", 12), command=dessert)
dessert_button.place(x=(wid/3-50)*3, y=hei/3)

basic_button = Button(text="이전", font=("바탕", 12), command=basic)

americano_button = Button(text="아메리카노", font=("바탕", 12), command=americano_add)
americano_price = Label(text="3500원", font=("돋움", 12))
cappuccino_button = Button(text="카푸치노", font=("바탕", 12), command=cappuccino_add)
cappuccino_price = Label(text="4000원", font=("돋움", 12))
latte_button = Button(text="라떼", font=("바탕", 12), command=latte_add)
latte_price = Label(text="4500원", font=("돋움", 12))

lemon_button = Button(text="레몬 에이드", font=("바탕", 12), command=lemon_add)
lemon_price = Label(text="3500원", font=("돋움", 12))
grapefruit_button = Button(text="자몽 에이드", font=("바탕", 12), command=grapefruit_add)
grapefruit_price = Label(text="3500원", font=("돋움", 12))
peach_button = Button(text="복숭아 아이스티", font=("바탕", 12), command=peach_add)
peach_price = Label(text="3000원", font=("돋움", 12))

chococake_button = Button(text="초코 케이크", font=("바탕", 12), command=chococake_add)
chococake_price = Label(text="5500원", font=("돋움", 12))
strowberryrollcake_button = Button(text="딸기 롤케익", font=("바탕", 12), command=strowberryrollcake_add)
strowberryrollcake_price = Label(text="5000원", font=("돋움", 12))
cookies_button = Button(text="쿠키", font=("바탕", 12), command=cookies_add)
cookies_price = Label(text="2500원", font=("돋움", 12))

payment_display_button = Button(text="결제화면", font=("바탕", 12), command=payment_display)
payment_display_button.place(x=wid/2-40, y=hei-50)

cash_button = Button(text="현금", font=("바탕", 12), command=cash_payment)
card_button = Button(text="카드", font=("바탕", 12), command=card_payment)
coupon_button = Button(text="쿠폰", font=("바탕", 12), command=coupon_payment)

entry = Entry(root)

payment_button = Button(text="결제확인", font=("바탕", 12), command=payment)

button_list = [
    coffee_button,
    drink_button,
    dessert_button,
    americano_button,
    cappuccino_button,
    latte_button,
    lemon_button,
    grapefruit_button,
    peach_button,
    chococake_button,
    strowberryrollcake_button,
    cookies_button,
    cash_button,
    card_button,
    coupon_button,
    basic_button,
    payment_button
]
label_list = [
    main_label,
    americano_price,
    cappuccino_price,
    latte_price,
    lemon_price,
    grapefruit_price,
    peach_price,
    chococake_price,
    strowberryrollcake_price,
    cookies_price
]

root.mainloop()