data_chunks = range(1, 100, 4)


def get_partial_df(num):
    return num


#complete_df = None
complete_df = list()
print(type(complete_df))
for data_chunk in data_chunks:
    partial_df = get_partial_df(data_chunk)
    complete_df.append(partial_df)

    # if complete_df is None:
    #     complete_df = partial_df
    # else:
    #    complete_df = complete_df.append(partial_df)
print(complete_df)
