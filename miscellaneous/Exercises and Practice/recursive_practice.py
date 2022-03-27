
def recursive_countdown(obj: int) -> int:
    """Print a countdown for any specific value"""
    
    if obj == 1:
        return print(1)
    else:
        print(obj)
        recursive_countdown(obj - 1)
        
    """
    Notes:
    - Initially, I called print on the recursive else statement and that resulted in 
    it printing None as the function was called again and again - why is that the case?
    
    - Returning 1 would mean the function wouldn't print past 2, so I needed to call print on the last function
    but also return it to break the function at that point 
    
    """


def recursive_sum_of_sequence(seq: int) -> int:
    """Return the sum of a set of numbers"""
    if seq == 0:
        return 0
    else:
        total = seq
        total += recursive_sum_of_sequence(seq - 1)
        return total

    """
    Notes:
    
    - Worked the first time - just needed to ensure I started the total off at 0 
    so it didn't keep resetting to the sequence
        - Ended up working even in the example above where I made total = seq
        - Still don't understand how it works but I think that's because of full tracing not partial
        and Sadia said to avoid that 
    """
    
def recursive_factorial(n: int) -> int:
    """Return the factorial sequence of a given number"""
    if n == 1:
        return 1 
    else:
        total = n * recursive_factorial(n-1)
        return total


def power(n:int, exp: int) -> int:
    """Takes the variable n to the power exp"""
    if exp == 1:
        return n
    else:
        return n * power(n, exp-1)
