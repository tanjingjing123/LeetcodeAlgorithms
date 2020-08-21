def validIPAddress(IP):
    if "." in IP:
        IP = IP.split('.')
        if len(IP) != 4:
            return "Neither"

        for i in range(len(IP)):
            if IP[i].isnumeric() == False:
                return "Neither"

            if int(IP[i]) >= 256 or int(IP[i]) <= -1:
                return "Neither"

            if len(IP[i]) > 1:
                if IP[i][0] == '0':
                    return "Neither"
        return "IPv4"

    elif ":" in IP:
        IP = IP.split(':')
        if len(IP) != 8:
            return "Neither"

        alpha = ["a", "b", "c", "d", "e", "f", "A", "B", "C", "D", "E", "F"]
        for i in range(len(IP)):
            temp = len(IP[i])
            if temp >= 5 or temp <= 0:
                return "Neither"
            for char in IP[i]:
                if char.isnumeric() == False:
                    if char not in alpha:
                        return "Neither"
        return "IPv6"

    else:
        return "Neither"

IP = "2001:0db8:85a3:0:0:8A2E:0370:7334"
print(validIPAddress(IP))