"""
Աստիճան բարձրացնելու ալգորիթմը հիմնված է հաջորդաբար բազմապատկում կատարելու քայլերի վրա։ Նույնկերպ կարելի է
իրականացնել բազմապատկումը հաջորդաբար գումարում կատարելու քայլերով։ Ենթադրենք, որ մեր լեզվում չկա բազմապատկում
կատարելու օպերատոր, և այն պետք է իրականացնել։ Հաջորդ ֆունկցիան իրականացնում է բազմապատկումը, այնպես, ինչպես pow-ն.
def mul(a, b):
    if b == 0:
        return 0
    else:
        return a + mul(a, b - 1)
Այս ալգորիթմը, ինչպես pow-ն, O(n) բարդության է և ժամանակի տեսանկյունից, և հիշողության։ Ենթադրենք, որ մեր լեզվում
կա double և halve ֆունկցիաները, որոնցից առաջինը ամբողջ թիվը բազմապատկում է 2-ով, իսկ մյուսը զույգ թիվը
բաժանում է 2-ի։ Օգտագործելով այդ ֆունկցիաները, fast_pow-ի օրինակով իրականացրեք fast_mul ֆունկցիան, որը O(log(n))
բարդության է։
"""
def is_even(n):
    return n % 2 == 0

def double(n):
    return n * 2

def halve(n):
    return n / 2

# Ռեկուրսիվ լուծում
def fast_mul_rec(a, b):
    if b == 0:
        return 0
    if is_even(b):
        return double(fast_mul_rec(a, halve(b)))
    return a + (fast_mul_rec(a, b - 1))

# Իտերատիվ լուծում
def fast_mul_iter(a, b):
    res = 0
    while b > 0:
        if not is_even(b):
            res += a
            b -= 1
        a = double(a)
        b = halve(b)
    return res

m, n = 41, 30

print(f"Fast-mul-rec {m} * {n}: {fast_mul_rec(m,n)}")
print(f"Fast-mul-iter {m} * {n}: {fast_mul_iter(m,n)}")
print(f"Built-in {m} * {n}: {m * n}")
print("-------------------------------")

m, n = 0, 12

print(f"Fast-mul-rec {m} * {n}: {fast_mul_rec(m,n)}")
print(f"Fast-mul-iter {m} * {n}: {fast_mul_iter(m,n)}")
print(f"Built-in {m} * {n}: {m * n}")
print("-------------------------------")

m, n = 4, 1

print(f"Fast-mul-rec {m} * {n}: {fast_mul_rec(m,n)}")
print(f"Fast-mul-iter {m} * {n}: {fast_mul_iter(m,n)}")
print(f"Built-in {m} * {n}: {m * n}")
print("-------------------------------")
