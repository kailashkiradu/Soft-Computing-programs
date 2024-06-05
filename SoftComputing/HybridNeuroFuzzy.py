import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Define input variables (sensor readings)
distance_to_object = ctrl.Antecedent(np.arange(0, 101, 1), 'distance_to_object')
vehicle_speed = ctrl.Antecedent(np.arange(0, 101, 1), 'vehicle_speed')
road_condition = ctrl.Antecedent(np.arange(0, 11, 1), 'road_condition')

# Define output variable (control action)
steering_angle = ctrl.Consequent(np.arange(-30, 31, 1), 'steering_angle')

# Define membership functions for input variables
distance_to_object['close'] = fuzz.trimf(distance_to_object.universe, [0, 0, 50])
distance_to_object['medium'] = fuzz.trimf(distance_to_object.universe, [0, 50, 100])
distance_to_object['far'] = fuzz.trimf(distance_to_object.universe, [50, 100, 100])

vehicle_speed['slow'] = fuzz.trimf(vehicle_speed.universe, [0, 0, 50])
vehicle_speed['moderate'] = fuzz.trimf(vehicle_speed.universe, [0, 50, 100])
vehicle_speed['fast'] = fuzz.trimf(vehicle_speed.universe, [50, 100, 100])

road_condition['poor'] = fuzz.trimf(road_condition.universe, [0, 0, 5])
road_condition['average'] = fuzz.trimf(road_condition.universe, [0, 5, 10])
road_condition['good'] = fuzz.trimf(road_condition.universe, [5, 10, 10])

# Define membership functions for output variable
steering_angle['left'] = fuzz.trimf(steering_angle.universe, [-30, -30, 0])
steering_angle['straight'] = fuzz.trimf(steering_angle.universe, [-15, 0, 15])
steering_angle['right'] = fuzz.trimf(steering_angle.universe, [0, 30, 30])

# Define fuzzy rules
rule1 = ctrl.Rule(distance_to_object['close'] & vehicle_speed['slow'], steering_angle['left'])
rule2 = ctrl.Rule(distance_to_object['medium'] & vehicle_speed['moderate'] & road_condition['average'], steering_angle['straight'])
rule3 = ctrl.Rule(distance_to_object['far'] | vehicle_speed['fast'] | road_condition['good'], steering_angle['right'])

# Create control system
control_system = ctrl.ControlSystem([rule1, rule2, rule3])
vehicle_ctrl = ctrl.ControlSystemSimulation(control_system)

# Provide inputs to the system (adjust these values as needed)
vehicle_ctrl.input['distance_to_object'] = 40
vehicle_ctrl.input['vehicle_speed'] = 70
vehicle_ctrl.input['road_condition'] = 8

# Compute the output
vehicle_ctrl.compute()

# Print the output (steering angle)
print("Predicted steering angle:", vehicle_ctrl.output['steering_angle'])
