import math

def hem_cubic_map(A, x0, num_steps, num_bits):
    data = [x0] 
    for i in range(1, num_steps + 2):
        data.append(A * data[i - 1] * (1 - data[i - 1] * data[i - 1]))
    data.pop(0)  # removing x0
    data.pop(0)  # removing x1

    binary_data_array = []
    for i in range(num_steps):
        float_data = '{:.16f}'.format(data[i]).split('.')[1]  # Extract decimal part and remove leading zeros
        binary_data = str(bin(int(float_data)))[-num_bits:]  # Store the lower num_bits in array
        binary_data_array.append(binary_data)
    return binary_data_array


def rickers_population_map(A, x0, num_steps, num_bits):
    data = [x0]
    for i in range(1, num_steps + 2):
        data.append(A * data[i - 1] * (math.e ** -data[i - 1]))
    data.pop(0)  # removing x0
    data.pop(0)  # removing x1

    binary_data_array = []
    for i in range(num_steps):
        float_data = '{:.16f}'.format(data[i]).split('.')[1]  # Extract decimal part and remove leading zeros
        binary_data = str(bin(int(float_data)))[-num_bits:]  # Store the lower num_bits in array
        binary_data_array.append(binary_data)
    return binary_data_array

# ATMOST 56 BITS IF 16 DECIMAL POINTS
# len(str(bin(int("9"*38))))) - 129 bits