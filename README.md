# Py-Study-up
Python技能提高总结

表格一：
Bandwidth [MHz]	carrierBandwidth	Range		Carrier centre	Carrier centre	point A	absoluteFrequencyPointA	offsetToCarrier [Carrier PRBs]	SS block SCS	GSCN	absoluteFrequencySSB		CORESET#0 Offset	CORESET#0 Index	offsetToPointA
	[PRBs]			[MHz]	[ARFCN]	[MHz]	[ARFCN]		[kHz]		[ARFCN]		[RBs]	Note 1	(SIB1)
													Note 1		[PRBs]
															Note 1
5	25	Downlink	Low	2112.5	422500	2110.25	422050	0	15	5279	422410	0	0	0	0
			Mid	2140	428000	2119.39	423878	102		5350	427970	20	0	0	102
			High	2167.5	433500	2074.53	414906	504		5418	433470	20	0	0	504
		Uplink	Low	1922.5	384500	1920.25	384050	0	-	-	-	-	-	-	-
			Mid	1950	390000	1857.03	371406	504		-	-	-	-	-	-
			High	1977.5	395500	1974.17	394834	6		-	-	-	-	-	-
10	52	Downlink	Low	2115	423000	2110.32	422064	0	15	5280	422430	2	0	0	0
			Mid	2140	428000	2116.96	423392	102		5344	427490	22	0	0	102
			High	2165	433000	2069.6	413920	504		5405	432490	22	0	0	504
		Uplink	Low	1925	385000	1920.32	384064	0	-	-	-	-	-	-	-
			Mid	1950	390000	1854.6	370920	504		-	-	-	-	-	-
			High	1975	395000	1969.24	393848	6		-	-	-	-	-	-
15	79	Downlink	Low	2117.5	423500	2110.39	422078	0	15	5281	422450	4	0	0	0
			Mid	2140	428000	2114.53	422906	102		5338	427010	0	2	1	104
			High	2162.5	432500	2064.67	412934	504		5395	431570	20	2	1	506
		Uplink	Low	1927.5	385500	1920.39	384078	0	-	-	-	-	-	-	-
			Mid	1950	390000	1852.17	370434	504		-	-	-	-	-	-
			High	1972.5	394500	1964.31	392862	6		-	-	-	-	-	-
20	106	Downlink	Low	2120	424000	2110.46	422092	0	15	5282	422650	18	4	2	4
			Mid	2140	428000	2112.1	422420	102		5332	426530	2	2	1	104
			High	2160	432000	2059.74	411948	504		5382	430590	22	2	1	506
		Uplink	Low	1930	386000	1920.46	384092	0	-	-	-	-	-	-	-
			Mid	1950	390000	1849.74	369948	504		-	-	-	-	-	-
			High	1970	394000	1959.38	391876	6		-	-	-	-	-	-
Note 1: The CORESET#0 Index and the associated CORESET#0 Offset refers to Table 13-1 in TS 38.213 [22]. The value of CORESET#0 Index is signalled in the four most significant bits of the IE pdcch-ConfigSIB1 in the MIB. The offsetToPointA IE is expressed in units of resource blocks assuming 15 kHz subcarrier spacing for FR1 and 60 kHz subcarrier spacing for FR2.															
