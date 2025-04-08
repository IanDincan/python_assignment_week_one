first_number=input("Give me a number ")
second_number=input("Give me another number " )
operator=input("What operator do you want to use ")
if operator=="+":
    sum=int(first_number)+int(second_number)
    print(f"{first_number}+{second_number}={sum}")
elif operator=="-":
    answer=int(first_number)-int(second_number)
    print(f"{first_number}-{second_number}={answer}")
elif operator=="*":
    product=int(first_number)*int(second_number)
    print(f"{first_number}*{second_number}={product}")
elif operator=="/":
    quotient=int(first_number)/int(second_number)
    print(f"{first_number}/{second_number}={quotient}")
elif operator=="**":
    power=int(first_number)**int(second_number)
    print(f"{first_number}**{second_number}={power}")       

