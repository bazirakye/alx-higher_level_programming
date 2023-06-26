def safe_print_list(my_list=[], x=0):
    try:
        count = 0
        for item in my_list:
            print(item, end='')
            count += 1
            if count == x:
                break  # Stop the loop when the desired number of elements is printed
        print()  # Print a new line
        return count  # Return the number of elements printed
    except IndexError:
        return 0  # Return 0 if an exception occurs
