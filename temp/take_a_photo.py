import sys
import getopt
import picamera
from time import sleep


def main(argv):

    filename = ""
    try:
        opts, args = getopt.getopt(argv, "f:")
    except getopt.GetoptError:
        print("ERROR!")
        sys.exit(2)
    for opt, arg in opts:
        #print("opt is:%s, arg is:%s" % (opt, arg))
        if opt == '-f':
            filename = arg
            print("fn is %s" % filename)

    camera = picamera.PiCamera()
    camera.resolution = (640, 480)
    camera.capture("../pic/%s" % filename)
    print("saved ../pic/%s" % filename)


if __name__ == "__main__":
    main(sys.argv[1:])
