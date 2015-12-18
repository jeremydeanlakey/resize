

MDPI =  "drawable-mdpi"
HDPI =  "drawable-hdpi"
XHDPI =  "drawable-xhdpi"
XXHDPI =  "drawable-xxhdpi"
XXXHDPI =  "drawable-xxxhdpi"

ANDROID_20DP = [
((24, 24), "drawable-mdpi"),
((36, 36), "drawable-hdpi"),
((48, 48), "drawable-xhdpi"),
((72, 72), "drawable-xxhdpi"),
((96, 96), "drawable-xxxhdpi"),
]


ANDROID_40DP = [
((48, 48), "drawable-mdpi"),
((72, 72), "drawable-hdpi"),
((96, 96), "drawable-xhdpi"),
((144, 144), "drawable-xxhdpi"),
((192, 192), "drawable-xxxhdpi"),
]


ANDROID_LAUNCHER = ANDROID_40DP + [((512, 512), "google_play_store")]


def calc_android_sizes(dp):
    return [((int(dp*1.2), int(dp*1.2)), MDPI),
            ((int(dp*1.8), int(dp*1.8)), HDPI),
            ((int(dp*2.4), int(dp*2.4)), XHDPI),
            ((int(dp*3.6), int(dp*3.6)), XXHDPI),
            ((int(dp*4.8), int(dp*4.8)), XXXHDPI)]

