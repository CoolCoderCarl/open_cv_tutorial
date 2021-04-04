from numpy import exp, array, random, dot

### LEARNING DATA FOR NEURON
training_set_inputs = array([[0, 1, 1], [3, 1, 2], [3, 2, 1], [0, 3, 1], [2, 3, 2]])
print("INPUT MATRIX")
print(training_set_inputs)
### MATRIX TRANSPOSING
### IF U WANT TO DELETE .T THEN SET (3, 4) IN synaptic_weights VARIABLE
training_set_outputs = array([[0, 3, 3, 0, 2]]).T
print("OUTPUT RESULTS")
print(training_set_outputs)
random.seed(1)
### IF U WANT TO MAKE SOME CHANGES TO RESULT U NEED TO CHANGE FIRST AND LAST DIGITS
### IF U CHANGE (3, 1) TO (3, 4) IT SHOW MATRIX WITH 4 DIFFIRENT DIGITS
synaptic_weights = 2 * random.random((3, 1)) - 1
print("SYNAPTIC WEIGHTS AT START")
print(synaptic_weights)

### RESULT BECOME MORE ACCURATE IF U INCREASE THE NUMBERS OF THE ROUNDS
for iteration in range(100000):
    ### EXP = EXPONENTIATION
    ### DOT = MATRIX MULTIPLICATION
    output = 3 / (1 + exp(-(dot(training_set_inputs, synaptic_weights))))
    ### REWRITE synaptic_weights BY MULTIPLICATION TRANSPARENT INPUTS AND OUTPUTS
    ### FORMULA CALLED "Weighted by mistake" AND CONTAINS SECOND PART STARTED AFTER COMMA
    ### SECOND PART OF FORMULA CALLED "Sigmode Gradient"
    synaptic_weights += dot(training_set_inputs.T, (training_set_outputs - output) * output * (1 - output))
    ### IF UNCOMMENT STRINGS BELOW U WILL SEE ALL IN-BETWEEN RESULTS. THINK TWICE
    #print("NEW SYNAPTIC WEIGHTS")
    #print(synaptic_weights)

print("RESULT")
### HERE WE DIVIDE 3 (1, in original) ON 1 PLUS EXPONENTIONAL MULTIPLICATION OF MATRIX WHICH WE WANT TO PREDICT
### AND synaptic_weights WHICH U CAN FIND ABOVE
print(3 / (1 + exp(-(dot(array([3, 0, 0]), synaptic_weights)))))