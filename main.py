from numpy import exp, array, random, dot


### LEARNING DATA FOR NEURON
training_set_inputs = array([[0, 0, 1], [1, 1, 1], [1, 0, 1], [0, 1, 1]])
print("INPUT MATRIX")
print(training_set_inputs)
### MATRIX TRANSPOSING
### IF U WANT TO DELETE .T THEN SET (3, 4) IN synaptic_weights VARIABLE
training_set_outputs = array([[0, 1, 1, 0]]).T
print("OUTPUT RESULTS")
print(training_set_outputs)
random.seed(1)
### AFTER CHANGE 2 TO 3 THE RESULT CHANGE FORM [0.99993704] TO [0.99993706]
### IF U WANT TO MAKE SOME CHANGES TO RESULT U NEED TO CHANGE FIRST AND LAST DIGITS
### IF U CHANGE (3, 1) TO (3, 4) IT SHOW MATRIX WITH 4 DIFFIRENT DIGITS
synaptic_weights = 2 * random.random((3, 1)) - 1
print("SYNAPTIC WEIGHTS")
print(synaptic_weights)


### RESULT BECOME MORE ACCURATE IF U INCREASE THE NUMBERS OF THE ROUNDS
### WHEN I SET 1000000 THE PC GOING TO CALCULATE A BIT LONG AND THEN SHOW 0.9999994 AS A RESULT
for iteration in range(10000):
    ### EXP = EXPONENTIATION
    ### DOT = MATRIX MULTIPLICATION
    output = 1 / (1 + exp(-(dot(training_set_inputs, synaptic_weights))))
    ### REWRITE synaptic_weights BY MULTIPLICATION TRANSPARENT INPUTS AND OUTPUTS
    ### FORMULA CALLED "Weighted by mistake" AND CONTAINS SECOND PART STARTED AFTER COMMA
    ### SECOND PART OF FORMULA CALLED "Sigmode Gradient"
    synaptic_weights += dot(training_set_inputs.T, (training_set_outputs - output) * output * (1 - output))
    ### IF UNCOMMENT STRINGS BELOW U WILL SEE ALL IN-BETWEEN RESULTS. THINK TWICE
    ###print("NEW SYNAPTIC WEIGHTS")
    ###print(synaptic_weights)

print("RESULT")
### THIS IS GREAT FAKA FORMULA AND I HAVE NO IDEA HOW ITS WORK, BUT ITS WORK
### HERE WE DIVIDE 1 ON 1 PLUS EXPONENTIONAL MULTIPLICATION OF MATRIX WHICH WE WANT TO PREDICT AND synaptic_weights WHICH U CAN FIND ABOVE
print(1 / (1 + exp(-(dot(array([1, 0, 0]), synaptic_weights)))))