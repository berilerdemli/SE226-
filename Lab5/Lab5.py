S = 0

class MathTasks:

   
    def factorial(self, x):
        if x == 0 or x == 1:
            return 1
        return x * self.factorial(x - 1)


    
    def exp_x(self, x, n):
        term = lambda x, i: (x ** i) / self.factorial(i)

        total = 0
        for i in range(n + 1):
            total += term(x, i)

        return total


   
    def alternating_sum(self, n):
        global S

        if n == 0:
            return

        if n % 2 == 1:
            S += 1 / n
        else:
            S -= 1 / n

        self.alternating_sum(n - 1)


