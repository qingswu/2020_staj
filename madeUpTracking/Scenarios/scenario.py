# -*- coding: utf-8 -*-
import sys
sys.path.append("./Scenarios")
import scenarioGenerator as scenario
import numpy as np


"""

    Scenario 0: Single object with no corruptions

"""


stds_0 = [1]
objectPathCorners_0 = [([55, 23, 51], [56,9,20])] 

# objectPathCorners_0 = [(None)] 

corruptions_0 = [None]
stepSizes_0 = [0.4]
colors_0 = [("b", "g")]

scenario_0 = scenario.Scenario(stds_0, objectPathCorners_0, corruptions_0, stepSizes_0, colors_0)

#scenario_0.plotScenario()


a = 3

######################################################

"""

    Scenario 1: Single object with corruptions

"""
stds_1 = [1]
objectPathCorners_1 = [([55, 23, 51], [56,9,20])] 
corruptions_1 = [(3, 4)]
stepSizes_1 = [0.4]
colors_1 = [("b", "g")]

scenario_1 = scenario.Scenario(stds_1, objectPathCorners_1, corruptions_1, stepSizes_1, colors_1)

#scenario_1.plotScenario()


######################################################

"""

    Scenario 2: 2 object with no corruptions

"""

stds_2 = [1.5, 1]
objectPathCorners_2 = [ ([0, 25, 50], [50, 10, 0]), ([50, 25, 0], [50, 10, 0]) ] 
corruptions_2 = [None, None]
stepSizes_2 = [0.4, 0.4]
colors_2 = [("b", "g"), ("k", "c")]

scenario_2 = scenario.Scenario(stds_2, objectPathCorners_2, corruptions_2, stepSizes_2, colors_2)

#scenario_2.plotScenario()






######################################################


"""

    Scenario 3: 2 object with corruptions

"""
stds_3 = [3, 2]
objectPathCorners_3 = [ ([55, 23, 51], [56,9,20]), None ] 
corruptions_3 = [None, None]
stepSizes_3 = [0.4, None]
colors_3 = [("b", "g"), None]

scenario_3 = scenario.Scenario(stds_3, objectPathCorners_3, corruptions_3, stepSizes_3, colors_3)

#scenario_3.plotScenario()




######################################################

"""

    Scenario 4: Single object with no corruptions

"""


