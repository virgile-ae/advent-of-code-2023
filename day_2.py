import re

data = open('data/day_2.txt').readlines()

def minimum_required(line: str, color: str) -> int:
    matches = re.findall(r'\d+ ' + color, line)
    nums = [int(x.split(' ')[0]) for x in matches]
    return max(nums)

def part_1(data: list[str]) -> int:
    COLOR_LIMITS = {
        'red': 12,
        'green': 13,
        'blue': 14,
    }

    total = 0
    for line in data:
        for color, limit in COLOR_LIMITS.items():
            minimum_count = minimum_required(line, color)
            if minimum_count > limit:
                break
        else:
            id = re.search(r'\d+', line)
            if id is not None:
                total += int(id.group(0))

    return total


def part_2(data: list[str]) -> int:
    total = 0
    for line in data:
        min_red = minimum_required(line, 'red')
        min_green = minimum_required(line, 'green')
        min_blue = minimum_required(line, 'blue')
        total += min_red * min_green * min_blue
    return total


if __name__ == '__main__':
    print(part_1(data))
    print(part_2(data))
