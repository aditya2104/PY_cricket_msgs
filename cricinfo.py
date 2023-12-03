def cricinfo_parser():
    teams = []
    import feedparser
    xml_feed = feedparser.parse("https://static.cricinfo.com/rss/livescores.xml")
    d = xml_feed.entries
    # print(type(d))
    # print(len(d))

    for item in d:
        # print((item.title))
        # print((item.description))
        teams.append(item.description)
    return teams
    
# a = cricinfo_parser()
# for team in a:
#     print(team)