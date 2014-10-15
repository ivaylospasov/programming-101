#!/usr/bin/env python3


def what_is_my_sign(date, month):
    check_date = (date, month)
    zodiac = {}
    zodiac_signs = ['Aries', 'Taurus', 'Gemini', 'Cancer'
                    'Leo', 'Virgo', 'Libra', 'Scorpio',
                    'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces']
    periods = [
              [(x, 3) for x in range(21, 32)] + [(y, 4) for y in range(1, 21)],
              [(x, 4) for x in range(21, 31)] + [(y, 5) for y in range(1, 22)],
              [(x, 5) for x in range(22, 32)] + [(y, 6) for y in range(1, 22)],
              [(x, 6) for x in range(22, 31)] + [(y, 7) for y in range(1, 23)],
              [(x, 7) for x in range(23, 32)] + [(y, 8) for y in range(1, 23)],
              [(x, 8) for x in range(23, 32)] + [(y, 9) for y in range(1, 24)],
              [(x, 9) for x in range(24, 31)] + [(y, 10) for y in range(1, 24)],
              [(x, 10) for x in range(24, 32)] + [(y, 11) for y in range(1, 23)],
              [(x, 11) for x in range(23, 31)] + [(y, 12) for y in range(1, 22)],
              [(x, 12) for x in range(22, 32)] + [(y, 1) for y in range(1, 21)],
              [(x, 1) for x in range(21, 32)] + [(y, 2) for y in range(1, 20)],
              [(x, 2) for x in range(20, 30)] + [(y, 3) for y in range(1, 21)]]
    for sign in range(len(zodiac_signs)):
        for date in range(len(periods[sign])):
            zodiac[periods[sign][date]] = zodiac_signs[sign]
    return zodiac[check_date]


def main():
    print(what_is_my_sign(23, 10))

if __name__ == '__main__':
    main()
