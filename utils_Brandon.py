'''
ITERATION 1

My First Python Project

This module provides a simple, reusable foundation for my analytics projects. 
When we work hard to write useful code, we want it to be reusable.
A good byline could be used in every Python analytics project we do.

Process:

We don't write code from top to bottom; instead, we often write it from the outside in.
Here's what a first draft of my utils_case.py might look like:

1. I start with this docstring at the very beginning.
   I use it to clarify the purpose of my Python file and organize my thoughts.
   
2. I'll declare a global variable for my byline string and just set it to some simple text.

3. I'll declare a main() function for my module. When I run this script, I can use main() to test my byline.

4. I'll add the boilerplate conditional execution code so I only run the main() function when 
   this script is executed directly (but not when I import it into another file).

I'll test it in an online interpreter to ensure this version runs correctly before continuing.
'''

#####################################
# Declare global variables - keep byline at the end
# We will use this information in a smarter byline
######################################

# Boolean variable to indicate if the company is privately held
is_privately_held: bool = True

# Integer variable for the number of employees
number_of_employees: int = 50

# List of strings representing the technologies used
technologies_used: list = ["Python", "Pandas", "NumPy", "SQL"]

# List of floats representing the recent scores
recent_scores: list = [92.22, 99.2, 95.3, 91.2]

#####################################
# Update the byline to include additional information.
#####################################

# Multiline f-string for the byline that includes all relevant information
byline: str = f"""
--------------------------
My First Python Project
--------------------------

Is Privately Held: {is_privately_held}
Number of Employees: {number_of_employees}
Technologies Used: {', '.join(technologies_used)}
Recent Scores: {recent_scores}
"""

#####################################
# Define the get_byline() Function
#####################################

def get_byline() -> str:
    '''Return a byline for my analytics projects.'''
    return byline

#####################################
# Define a main() function for this module.
#####################################

# The main function now calls get_byline() to retrieve the byline.

def main() -> None:
    '''Print the byline to the console when this function is called.'''
    print(get_byline())

#####################################
# Conditional Execution - Only call main() when executing this module as a script.
#####################################

if __name__ == '__main__':
    main()