stds_4 = [2]
objectPathCorners_4 = [([0, 20, 1000], [0,20,1000])] 
circleX = [6.123233995736766e-15, 4.710645070964268, 9.410831331851428, 14.09012319375828, 18.738131458572475, 23.344536385590548, 27.899110603922928, 32.39174181981494, 36.81245526846781, 41.15143586051089, 45.39904997395468, 49.54586684324075, 53.582679497899655, 57.50052520432786, 61.29070536529765, 64.94480483301837, 68.45471059286886, 71.81262977631889, 75.01110696304596, 78.04304073383297, 80.90169943749474, 83.58073613682703, 86.07420270039437, 88.37656300886934, 90.48270524660195, 92.38795325112868, 94.08807689542255, 95.579301479833, 96.85831611286311, 97.92228106217658, 98.76883405951378, 99.39609554551797, 99.80267284282715, 99.98766324816606, 99.95065603657316, 99.6917333733128, 99.21147013144778, 98.5109326154774, 97.59167619387475, 96.45574184577981, 95.10565162951535, 93.54440308298673, 91.77546256839811, 89.80275757606157, 87.63066800438637, 85.26401643540922, 82.7080574274562, 79.96846584870906, 77.05132427757894, 73.96310949786098, 70.71067811865476, 67.30125135097735, 63.74239897486898, 60.04202253258843, 56.20833778521308, 52.24985647159489, 48.17536741017155, 43.993916985591525, 39.7147890634781, 35.34748437792573, 30.901699437494745, 26.38730499653732, 21.81432413965427, 17.192910027940993, 12.533323356430447, 7.8459095727845, 3.1410759078128616, -1.5707317311820526, -6.279051952931296, -10.973431109104501, -15.643446504023082, -20.278729535651216, -24.86898871648546, -29.404032523230356, -33.873792024529116, -38.268343236508976, -42.57792915650723, -46.792981426057324, -50.90414157503709, -54.90228179981316, -58.7785252292473, -62.52426563357049, -66.13118653236518, -69.5912796592314, -72.89686274214114, -76.04059656000305, -79.01550123756904, -81.81497174250232, -84.43279255020148, -86.86315144381909, -89.10065241883677, -91.14032766354451, -92.97764858882512, -94.60853588275452, -96.02936856769429, -97.23699203976764, -98.22872507286885, -99.00236577165575, -99.556196460308, -99.88898749619699]
circleY = [100.0, 99.888987496197, 99.556196460308, 99.00236577165575, 98.22872507286885, 97.23699203976766, 96.0293685676943, 94.60853588275452, 92.97764858882513, 91.14032766354453, 89.10065241883677, 86.86315144381912, 84.43279255020151, 81.81497174250234, 79.01550123756904, 76.0405965600031, 72.89686274214115, 69.59127965923145, 66.13118653236518, 62.52426563357052, 58.778525229247315, 54.90228179981318, 50.90414157503713, 46.792981426057345, 42.577929156507274, 38.268343236508976, 33.873792024529145, 29.404032523230406, 24.86898871648549, 20.278729535651266, 15.643446504023087, 10.973431109104531, 6.279051952931345, 1.5707317311820808, -3.141075907812812, -7.845909572784494, -12.53332335643042, -17.192910027940943, -21.814324139654243, -26.38730499653727, -30.901699437494738, -35.34748437792571, -39.71478906347805, -43.99391698559152, -48.17536741017151, -52.24985647159488, -56.20833778521303, -60.04202253258839, -63.74239897486894, -67.30125135097732, -70.71067811865474, -73.96310949786094, -77.05132427757891, -79.96846584870903, -82.70805742745617, -85.26401643540922, -87.63066800438635, -89.80275757606155, -91.7754625683981, -93.54440308298673, -95.10565162951535, -96.4557418457798, -97.59167619387473, -98.51093261547739, -99.21147013144778, -99.6917333733128, -99.95065603657316, -99.98766324816606, -99.80267284282715, -99.39609554551797, -98.76883405951378, -97.92228106217658, -96.85831611286312, -95.57930147983302, -94.08807689542256, -92.38795325112868, -90.48270524660197, -88.37656300886934, -86.07420270039438, -83.58073613682704, -80.90169943749474, -78.043040733833, -75.01110696304598, -71.81262977631891, -68.45471059286888, -64.94480483301841, -61.29070536529764, -57.50052520432787, -53.5826794978997, -49.545866843240816, -45.39904997395469, -41.15143586051091, -36.81245526846785, -32.391741819814946, -27.899110603922956, -23.344536385590594, -18.738131458572543, -14.090123193758286, -9.41083133185148, -4.71064507096434]
#objectPathCorners_4 = [(circleX, circleY)] 

# objectPathCorners_4 = [(None)] 

corruptions_4 = [None]
stepSizes_4 = [0.4]
colors_4 = [("b", "g")]

scenario_4 = scenario.Scenario(stds_4, objectPathCorners_4, corruptions_4, stepSizes_4, colors_4)

#scenario_4.plotScenario()


a = 3

######################################################

"""

    Scenario 5: 1 complicated path object with no corruptions

"""
stds_5 = [1.5]
objectPathCorners_5 = [ None ] 
corruptions_5 = [None]
stepSizes_5 = [0.4]
colors_5 = [("b", "g")]

scenario_5 = scenario.Scenario(stds_5, objectPathCorners_5, corruptions_5, stepSizes_5, colors_5)

#scenario_3.plotScenario()
