def maximumPeople(ppl_in_town, loc_of_town, loc_of_cloud, range_of_cloud):

    lower_limit = loc_of_cloud[0] - range_of_cloud[0]
    upper_limit = loc_of_cloud[0] + range_of_cloud[0] + 1
    cloud_location_union = set(range(lower_limit, upper_limit))

    cloud_location_intersection = set()
    cloud_loc_len = len(loc_of_cloud)

    # import pdb
    # pdb.set_trace()
    for i in range(1, cloud_loc_len):
        lower_limit = loc_of_cloud[i] - range_of_cloud[i]
        upper_limit = loc_of_cloud[i] + range_of_cloud[i] + 1
        tmp_set = set(range(lower_limit, upper_limit))

        if cloud_location_union.intersection(tmp_set):
            cloud_location_intersection.update(cloud_location_union.intersection(tmp_set))

        cloud_location_union.update(tmp_set)

    tmp_loc_of_town = set(loc_of_town)
    town_not_under_cloud = list(tmp_loc_of_town.difference(cloud_location_union))
    population_already_in_sunny_city = 0

    for town in town_not_under_cloud:
        my_index = loc_of_town.index(town)
        population_already_in_sunny_city += ppl_in_town[my_index]

    ppl_under_single_cloud = []
    for i in range(cloud_loc_len):
        lower_limit = loc_of_cloud[i] - range_of_cloud[i]
        upper_limit = loc_of_cloud[i] + range_of_cloud[i] + 1
        tmp_set = set(range(lower_limit, upper_limit))

        tmp_set2 = tmp_set.difference(cloud_location_intersection)
        tmp_lst = list(tmp_set2.intersection(tmp_loc_of_town))

        my_index = []
        for fnd in tmp_lst:
            town_count = 0
            town_count = loc_of_town.count(fnd)
            my_index.append(loc_of_town.index(fnd))

            if town_count == 1:
                continue

            town_count -= 1
            while(town_count):
                start = my_index[-1] + 1
                new_fnd = loc_of_town[start:].index(fnd)
                my_index.append(my_index[-1] + new_fnd + 1)
                town_count -= 1

        tot = sum(ppl_in_town[j] for j in my_index)
        ppl_under_single_cloud.append(tot)

    max_ppl_under_single_cloud = 0
    if ppl_under_single_cloud:
        max_ppl_under_single_cloud = max(ppl_under_single_cloud)

    return population_already_in_sunny_city + max_ppl_under_single_cloud


if __name__ == "__main__":
    ppl_in_town = [814442966]
    loc_of_town = [450418]
    loc_of_cloud = [638572]
    range_of_cloud = [570738426]
    ppl = maximumPeople(ppl_in_town, loc_of_town, loc_of_cloud, range_of_cloud)
    print(ppl)
