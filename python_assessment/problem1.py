class CustomException(Exception):
    """Custom Exception to handle, if the element is not found"""

    def __init__(self, msg):
        self.msg = msg


def binary_search(int_list, left_index, right_index, element):
    """
    Returns index of x in arr if present, else -1
    Attributes:
        int_list (list): list of integer values
        left_index (int): index of the first element
        right_index (int): index of the last element
        element (int): element to be searched

    Returns:
        int: index of the element if found, else -1
    """
    # Check base case
    if right_index >= left_index:

        mid = left_index + (right_index - left_index) / 2

        # If element is present at the middle itself
        if int_list[mid] == element:
            return mid

            # If element is smaller than mid, then it can only
        # be present in left subarray
        elif int_list[mid] > element:
            return binary_search(int_list, left_index, mid - 1, element)

            # Else the element can only be present in right subarray
        else:
            return binary_search(int_list, mid + 1, right_index, element)

    else:
        # Element is not present in the array
        return -1


def run():
    """Main function to take input from the user and returns the search index"""

    print("Enter the list of integers one by one.")

    # try block to handle the exception
    try:
        input_list = []

        while True:
            input_list.append(int(input()))

            # if input is not-integer, just print the list
    except:
        print("Input list is {}".format(input_list))

    print("Enter the integer to search")

    element = int(input())

    # Function call
    result = binary_search(input_list, 0, len(input_list) - 1, element)

    if result != -1:
        print("Element is present at index {}".format(result))
    else:
        raise CustomException("Element not found")


if __name__ == "__main__":
    run()
