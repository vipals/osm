#!/usr/bin/python
# -*- coding: utf-8 -*-

from latin import transliterate
import codecs

out = codecs.open('data_new.osm', 'w', 'utf-8')

with codecs.open('data.osm', 'r', 'utf-8') as f:
	line = f.readline()
	while line:
		out.write(line)
		if "\"name:kk\"" in line:
			res=transliterate(line.replace("name:kk", "int_name"))
			out.write(res)
		line = f.readline()
out.close()
