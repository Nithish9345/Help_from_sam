class HelpFromSam:
    def help(self, n):
        total = 1
        while total <= n:
            total *= 2
            if total * 2 > n :
                return 1+ (n- total)

object = HelpFromSam()
print(object.help(n= int(input())))
