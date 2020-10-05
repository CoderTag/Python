from collections import defaultdict


def maximumPeople(ppl_in_town, loc_of_town, loc_of_cloud, range_of_cloud):

    ppl_in_sunny_city = []
    city_under_common_cloud = defaultdict(int)

    for city_index, city_loc in enumerate(loc_of_town):
        FOUND = 0
        tmp_city_index = []
        tmp_cloud_index = []

        for cloud_index, cloud_loc in enumerate(loc_of_cloud):

            lower_range = cloud_loc - range_of_cloud[cloud_index]
            upper_range = cloud_loc + range_of_cloud[cloud_index] + 1
            if city_loc in range(lower_range, upper_range):
                FOUND += 1
                if FOUND > 1:
                    break
                tmp_city_index.append(city_index)
                tmp_cloud_index.append(cloud_index)

        if FOUND == 0:
            ppl_in_sunny_city.append(ppl_in_town[city_index])
        if FOUND == 1:
            cloud_to_be_consider = str(loc_of_cloud[tmp_cloud_index[0]])
            city_under_common_cloud[cloud_to_be_consider] += ppl_in_town[tmp_city_index[0]]

    population_already_in_sunny_city = 0
    max_ppl_under_single_cloud = 0

    population_already_in_sunny_city = sum(ppl_in_sunny_city)
    if city_under_common_cloud.values():
        max_ppl_under_single_cloud = max(city_under_common_cloud.values())
    return population_already_in_sunny_city + max_ppl_under_single_cloud


if __name__ == "__main__":
    ppl_in_town = [10, 1, 8, 3]
    loc_of_town = [4, 5, 7, 2]
    loc_of_cloud = [3, 9, 3, 5]
    range_of_cloud = [11, 10, 8, 7]
    ppl = maximumPeople(ppl_in_town, loc_of_town, loc_of_cloud, range_of_cloud)
    print(ppl)
