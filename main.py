def main():
    the_array = [15, 22, 84, 14, 88, 23]
    min_val = the_array[0]
    max_val = the_array[0]

    for i in range(len(the_array)):
        current_value = the_array[i]
        if current_value < min_val:
            min_val = current_value
        elif current_value > max_val:
            max_val = current_value

    print("the_highest_value = {0}".format(max_val))
    print("the_smallest_number = {0}".format(min_val))
    print("the_difference = {0}".format(max_val - min_val))

if __name__ == "__main__":
    main()