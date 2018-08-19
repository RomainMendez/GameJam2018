def SCREEN_HEIGHT():
    return 720

def BAR_HEIGHT():
    return 80

def GAME_AREA_HEIGHT():
    return SCREEN_HEIGHT() - BAR_HEIGHT()

def GAME_AREA_WIDTH():
    return SCREEN_WIDTH() - TWO()*COAST_OFFSET()

def COAST_OFFSET():
    return 91

def SCREEN_WIDTH():
    return 1280

def BASIC_ENNEMY_DETECTION_RANGE():
    return 100*100

def BASIC_ENNEMY_LOSING_RANGE():
    return 200*200


def TWO():
    return 2


def STARTING_COUNT():
    return 40

def SPAWN_RATE():
    return 120
