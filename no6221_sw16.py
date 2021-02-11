Man1 = input()
Man2 = input()

rsp=["가위", "바위", "보"]



if Man1 == Man2:
    print("Result : Draw")

# Man1이 이기는 경우
if Man1 == "가위" and Man2 == "보":
    print("Result : Man1 Win!")
elif Man1 == "바위" and Man2 == "가위":
    print("Result : Man1 Win!")
elif Man1 == "보" and Man2 == "바위":
    print("Result : Man1 Win!")
# Man2가 이기는 경우
elif Man2 == "가위" and Man1 == "보":
    print("Result : Man2 Win!")
elif Man2 == "바위" and Man1 == "가위":
    print("Result : Man2 Win!")
elif Man2 == "보" and Man1 == "바위":
    print("Result : Man2 Win!")