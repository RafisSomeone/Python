from Camera_Operator import Camera_operator
from Operation import *
from Browser_operator import *


def main():
    camera_operator = Camera_operator()
    camera_operator.start()

    browser_operator = Browser_operator()

main()