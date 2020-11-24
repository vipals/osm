#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

def transliterate(word):
	C = {};
	V = {};
	I = {};
	J = {};
	P = {};
	out = '';
	prev = u"а";
	SOFT = u"ь";
	APO = u"'";
	APO2 = u"’";

	C[u"б"]=u"b"; C[u"в"]=u"v"; C[u"г"]=u"h"; C[u"д"]=u"d"; C[u"ж"]=u"ž"; C[u"з"]=u"z"; C[u"й"]=u"j"; C[u"к"]=u"k";
	C[u"л"]=u"l"; C[u"м"]=u"m"; C[u"н"]=u"n"; C[u"п"]=u"p"; C[u"р"]=u"r"; C[u"с"]=u"s"; C[u"т"]=u"t"; C[u"ф"]=u"f"; 
	C[u"х"]=u"ch"; C[u"ч"]=u"č"; C[u"ц"]=u"c"; C[u"ш"]=u"š"; C[u"ь"]=u""; C[u"ґ"]=u"g"; C[u"щ"]=u"šč";
	V[APO]=u""; V[APO2]=u""; V[SOFT]=u"";
	V[u"а"]=u"a"; V[u"э"]=u"e"; V[u"о"]=u"o"; V[u"у"]=u"u"; V[u"и"]=u"i"; V[u"і"]=u"i"; V[u"ы"]=u"y"; V[u"ў"]=u"ŭ";
	
	I[u"я"]=u"ia"; I[u"е"]=u"ie"; I[u"ё"]=u"io"; I[u"ю"]=u"iu";
	J[u"я"]=u"ja"; J[u"е"]=u"je"; J[u"ё"]=u"jo"; J[u"ю"]=u"ju";
	P[u"з"]=u"ź"; P[u"л"]=u"ĺ"; P[u"н"]=u"ń"; P[u"с"]=u"ś"; P[u"ц"]=u"ć";
	
	uword = word
	
	for i in xrange(len(uword)):
		curr = uword[i];
		low = curr.lower();
		if i+1 < len(uword):
			nxt = uword[i+1];
		result = '';
		if (low in C):
			if (nxt.lower() == SOFT):
				result = P.get(low, C[low])
			else:
				result = C[low];
		else:
			if (prev in C):
				result = V.get(low, I.get(low, curr))
			else:
				result = V.get(low, J.get(low, curr))
			if ((prev == APO or prev == APO2) and (low == u"i" or low == u"и")):
				result = u"ji";
		
		prev = low;
		if (curr == low):
			#print result
			out += result;
		else:
			if (nxt == nxt.lower()):
				out += result.capitalize();
			else:
				out += result.upper();
	return out;


text = u"Аршанскі, Бешанковічы, Віцебск, Гомель, Гаўя, Добруш, Ельск, \
Венцавічы, Ёды, Вераб'ёвічы, Мёры, Жодзішкі, Зэльва, Iванава, Iўе, \
Лагойск, Круглае, Лошыца, Магілёў, Нясвіж, Орша, Паставы, Рагачоў, \
Светлагорск, Талачын, Узда, Шаркаўшчына, Фаніпаль, Хоцімск, Цёмны Лес, \
Чавусы, Шуміліна, Чыгірынка, Чэрвень, Друць, Чачэрск, Юхнаўка, \
Гаюціна, Цюрлі, Любонічы, Ямнае, Баяры, Валяр'яны, Вязынка."

#text = u"Вераб'ёвічы"

#if len(sys.argv) > 1:
	#text = sys.argv[1]

#print transliterate(text)
