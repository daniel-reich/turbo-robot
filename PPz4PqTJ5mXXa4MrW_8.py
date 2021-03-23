"""


The **Ulam sequence** starts with:

    ulam = [1, 2]

The next number in the sequence is the smallest positive number that is equal
to the _sum of 2 distinct numbers_ (that are already in the sequence) _exactly
one way_. Trivially, this is 3, as there are only 2 numbers in the starting
sequence.

    ulam = [1, 2, 3]

The next number is 4, which is the sum of 3+1. 4 is also 2+2, but this
equation does not count, as the 2 addends have to be distinct.

    ulam = [1, 2, 3, 4]

The next number _cannot be_ 5, as 5 = 1 + 4, but also 5 = 2 + 3. There should
only be one way to make an Ulam number from 2 distinct addends found in the
sequence. The next number is 6 (2+4). There are 2 ways to make 7 (1+6 or 3+4),
so the next is 8 (2+6). And so on.

    ulam = [1, 2, 3, 4, 6, 8, 11, 13, 16, 18, 26, 28, 36, 38, 47, 48, 53, …]

Create a function that takes a number n and returns the nth number in the Ulam
sequence.

### Examples

    ulam(4) ➞ 4
    
    ulam(9) ➞ 16
    
    ulam(206) ➞ 1856

### Notes

N/A

"""

