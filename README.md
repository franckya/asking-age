# asking-age
We define a function get_verified_age() that will handle the user input and age verification.
We use a while loop to keep prompting the user until a valid age is provided.
Inside the loop, we use a try block to attempt converting the input to an integer. If it's not a valid integer, a ValueError will be raised, and we'll handle it by displaying an error message.
If the input is a valid integer, we check if it's greater than or equal to 18. If it is, we print "Age verified" and return the age.
If the age is less than 18, we inform the user that they must be 18 or older to proceed and continue the loop to ask for age input again.
