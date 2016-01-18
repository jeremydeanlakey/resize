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


# source: http://makeappicon.com/ios7icon
IOS_ICON_SMALL = ((29, 29), "Icon-Small")
IOS_ICON_SMALL_2x = ((58, 58), "Icon-Small@2x")
IOS_ICON_40 = ((40, 40), "Icon-40")
IOS_ICON_40_2x = ((80, 80), "Icon-40@2x")
IOS_ICON_60_2x = ((120, 120), "Icon-60@2x")
IOS_ICON_76 = ((76, 76), "Icon-76")
IOS_ICON_76_2x = ((152, 152), "Icon-76@2x")
IOS_ITUNES = ((512, 512), "iTunesArtwork")
IOS_ITUNES_2x = ((1024, 1024), "iTunesArtwork@2x")

