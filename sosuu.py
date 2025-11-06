class sosu:
    def souuhanntei(num):
        #num=int(input("整数を入力"))

        if num<2:
            print(f"{num}は素数ではない")
        else:

            for i in range(2,num):
                if num%i==0:
                    print(f"{num}は素数ではない")
                    break
            else:
                print(f"{num}は素数")













