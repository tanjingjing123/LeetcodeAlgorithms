import collections


def dataConvert(ad_clicks, all_user_ips, completed_purchase_user_ids):
    click_ip_map = {}
    click_times_map = collections.defaultdict(int)
    ip_activities_map = {}
    for clicks in ad_clicks:
        clicks = list(clicks.split(','))
        click_ip_map[clicks[2]] = clicks[0]
        click_times_map[clicks[2]] += 1
        ip_activities_map[clicks[0]] = clicks[2]
    id2ip_map = {}

    for pair in all_user_ips:
        pair = list(pair.split(','))
        id2ip_map[pair[0]] = pair[1]

    res = collections.defaultdict(list)
    for transaction in completed_purchase_user_ids:
        ip = id2ip_map[transaction]
        activity = ip_activities_map[ip]
        total_clicks = click_times_map[activity]
        if activity not in res:
            res[activity] = [1, total_clicks]
        else:
            res[activity][0] += 1
    for k in click_times_map.keys():
        if k not in res:
            res[k] = [0, click_times_map[k]]
    print("Bought Clicked Ad Text")
    for k, v in res.items():
        print(str(v[0]) + ' of ' + str(v[1]) + ' ' + str(k))







ad_clicks = [
#"IP_Address,Time,Ad_Text",
"122.121.0.1,2016-11-03 11:41:19,Buy wool coats for your pets",
"96.3.199.11,2016-10-15 20:18:31,2017 Pet Mittens",
"122.121.0.250,2016-11-01 06:13:13,The Best Hollywood Coats",
"82.1.106.8,2016-11-12 23:05:14,Buy wool coats for your pets",
"92.130.6.144,2017-01-01 03:18:55,Buy wool coats for your pets",
"92.130.6.145,2017-01-01 03:18:55,2017 Pet Mittens",
]

all_user_ips = [
#"User_ID,IP_Address",
"2339985511,122.121.0.155",
"234111110,122.121.0.1",
"3123122444,92.130.6.145",
"39471289472,2001:0db8:ac10:fe01:0000:0000:0000:0000",
"8321125440,82.1.106.8",
"99911063,92.130.6.144"
]

completed_purchase_user_ids = [ "3123122444","234111110", "8321125440", "99911063"]

dataConvert(ad_clicks, all_user_ips, completed_purchase_user_ids)