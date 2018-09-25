#!/usr/bin/env python3
# -*- coding:Utf-8 -*-

from random import randint
entiers = []
i=0
while len(entiers) < 25:
	i+=1
	entier = randint (1,100)
	if entier not in entiers:
		entiers.append(entier)
entiers.sort()
print(i, entiers)
