def canConvert(str1, str2):
    visited = {}
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            if str1[i] in visited and visited[str1[i]] != str2[i]:
                return False
            elif str1[i] not in visited:
                visited[str1[i]] = str2[i]
    if len(set(str2)) == 26 and len(visited) != 0:
        return False
    return True

str1 = "fghijkabcdelmnopqrstuvwxyzsda"
str2 = "abcdefaghijklamnopqrastuvwxyz"
print(canConvert(str1, str2))