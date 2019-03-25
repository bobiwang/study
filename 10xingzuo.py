zodiac_name = (u'摩羯座', u'水瓶座', u'双鱼座', '白羊座')
zodiac_days = ((1, 20), (2, 19), (3, 21), (4, 21))
(mouth, day) = (, 1)
zodiac_day = filter(lambda x: x <= (mouth, day), zodiac_days)
print(zodiac_day)

zodac_len = len(list(zodiac_day)) % 4
print(zodiac_name[zodac_len])
