Print the numbers from 1 to 100 inclusive, each on their own line.

If, however, the number is a multiple of three then print Fizz instead, and if the number is a multiple of five then print Buzz.

For numbers which are multiples of both three and five then print FizzBuzz.

from https://code-golf.io/fizz-buzz


    print((i%3==0*"Fizz" + i%5==0*"Buzz") if i%3==0 or i%5==0 else str(i) + "\n", end="")