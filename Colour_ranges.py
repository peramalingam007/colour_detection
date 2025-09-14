# color_ranges.py

color_ranges = [
    # 🔴 Red (split into 2 ranges because red is at both ends of HSV circle)
    ((0, 120, 70), (10, 255, 255), "Red"),
    ((170, 120, 70), (180, 255, 255), "Red"),

    # 🟢 Green
    ((36, 50, 70), (89, 255, 255), "Green"),

    # 🔵 Blue
    ((90, 50, 70), (128, 255, 255), "Blue"),

    # 🟡 Yellow
    ((20, 100, 100), (30, 255, 255), "Yellow"),

    # 🟠 Orange
    ((10, 100, 20), (
