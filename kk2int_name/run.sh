#!/bin/sh

echo "data=node[\"addr:country\"=\"KZ\"][\"name:kk\"~\".\"][\"int_name\"!~\".\"];out meta;" > query.osm

wget --post-file=query.osm -O data.osm https://overpass-api.de/api/interpreter

python convert.py

sed -i 's/node id=/node action=\"modify\" id=/g' data_new.osm
diff data.osm data_new.osm | grep "^>" | sort -u | grep -v modify
