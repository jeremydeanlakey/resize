MDPI =  "outputs/drawable-mdpi/{}.png"
HDPI =  "outputs/drawable-hdpi/{}.png"
XHDPI =  "outputs/drawable-xhdpi/{}.png"
XXHDPI =  "outputs/drawable-xxhdpi/{}.png"
XXXHDPI =  "outputs/drawable-xxxhdpi/{}.png"

def calc_android_sizes(dp):
    return [((int(dp*1.2), int(dp*1.2)), MDPI),
            ((int(dp*1.8), int(dp*1.8)), HDPI),
            ((int(dp*2.4), int(dp*2.4)), XHDPI),
            ((int(dp*3.6), int(dp*3.6)), XXHDPI),
            ((int(dp*4.8), int(dp*4.8)), XXXHDPI)]

ANDROID_20DP = calc_android_sizes(20)
ANDROID_40DP = calc_android_sizes(40)
ANDROID_LAUNCHER = ANDROID_40DP + [((512, 512), "outputs/google_play_store/{}.{}")]

IOS = {
    "Icon.png":             (57, 57,),
    "Icon@2x.png":          (114, 114,),
    "Icon-60@2x.png":       (120, 120,),
    "Icon-60@3x.png":       (180, 180,),
    "Icon-72.png":          (72, 72,),
    "Icon-72@2x.png":       (144, 144,),
    "Icon-76.png":          (76, 76,),
    "Icon-76@2x.png":       (152, 152,),
    "Icon-Small.png":       (29, 29,),
    "Icon-Small@2x.png":    (58, 58,),
    "Icon-Small@3x.png":    (87, 87,),
    "Icon-Small-40.png":    (40, 40,),
    "Icon-Small-40@2x.png": (80, 80,),
    "Icon-Small-40@3x.png": (120, 120,),
    "Icon-Small-50.png":    (50, 50,),
    "Icon-Small-50@2x.png": (100, 100,),
    "Icon-60.png":          (60, 60,),
    "Icon-60@2x.png":       (120, 120,),
    "Icon-60@3x.png":       (180, 180,),
    "Icon-76.png":          (76, 76,),
    "Icon-76@2x.png":       (152, 152,),
    "Icon-86.5@x.png":      (175, 175,),
    "iTunesArtwork.png":    (512, 512,),
    "iTunesArtwork@2x.png": (1024, 1024,),
}

IOS_NAMES = ['outputs/{}'.format(fname) for fname in IOS.keys()]
IOS_ICONS = zip(IOS.values(), IOS_NAMES)

