def merge_sort(items):
    """ Implementation of mergesort """
    if len(items) > 1:

        mid = len(items) // 2        # Determine the midpoint and split
        left = items[0:mid]
        right = items[mid:]

        merge_sort(left)            # Sort left list in-place
        merge_sort(right)           # Sort right list in-place

        l, r = 0, 0
        for i in range(len(items)):     # Merging the left and right list

            lval = left[l] if l < len(left) else None
            rval = right[r] if r < len(right) else None

            if (lval is not None and rval is not None and lval < rval) or rval is None:
                items[i] = lval
                l += 1
            elif (lval is not None and rval is not None and lval >= rval) or lval is None:
                items[i] = rval
                r += 1
            else:
                raise Exception('Could not merge, sub arrays sizes do not match the main array')