# Հաջորդ ֆունկցիան հաշվարկում է մաթեմատիկական ֆունկցիա, որը հայտնի է Ակերմանի ֆունկցիա անվամբ

def ackermann(x, y):
	if y == 0:
		return 0
	elif x == 0:
		return 2 * y
	elif y == 1:
		return 2
	else:
		return ackermann(x - 1, ackermann(x, y - 1))

# Ի՞նչ կլինի հետևյալ կանչերի արդյունքը

ackermann(1, 5)
# Արդյունքը 32

ackermann(2, 4)
# Արյունքը՝ 65536

ackermann(3, 3)
# Արյունքը՝ 65536


# Կարճ նկարագրեք, թե ինչ են հաշվում a1, a2, և a3 ֆունկցիաները

def a1(n):
	return ackermann(0, n)
"""
a1 ֆունկցիան ցանկացած դեպքում քանի որ x-ը 0 է, վերադարձնելու է 2 * n
"""

def a2(n):
	return ackermann(1, n)

"""
a2 ֆունկցիան n > 1 դեքպում => ackermann(0, ackermann(1, n - 1)) որն էլ իր հերթին,
ackermann(0, ackermann(0, ackermann(1, n - 2)))․․․ ackermann(0,․․․, ackermann(1, {n (n - 1) == 1})), n - 1 հատ
վերջին արժեքն էլ 2 ստացվում է 2 * 2 * 2 * ... * 2 = 2 ** n
"""

def a3(n):
	return ackermann(2, n)

"""
a3 ֆունկցիան n > 1 դեքպում => ackermann(1, ackermann(2, n - 1)) որն էլ իր հերթին,
ackermann(1, ackermann(1, ackermann(2, n - 2))) նախորդի պրինցիպով շարունակելով ստացվում է 2 ** 2 ** 2 ... ** 2
ընհանուր n հատ
"""
