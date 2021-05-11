#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Kaloyan Krastev Krastev, kaloyansen@gmail.com
###########################################################

class EX1:
	"""
	Ecrire un algorithme qui demande successivement 20 nombres à l’utilisateur, et qui lui dise ensuite quel était le plus grand parmi ces 20 nombres :
	Modifiez ensuite l’algorithme pour que le programme affiche de surcroît en quelle position avait été saisie ce nombre :
	C’était le nombre numéro 2
	"""
	numax = 20
	inum = []

	def __init__(self):
		i = 0
		while i < self.numax:
			num = input("enter a whole number {}/{}: ".format(i + 1, self.numax))
			self.inum.append(num)
			i += 1
		print('list all {}'.format(self.inum))
		lpg, pos = self.calcul()
		print('max = {}, pos[0] = {}'.format(lpg, pos))

	def calcul(self):
		leplusgrand = max(self.inum)
		count = self.inum.count(leplusgrand)
		if count > 1:
			print('warning {} maximum found'.format(count))
		position = self.inum.index(leplusgrand) + 1
		return leplusgrand, position


class EX2:
	"""
	Ecrire un algorithme qui demande un nombre de départ, et qui ensuite écrit la table de multiplication de ce nombre,
	présentée comme suit (cas où l'utilisateur entre le nombre 7) : Table de 7 : 7 x 1 = 7 7 x 2 = 14 7 x 3 = 21 … 7 x 10 = 70
	"""
	inum = 0
	def __init__(self):
		self.inum = input("enter a whole number: ")
		self.printable()
		
	def printable(self):
		self.inum = int(self.inum)
		i = 1
		while i < 11:
			print('{} x {} = {}'.format(self.inum, i, i * self.inum))
			i += 1

class EX3:
	"""
	Ecrire un algorithme qui demande un nombre de départ, et qui calcule sa factorielle.
	"""
	fact = 0
	def __init__(self):
		inum = input("enter a whole number to see the factorial of it: ")
		self.fact = HELP().factorielle(int(inum))
		print('{}! = {}'.format(inum, self.fact))

class HELP:		
	def factorielle(self, n):
		factor = 1
		for i in range(1, n + 1):
			factor *= i
		return factor

class EX4:
	""" Écrire un algorithme qui permette de connaître ses chances de gagner au tiercé, quarté, quinté et autres impôts volontaires.
	On demande à l’utilisateur le nombre de chevaux partants, et le nombre de chevaux joués.
	Les deux messages affichés devront être :
	Dans l’ordre : une chance sur X de gagner
	Dans le désordre : une chance sur Y de gagner
	X et Y nous sont donnés par la formule suivante, si n est le nombre de chevaux partants et p le nombre de chevaux joués :
	X = n! / (n - p)!
	Y = n! / (p! * (n – p)!)
	"""
	def __init__(self):
		n = input("le nombre de chevaux partants: ")
		p = input("le nombre de chevaux joués: ")
		x, y = self.chance(int(n), int(p))
		print('dans l\'ordre: une chanse à gagner sur {} = {:.2f}%'.format(x, 100./x))
		print('dans le désordre: une chance de gagner sur {} = {:.2f}%'.format(y, 100./y))

	def chance(self, n, p):
		h = HELP()
		x = h.factorielle(n)
		x /= h.factorielle(n - p)
		y = x / h.factorielle(p)
		return x, y

class EX5:
	"""
	Faire un algorithme qui détermine la longueur d’une chaîne de caractères.
	"""
	def __init__(self, arg1):
		self.chaine = arg1
		print('string logeueur build-in {}'.format(len(self.chaine))) # build-in function
		print('string longueur custom {}'.format(self.longueur(self.chaine))) # custom function

	def longueur(self, txt):
		result = 0
		for char in txt:
			result += 1
		return result

class EX6:
	""" Faire une fonction de concaténation (ajoute à la fin de la première chaîne de caractères le contenu de la deuxième chaîne de caractères.)
	Faire une fonction de Comparaison qui compare deux chaînes de caractères suivant l’ordre lexicographique.
	Faire une fonction qui efface une partie de la chaîne en spécifiant une longueur d’effacement et un indice à partir duquel il faut effacer.
	"""
	def __init__(self, arg1, arg2):
		self.chaine = arg1 + arg2
		self.comparer(arg1, arg2)

	def comparer(self, c1, c2):
		if c1 == c2: print('{} == {}'.format(c1, c2))
		elif c1 > c2: print('{} > {}'.format(c1, c2))
		elif c1 < c2: print('{} < {}'.format(c1, c2))
		else: print('attention cela ne doit pas arriver {} ? {}'.format(c1, c2))

	def effacer(self, mot, longeur, position):
		if position > len(mot): return mot
		word = mot[:position - 1] + mot[position + longeur - 1:]
		print(word)
		return word

class EX7:
	"""
	Ecrire un algorithme qui affiche la moyenne d’une suite d’entiers
	"""
	def __init__(self):
		intarray = [2, 3, 7, 45, 15, 5]
		print('moyenne: {:.2f}'.format(self.moyenne(intarray)))

	def moyenne(self, arr):
		sum = 0
		for a in arr:
			sum += a
		return sum / len(arr)

class EX8:
	"""
	Ecrire une fonction max3 qui retourne le maximum de trois entiers
	Ecrire une fonction min3 qui retourne le minimum de trois entiers
	Ecrire une fonction max2 qui retourne le maximum de deux entiers
	Ecrire une fonction max3 qui retourne le maximum de trois entiers en faisant appel à max2
	"""
	def __init__(self):
		i1 = 5
		i2 = 18
		i3 = 104
		print('max3', self.max3(i1, i2, i3))
		print('min3', self.min3(i1, i2, i3))
		print('max2', self.max2(i1, i2))
		print('max3parmax2', self.max3parmax2(i1, i2, i3))

	def max3(self, i1, i2, i3):
		max = i1
		if max < i2: max = i2
		if max < i3: max = i3
		return max
	
	def min3(self, i1, i2, i3):
		min = i1
		if min > i2: min = i2
		if min > i3: min = i3
		return min

	def max2(self, i1, i2):
		max = i1
		if max < i2: max = i2
		return max
	
	def max3parmax2(self, i1, i2, i3):
		i4 = self.max2(i1, i2)
		max = self.max2(i3, i4)
		return max

class EX9:
	""" 
	Ecrire une action qui fournit les félicitations ou l’ajournement d’un élève suivant sa note en utilisant Si-alors-sinon.
	"""
	action = {2 : 'ajournement', 3 : 'ajournement', 4 : 'félicitations', 5 : 'félicitations', 6 : 'félicitations'}

	def __init__(self, note = 4):
		# self.message = self.action[note]
		if note < 4: self.message = self.action[2]
		else: self.message = self.action[6]
		self.sendemail()

	def sendemail(self):
		print(self.message)



# ex9 = EX9(3)
# ex8 = EX8()
# ex7 = EX7()
# ex6 = EX6('beau', 'coup')
# ex6.effacer('verylongword', 4, 5)
# ex5 = EX5('vfdvdscds')	
# ex4 = EX4()
ex3 = EX3()
# ex2 = EX2()
# ex1 = EX1()



exit(0)
