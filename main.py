let random = false
basic.forever(function () {
    if (maqueen.Ultrasonic(PingUnit.Centimeters) < 20 && maqueen.Ultrasonic(PingUnit.Centimeters) != 0) {
        random = Math.randomBoolean()
        if (random == true) {
            maqueen.motorRun(maqueen.Motors.All, maqueen.Dir.CCW, 255)
            basic.pause(1000)
            maqueen.motorRun(maqueen.Motors.M2, maqueen.Dir.CW, 255)
            maqueen.motorStop(maqueen.Motors.M1)
            basic.pause(800)
        }
        if (random == false) {
            maqueen.motorRun(maqueen.Motors.All, maqueen.Dir.CCW, 255)
            basic.pause(1000)
            maqueen.motorRun(maqueen.Motors.M1, maqueen.Dir.CW, 255)
            maqueen.motorStop(maqueen.Motors.M2)
            basic.pause(800)
        }
    } else {
        maqueen.motorRun(maqueen.Motors.All, maqueen.Dir.CW, 255)
    }
})
