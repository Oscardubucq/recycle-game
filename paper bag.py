import pgzrun
import random
WIDTH = 800
HEIGHT = 600
CENTRE = (WIDTH/2,HEIGHT/2)
final_level = 6
start_speed = 10
ITEMS = ["bag","battery","bottle","chips"]
game_over = False
game_complete = False
current_level = 1
items = []
animations = []

def draw ():
    global items,current_level,game_over,game_complete
    screen.clear()
    screen.blit("image",(0,0))
    if game_over :
        display_message("GAME OVER","try again")
    elif game_complete:
        display_message("YOU WON","well done")
    else :
        for item in items:
            item.draw()
            
def update():
    global items
    if len(items)==0 :
        items = make_items(current_level)
        
def make_items(number_of_extra_items):
    items_to_create = get_option_to_create(number_of_extra_items)
    
    new_items = create_items(items_to_create)
    layout_items(new_items)
    animate_items(new_items)

def get_option_to_create (number_of_extra_items):
    items_to_create = ["paper"]
    for i in range(0,number_of_extra_items):
        random_option = random.choice(ITEMS)
        items_to_create.append(random_option)
    return items_to_create
    
def create_items (items_to_create):
    new_items = []
    for option in items_to_create:
        item = Actor(option + "img")
        new_items.append(item)
    return new_items
    
def layout_items(items_to_layout):
    number_of_gaps = len(items_to_layout) + 1
    gap_size = WIDTH / number_of_gaps
    random.shuffle(items_to_layout)
    
    for index,item in enumerate(items_to_layout):
        new_x_pos = (index + 1) * gap_size
        item.x = new_x_pos

def animate_items(items_to_animate):
    global animations 
    for item in items_to_animate:
        duration = start_speed - current_level
        item.anchor = ("center","bottom")
        animation = animate(item,duration = duration,on_finished = handle_game_over,y = HEIGHT)
        animations.append(animation)
        
def handle_game_over():
    global game_over
    game_over = True
    

   
