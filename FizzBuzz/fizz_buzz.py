for i in range(1,101):
    x=(i%3==0)*"Fizz"+(i%5==0)*"Buzz"
    print(i if not x else x)