seq = [1, 2, 3, 4, 6, 8, 11, 13, 16, 18, 26, 28, 36, 38, 47, 48, 53, 57, 62, 69, 72, 77, 82, 87, 97, 99, 102, 106, 114, 126, 131, 138, 145, 148, 155, 175, 177, 180, 182, 189, 197, 206, 209, 219, 221, 236, 238, 241, 243, 253, 258, 260, 273, 282, 309, 316, 319, 324, 339, 341, 356, 358, 363, 370, 382, 390, 400, 402, 409, 412, 414, 429, 431, 434, 441, 451, 456, 483, 485, 497, 502, 522, 524, 544, 546, 566, 568, 585, 602, 605, 607, 612, 624, 627, 646, 668, 673, 685, 688, 690, 695, 720, 722, 732, 734, 739, 751, 781, 783, 798, 800, 820, 847, 849, 861, 864, 866, 891, 893, 905, 927, 949, 983, 986, 991, 1018, 1020, 1023, 1025, 1030, 1032, 1035, 1037, 1052, 1079, 1081, 1101, 1103, 1125, 1155, 1157, 1164, 1167, 1169, 1186, 1191, 1208, 1230, 1252, 1257, 1296, 1308, 1311, 1313, 1335, 1338, 1340, 1355, 1360, 1377, 1387, 1389, 1404, 1406, 1428, 1431, 1433, 1462, 1465, 1470, 1472, 1489, 1492, 1509, 1514, 1516, 1531, 1536, 1538, 1550, 1553, 1594, 1602, 1604, 1616, 1641, 1643, 1646, 1648, 1660, 1682, 1707, 1709, 1721, 1724, 1748, 1765, 1770, 1790, 1792, 1812, 1814, 1834, 1836, 1853, 1856, 1858, 1900, 1902, 1919, 1941, 1944, 1946, 1966, 1968, 1985, 2010, 2012, 2032, 2034, 2054, 2056, 2090, 2093, 2095, 2112, 2115, 2117, 2134, 2156, 2178, 2247, 2249, 2252, 2254, 2288, 2327, 2330, 2332, 2354, 2371, 2393, 2418, 2420, 2445, 2447, 2462, 2464, 2481, 2484, 2486, 2511, 2513, 2525, 2550, 2552, 2572, 2574, 2581, 2584, 2589, 2613, 2616, 2618, 2628, 2630, 2633, 2635, 2650, 2660, 2662, 2674, 2696, 2721, 2723, 2748, 2750, 2762, 2787, 2789, 2809, 2811, 2814, 2816, 2831, 2833, 2897, 2899, 2916, 2919, 2921, 2985, 2987, 3029, 3031, 3038, 3041, 3043, 3065, 3068, 3070, 3085, 3090, 3092, 3107, 3109, 3131, 3153, 3205, 3207, 3214, 3217, 3219, 3236, 3239, 3261, 3263, 3288, 3290, 3305, 3368, 3371, 3373, 3390, 3393, 3395, 3415, 3417, 3451, 3454, 3456, 3473, 3476, 3481, 3483, 3495, 3525, 3527, 3544, 3547, 3549, 3591, 3593, 3605, 3608, 3610, 3622, 3625, 3630, 3632, 3649, 3669, 3671, 3691, 3696, 3698, 3723, 3725, 3740, 3742, 3759, 3762, 3764, 3806, 3808, 3825, 3872, 3874, 3886, 3916, 3918, 3930, 3952, 3960, 3962, 3974, 3991, 3994, 4018, 4038, 4040, 4057, 4101, 4118, 4121, 4148, 4150, 4153, 4155, 4165, 4167, 4187, 4211, 4233, 4258, 4260, 4294, 4297, 4324, 4326, 4341, 4343, 4363, 4365, 4368, 4370, 4390, 4392, 4404, 4407, 4409, 4451, 4453, 4470, 4517, 4519, 4531, 4534, 4536, 4578, 4580, 4600, 4602, 4619, 4622, 4624, 4641, 4644, 4646, 4666, 4668, 4707, 4729, 4732, 4734, 4754, 4756, 4798, 4800, 4878, 4881, 4883, 4900, 4903, 4905, 4925, 4927, 4969, 4971, 4996, 4998, 5018, 5020, 5032, 5035, 5037, 5049, 5052, 5057, 5059, 5079, 5081, 5096, 5118, 5159, 5162, 5164, 5181, 5184, 5186, 5206, 5208, 5250, 5252, 5269, 5272, 5274, 5291, 5294, 5296, 5316, 5318, 5335, 5357, 5382, 5384, 5484, 5487, 5489, 5514, 5516, 5531, 5533, 5550, 5597, 5599, 5616, 5663, 5665, 5685, 5687, 5765, 5768, 5770, 5795, 5797, 5812, 5814, 5826, 5829, 5853, 5856, 5858, 5873, 5875, 5878, 5880, 5895, 5900, 5902, 5944, 5946, 6024, 6027, 6029, 6046, 6049, 6051, 6068, 6107, 6110, 6112, 6134, 6154, 6156, 6176, 6178, 6239, 6242, 6244, 6283, 6308, 6310, 6322, 6325, 6327, 6352, 6354, 6366, 6391, 6393, 6410, 6418, 6420, 6435, 6437, 6457, 6459, 6479, 6481, 6520, 6523, 6525, 6550, 6552, 6567, 6569, 6586, 6633, 6635, 6652, 6721, 6723, 6735, 6738, 6740, 6782, 6784, 6804, 6806, 6831, 6833, 6862, 6865, 6870, 6872, 6889, 6892, 6894, 6909, 6911, 6914, 6916, 6931, 6936, 6938, 6980, 6982, 7038, 7041, 7043, 7060, 7063, 7065, 7082, 7104, 7156, 7158, 7170, 7192, 7195, 7197, 7217, 7219, 7258, 7275, 7278, 7280, 7297, 7300, 7302, 7322, 7324, 7366, 7368, 7424, 7427, 7432, 7434, 7459, 7461, 7471, 7473, 7476, 7478, 7490, 7498, 7500, 7520, 7522, 7537, 7539, 7559, 7578, 7581, 7583, 7600, 7603, 7605, 7622, 7691, 7693, 7727, 7730, 7735, 7737, 7749, 7752, 7754, 7774, 7776, 7779, 7781, 7798, 7818, 7820, 7881, 7884, 7886, 7928, 7930, 7950, 7952, 7977, 7979, 8008, 8011, 8016, 8018, 8055, 8057, 8060, 8062, 8077, 8096, 8099, 8101, 8126, 8128, 8143, 8145, 8165, 8167, 8192, 8194, 8236, 8238, 8250, 8253, 8255, 8272, 8275, 8277, 8294, 8316, 8338, 8368, 8370, 8404, 8421, 8424, 8426, 8451, 8453, 8468, 8487, 8509, 8512, 8514, 8531, 8539, 8541, 8553, 8570, 8573, 8617, 8619, 8639, 8666, 8668, 8702, 8705, 8749, 8751, 8754, 8756, 8771, 8773, 8812, 8815, 8817, 8842, 8844, 8856, 8873, 8876, 8917, 8942, 8947, 8949, 8964, 8966, 8969, 8971, 8983, 9013, 9015, 9027, 9052, 9054, 9071, 9093, 9118, 9120, 9132, 9135, 9137, 9162, 9164, 9179, 9184, 9186, 9193, 9196, 9240, 9250, 9252, 9262, 9308, 9311, 9313, 9355, 9357, 9377, 9379, 9399, 9401, 9443, 9445, 9509, 9511, 9553, 9555, 9575, 9577, 9619, 9621, 9641, 9643, 9663, 9665, 9699, 9702, 9704, 9721, 9724, 9726, 9743, 9765, 9804, 9807, 9809, 9834, 9836, 9851, 9853, 9870, 9917, 9919, 9939, 9941, 9958, 9961, 9963, 9980, 9983, 9985, 10002, 10085, 10088, 10090, 10107, 10110, 10112, 10132, 10134, 10173, 10220, 10222, 10242, 10244, 10247, 10249, 10269, 10271, 10283, 10286, 10288, 10305, 10349, 10366, 10369, 10388, 10391, 10393, 10413, 10415, 10457, 10459, 10501, 10503, 10520, 10523, 10525, 10537, 10540, 10545, 10547, 10567, 10569, 10584, 10606, 10655, 10657, 10677, 10679, 10691, 10694, 10696, 10713, 10716, 10718, 10738, 10740, 10757, 10779, 10804, 10806, 10831, 10833, 10848, 10850, 10862, 10865, 10870, 10872, 10909, 10911, 10931, 10972, 10975, 10977, 10994, 10997, 10999, 11016, 11085, 11087, 11099, 11102, 11107, 11109, 11146, 11148, 11168, 11195, 11197, 11217, 11219, 11226, 11229, 11234, 11236, 11253, 11256, 11258, 11273, 11275, 11278, 11280, 11295, 11300, 11302, 11319, 11344, 11346, 11366, 11368, 11388, 11390, 11432, 11434, 11454, 11456, 11498, 11500, 11586, 11588, 11600, 11603, 11605, 11622, 11625, 11627, 11647, 11649, 11688, 11713, 11715, 11735, 11737, 11757, 11759, 11774, 11776, 11779, 11781, 11881, 11884, 11886, 11925, 11950, 11952, 11964, 11967, 11969, 11994, 11996, 12008, 12033, 12035, 12055, 12057, 12060, 12062, 12074, 12118, 12143, 12145, 12162, 12187, 12189, 12245, 12248, 12250, 12267, 12270, 12272, 12292, 12294]
​
def ulam(n):
    return seq[n-1]

