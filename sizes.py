MDPI =  "drawable-mdpi"
HDPI =  "drawable-hdpi"
XHDPI =  "drawable-xhdpi"
XXHDPI =  "drawable-xxhdpi"
XXXHDPI =  "drawable-xxxhdpi"

def calc_android_sizes(dp):
    return [((int(dp*1.2), int(dp*1.2)), MDPI),
            ((int(dp*1.8), int(dp*1.8)), HDPI),
            ((int(dp*2.4), int(dp*2.4)), XHDPI),
            ((int(dp*3.6), int(dp*3.6)), XXHDPI),
            ((int(dp*4.8), int(dp*4.8)), XXXHDPI)]

ANDROID_20DP = calc_android_sizes(20)
ANDROID_40DP = calc_android_sizes(40)
ANDROID_LAUNCHER = ANDROID_40DP + [((512, 512), "google_play_store")]



