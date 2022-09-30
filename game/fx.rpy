init:
    transform loguito2:
        alpha 0.0
        linear 3.0 alpha 1.0
        block:
            linear 0.010 xoffset -20
            linear 0.010 xoffset 1
            linear 0.090 xoffset +0
            linear 0.010 xoffset +20
            linear 0.010 xoffset -1
            linear 0.01 xoffset +0
            pause 2
            repeat

################################################################
#RAIN
################################################################
init:

    image rain:

        "fx/rain1.png"
        0.2
        "fx/rain3.png"
        0.2
        "fx/rain2.png"
        0.2
        repeat
init:

    image rainmain:

        "fx/rainmain1.png"
        0.2
        "fx/rainmain3.png"
        0.2
        "fx/rainmain2.png"
        0.2
        repeat