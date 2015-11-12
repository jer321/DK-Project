__Autor__ = "Juan Fernando Otoya"

#Fuerzas en el Jugador(playes)
WALK_VEL=7
GRAVITY = 1.01
JUMP_VEL = -10
FAST_JUMP_VEL = -12.5

MAX_Y_VEL = 10
MAX_RUN_SPEED = 8
MAX_WALK_SPEED = 6

WALK_ACCEL = 0.15
RUN_ACCEL = .21
SMALL_TURNAROUND = .35

#Estados del Jugador(player)
STAND = 'standing'
WALK = 'walk'
JUMP = 'jump'
FALL = 'fall'

#Cosas Extra
LEFT = 'left'
RIGHT = 'right'
JUMPED_ON = 'jumped on'
DEATH_JUMP = 'death jump'

#Estados de los Barriles
RESTING = 'resting'
ROLLING = 'rolling'
DESTROID = 'destroid'

#Cosas que se pueden Obtener
MARTILLO = 'martillo'
COIN = 'coin'

#Estados del nivel
FROZEN = 'frozen'
NOT_FROZEN = 'not frozen'
KILL_DK = 'kill dk'
SAVE_PRINCESS = 'save princess'

#Info en el juego .. Diccionarios
COIN_TOTAL = 'coin total'
SCORE = 'score'
LIVES = 'lives'
CURRENT_TIME = 'current time'
LEVEL_STATE = 'level state'
PLAYER_DEATH = 'player death'

#Display
CAPTION = "Donkey Kong by Guaberx(Juan Fernando Otoya)"
SCREEN_SIZE = 1280,680#768,700#800,580

#Estados de todo el Juego
MAIN_MENU = 'main menu'
LOAD_SCREEN = 'load screen'
GAME_OVER = 'game over'
