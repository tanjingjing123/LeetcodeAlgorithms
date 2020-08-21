import collections
def subdomainVisits(cpdomains):
    memo = collections.defaultdict(int)

    for d in cpdomains:
        d = d.split(' ')
        num = int(d[0])
        d_str = d[1]
        memo[d_str] += num
        for i, c in enumerate(d_str):
            if c == '.':
                memo[d_str[i+1:]] += num
            else:continue
    res = []
    for k, v in memo.items():
        item = str(v) + ' ' + k
        res.append(item)
    return res

x = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
print(subdomainVisits(x))



