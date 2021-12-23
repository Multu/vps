def GenerateBBSTArray(a):
    sorted_nodes = sorted(a)
    bst_array = [None] * len(a)
    recursive_bst_generation(sorted_nodes, bst_array)
    return bst_array


def recursive_bst_generation(sorted_nodes, bst_array, bst_index=0):
    middle_index = len(sorted_nodes) // 2
    bst_array[bst_index] = sorted_nodes[middle_index]

    if middle_index > 0:
        left_nodes = sorted_nodes[:middle_index]
        right_nodes = sorted_nodes[middle_index + 1:]

        recursive_bst_generation(left_nodes, bst_array, bst_index * 2 + 1)
        recursive_bst_generation(right_nodes, bst_array, bst_index * 2 + 2)
