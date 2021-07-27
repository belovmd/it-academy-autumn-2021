from typing import Union


def sun_angle(time: str) -> Union[int, str]:
    angl = 0
    tim = time.split(':')
    hour = float(tim[0])
    min = float(tim[1])


    if 6 <= hour <= 18:
        angl=((hour-6)*60+min)*0.25

    else:
        angl = "I don't see the sun!"

    return angl


print(sun_angle("5:30"))