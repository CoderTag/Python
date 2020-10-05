def power_station(k, arr):
    if (k < 2):
        print("step should be minimum 2")
        return -1

    step = k - 1
    ideal_jump = step * 2 + 1
    array_length = len(arr)

    if array_length == 0:
        return -1

    if array_length <= k:
        first_occurance = next((i for i, e in enumerate(arr) if e), None)
        if first_occurance != None:
            no_of_station = 1
            return no_of_station
        else:
            return -1

    highest_index = array_length - 1
    high = step
    low = -1
    station_postion = []
    extreme_right_one_pos = 0

    while(high <= highest_index):
        Found = False
        trigger_extreme_right = False
        # print(f'LOW: {low} HIGH: {high}')
        for i in range(high, low, -1):
            if arr[i] == 1:
                Found = True
                station_postion.append(i)
                trigger_extreme_right = True

                if(trigger_extreme_right) and ((i + step) < highest_index):
                    temp_step = step
                    other_low = None
                    other_high = None
                    while(temp_step):
                        if arr[i + temp_step]:
                            extreme_right_one_pos = i + temp_step
                            other_low = extreme_right_one_pos - 1
                            other_high = extreme_right_one_pos + step
                            break
                        temp_step -= 1

                break

        if not Found:
            if(extreme_right_one_pos) and (other_low != None) and (other_high != None):
                low = other_low
                high = other_high
                extreme_right_one_pos = 0
                continue
            else:
                print("here2")
                return -1

        low = i + step
        high = i + ideal_jump
        # print(station_postion)
        # print(f'OTHER_LOW: {other_low} OTHER_HIGH: {other_high}')

    print(f'Low: {low} high: {high}')
    low = low + 1
    if(low <= highest_index):
        arr2 = arr[low:]

        if len(arr2) < step + 1:
            diff = (step + 1) - len(arr2)
            low = low - diff
            arr2 = arr[low:]

        first_occurance = next((i for i, e in enumerate(arr2) if e), None)
        if first_occurance != None:
            station_postion.append(low + first_occurance)
        else:
            print("here3")
            return -1

    print(station_postion)
    return len(station_postion)


if __name__ == "__main__":
    while True:
        try:
            (length, step) = map(int, (input("Enter length & step: ").strip().split(" ")))
            break
        except ValueError:
            print("Enter length & step(exactly two int values) : ")

    while True:
        city_distribution = list(map(int, (input("Enter array of 0 & 1 (e.g 0 1 1 0):  ").strip().split(" "))))
        print(city_distribution)
        if len(city_distribution) == length:
            break
        else:
            print("length of array does not match with entered value")
    result = power_station(step, city_distribution)
    print(str(result) + "\n ")
