# XCSoarMapGenDebug
'back-end' Python code from https://github.com/XCSoar/mapgen/

This repo was constructed to help debug problems with the web-based XCSoar Map Generator (MapGen).  Currently, MapGen rejects all waypoint files as 'invalid', which is a major PITA as this is the very best way of constructing an XCSoar map (.XCM) file that is guaranteed to contain all contest waypoints for that scenery.
The repo uses the python 'back-end' code directly, but without any of the front-end GUI stuff.  My thinking is that I (or someone else) can probably figure out why MapGen doesn't like .CUP files anymore, or failing that - at least show that it is something besides the python code
On my Debian Linux box, I have all the python files and the sample WaypointFile.Cup file in the same directory (~/MapGenDebug). Here is the output from a sample run:

-rw-rw-r--  1 frank frank 4124 Feb 26 21:52 XCSoarMapGen.py
frank@M6700:~$ cd MapGenDebug/
frank@M6700:~/MapGenDebug$ python3 XCSoarMapGen.py 
length = 59, entry = name,code,country,lat,lon,elev,style,rwdir,rwlen,freq,desc

length = 57, entry = "Aarau Gare",Aarau Ga,,4723.500N,00803.117E,386.0m,1,,,,

length = 63, entry = "Aarau Schachen C",Aarau Sc,,4723.276N,00802.057E,368.0m,1,,,,

length = 59, entry = "Aarberg Gare",Aarberg ,,4702.650N,00716.700E,450.0m,1,,,,

length = 61, entry = "Abfaltersb Chp",Abfalter,,4645.518N,01232.392E,952.0m,1,,,,

length = 62, entry = "Achenkirch Nord",Achenkir,,4732.193N,01142.407E,902.0m,1,,,,

length = 62, entry = "Achenkirch Sued",Achenkir,,4730.807N,01142.078E,938.0m,1,,,,

length = 63, entry = "Achensee Nordspi",Achensee,,4730.083N,01142.450E,932.0m,1,,,,

length = 63, entry = "Achensee Sued Sp",Achensee,,4725.550N,01144.067E,928.0m,1,,,,

length = 63, entry = "Achenwald Klammb",Achenwal,,4733.933N,01140.383E,840.0m,1,,,,

length = 61, entry = "Adamello Cima",Adamello,,4609.000N,01030.000E,3280.0m,1,,,,

length = 57, entry = "Adige Sce",Adige Sc,,4648.573N,01031.678E,1498.0m,1,,,,

length = 57, entry = "Admont Chp",Admont C,,4734.994N,01427.156E,630.0m,1,,,,

length = 63, entry = "Admont Stift Kir",Admont S,,4734.517N,01427.700E,640.0m,1,,,,

length = 60, entry = "Admonterhaus",Admonter,,4737.917N,01429.483E,1712.0m,1,,,,

Aarau Gare, 47.391666666666666, 8.05195, 386, None
Aarau Schachen C, 47.387933333333336, 8.034283333333333, 368, None
Aarberg Gare, 47.04416666666667, 7.278333333333333, 450, None
Abfaltersb Chp, 46.758633333333336, 12.539866666666667, 952, None
Achenkirch Nord, 47.53655, 11.706783333333334, 902, None
Achenkirch Sued, 47.51345, 11.7013, 938, None
Achensee Nordspi, 47.50138333333334, 11.7075, 932, None
Achensee Sued Sp, 47.42583333333334, 11.73445, 928, None
Achenwald Klammb, 47.56555, 11.67305, 840, None
Adamello Cima, 46.15, 10.5, 3280, None
Adige Sce, 46.80955, 10.527966666666666, 1498, None
Admont Chp, 47.58323333333333, 14.4526, 630, None
Admont Stift Kir, 47.57528333333333, 14.461666666666666, 640, None
Admonterhaus, 47.63195, 14.491383333333333, 1712, None
frank@M6700:~/MapGenDebug$ ^C

This shows that the 'parse_seeyou_waypoints(Waypoint_Strings)' function from the MapGen repo properly parses waypoint strings from a Condor2 waypoint file, so its probably not the culprit here.

27 Feb 2024: Added XCSoarMapServerDebug.py - when run this emulates most server operations using 'WaypointFile.cup' as input

