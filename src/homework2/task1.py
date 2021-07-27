# Вводится M рублей и N копеек цена, а также количество S товара
# Посчитайте общую цену в рублях и копейках за L товаров.
from typing import Tuple


def penny_to_rubles(penny: int) -> Tuple[int, int]:
    return penny // 100, penny % 100


def calculate_cost(rubles: int, penny: int, count: int) -> Tuple[int, int]:
    if rubles < 0 or penny < 0 or count < 0:
        raise ValueError("Input only positive values")
    rubles_from_penny, penny = penny_to_rubles(penny * count)
    return rubles * count + rubles_from_penny, penny


if __name__ == '__main__':
    input_rubles = int(input("Input rubles cost: "))
    input_penny = int(input("Input penny cost: "))
    input_count = int(input("Input product count: "))
    total_rubles, total_penny = calculate_cost(input_rubles, input_penny, input_count)
    print(f"Total cost {total_rubles} rubles {total_penny} penny")
