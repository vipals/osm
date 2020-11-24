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

	C[u"б"]=u"b"; C[u"в"]=u"v"; C[u"г"]=u"g"; C[u"д"]=u"d"; C[u"ж"]=u"j"; C[u"з"]=u"z"; C[u"й"]=u"ı"; C[u"к"]=u"k";
	C[u"л"]=u"l"; C[u"м"]=u"m"; C[u"н"]=u"n"; C[u"п"]=u"p"; C[u"р"]=u"r"; C[u"с"]=u"s"; C[u"т"]=u"t"; C[u"ф"]=u"f"; 
	C[u"х"]=u"h"; C[u"ч"]=u"ch"; C[u"ц"]=u"ts"; C[u"ш"]=u"sh"; C[u"ь"]=u""; C[u"щ"]=u"shch";
	C[u"ғ"]=u"ǵ"; C[u"қ"]=u"q"; C[u"ң"]=u"ń"; C[u"һ"]=u"h";

	V[APO]=u""; V[APO2]=u""; V[SOFT]=u"";
	V[u"а"]=u"a"; V[u"э"]=u"e"; V[u"о"]=u"o"; V[u"у"]=u"ý"; V[u"и"]=u"i"; V[u"і"]=u"i"; V[u"ы"]=u"y";
	V[u"ә"]=u"á"; V[u"ө"]=u"ó"; V[u"ұ"]=u"u"; V[u"ү"]=u"ú";
	
	I[u"я"]=u"ıa"; I[u"е"]=u"e"; I[u"ё"]=u"ıo"; I[u"ю"]=u"ıu";
	
	uword = word
	
	for i in xrange(len(uword)):
		curr = uword[i];
		low = curr.lower();
		if i+1 < len(uword):
			nxt = uword[i+1];
		result = '';
		if (low in C):
			result = C[low];
		else:
			result = V.get(low, I.get(low, curr))
		
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


text = u"Барлық адамдар тумысынан азат және қадір-қасиеті мен құқықтары тең болып дүниеге келеді. \
	Адамдарға ақыл-парасат, ар-ождан берілген, сондықтан олар бір-бірімен туыстық, \
	бауырмалдық қарым-қатынас жасаулары тиіс.."

#text = u"Вераб'ёвічы"

#if len(sys.argv) > 1:
	#text = sys.argv[1]

#print transliterate(text)
