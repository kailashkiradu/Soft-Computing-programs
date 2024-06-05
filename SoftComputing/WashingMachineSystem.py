#pip install scikit-fuzzy

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Define input variables
dirtiness = ctrl.Antecedent(np.arange(0, 11, 1), 'dirtiness')
fabric_type = ctrl.Antecedent(np.arange(0, 11, 1), 'fabric_type')

# Define output variable
wash_time = ctrl.Consequent(np.arange(0, 101, 1), 'wash_time')

# Define membership functions for input variables
dirtiness['low'] = fuzz.trimf(dirtiness.universe, [0, 0, 5])
dirtiness['medium'] = fuzz.trimf(dirtiness.universe, [0, 5, 10])
dirtiness['high'] = fuzz.trimf(dirtiness.universe, [5, 10, 10])

fabric_type['delicate'] = fuzz.trimf(fabric_type.universe, [0, 0, 5])
fabric_type['normal'] = fuzz.trimf(fabric_type.universe, [0, 5, 10])
fabric_type['heavy_duty'] = fuzz.trimf(fabric_type.universe, [5, 10, 10])

# Define membership functions for output variable
wash_time['short'] = fuzz.trimf(wash_time.universe, [0, 0, 50])
wash_time['medium'] = fuzz.trimf(wash_time.universe, [0, 50, 100])
wash_time['long'] = fuzz.trimf(wash_time.universe, [50, 100, 100])

# Define fuzzy rules
rule1 = ctrl.Rule(dirtiness['low'] & fabric_type['delicate'], wash_time['short'])
rule2 = ctrl.Rule(dirtiness['medium'] & fabric_type['delicate'], wash_time['medium'])
rule3 = ctrl.Rule(dirtiness['high'] & fabric_type['delicate'], wash_time['long'])

rule4 = ctrl.Rule(dirtiness['low'] & fabric_type['normal'], wash_time['medium'])
rule5 = ctrl.Rule(dirtiness['medium'] & fabric_type['normal'], wash_time['medium'])
rule6 = ctrl.Rule(dirtiness['high'] & fabric_type['normal'], wash_time['long'])

rule7 = ctrl.Rule(dirtiness['low'] & fabric_type['heavy_duty'], wash_time['medium'])
rule8 = ctrl.Rule(dirtiness['medium'] & fabric_type['heavy_duty'], wash_time['long'])
rule9 = ctrl.Rule(dirtiness['high'] & fabric_type['heavy_duty'], wash_time['long'])

# Create control system
washing_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9])
washing_sim = ctrl.ControlSystemSimulation(washing_ctrl)

# Provide inputs to the system
washing_sim.input['dirtiness'] = 7
washing_sim.input['fabric_type'] = 8

# Compute the output
washing_sim.compute()

# Print the output
print("Predicted wash time:", washing_sim.output['wash_time'])
