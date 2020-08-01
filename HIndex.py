import bisect
def hIndex(citations):
    sorted_citations = sorted(citations, reverse=True)
    citations_len = len(sorted_citations)
    if citations_len <= 0:
        return 0
    h_idx = 0
    for order_loc in range(citations_len):
        if sorted_citations[order_loc] >= order_loc + 1:
            h_idx += 1
    return h_idx

citations = [3,0,6,1,5]
print(hIndex(citations))
