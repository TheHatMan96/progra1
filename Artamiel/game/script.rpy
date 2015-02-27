# You can place the script of your game in this file.
# - Puedes colocar el 'script' de tu juego en este archivo.

# Declare images below this line, using the image statement.
# - Declara imágenes bajo esta línea, usando 'image' como
#   en el ejemplo.
# eg. image eileen happy = "eileen_happy.png"

image hab3 = "cave.jpg"
image hab2 = "back2.jpg"
image hab1 = "back.jpg"
image hab4 = "bosque.jpg"

image Artamiel ="elegante.png"
image Trent ="Leon.png"
image chumil = "cthulu.png"
image razer ="Sombrero.png"
image franklin ="hojalata.png"

# Declare characters used by this game.
# - Declara los personajes usados en el juego como en el 
#   ejemplo.
define e = Character("Artamiel", color="#c8ffc8")
define b = Character("Scar", color="FFFF00")
define c = Character("??????????", color="FFFFFF")
define d = Character("Chumil", color="FFFFFF")
define f = Character(" ", color="c8ffc8")
define r = Character("Razer", color="FFFFFF")
define s = Character("Franklin", color="FFFF00")
define n = Character(" ", color="FFFF00")

# The game starts here.
# - El juego comienza aquí.

label start:
    
    scene hab1
    
    play music "ball.mp3"
    
    show Artamiel at truecenter
    e "Mi nombre es Artamiel y soy el magico mas poderosos del mundo"
    hide Artamiel
    
    show Trent 
    b "Y yo soy scar su fiel acompañante!!!!!"
    hide Trent
    
    show Artamiel
    e "Cual es nuestra aventura Scar ?"
    hide Artamiel 
        
    scene hab2
    menu:
        
        "Cuevas Oscuras":
          jump cuevas
        "Pasaje Misterioso":
          jump pasaje 
          
    label cuevas:
        
    scene hab3 
    
    show Trent
    b " Este lugar se mira raro.... "
    hide Trent
    
    show Artamiel
    e " Preciento lo mismo, que algo malo va pasar."
    hide Artamiel
    
    c "Como osan entrar a mi cueva,vandalos."
    
    show chumil at truecenter
    
    d " Mi nombre es chumil y esta es mi cueva..... y ustedes no son bienvenidos" 
    
    hide chumil
    
    show Artamiel
    e " Escuchamos que hay magia oscura en esta cueva y vinimos a detener esta abominacion "
    hide Artamiel
    
    show chumil at truecenter
    d " Magia oscura?"
    d " Yo he sido atormentado por los humanos toda mi vida por eso esta cueva es el unico hogar que tengo y no dejare que me lo quiten"
    hide chumil
    
    show Trent
    b " No lo haremos,te comprendo, yo pase por lo mismo."
    b " Pero ya no debes de ocultarte mas,el mundo ha cambeado y ahora humanos y criaturas son mas unidas que antes. "
    hide Trent
    
    show chumil at truecenter 
    d " Talvez tengas razon..."
    d " Pero esperare el momento apropeado"
    hide chumil
    
    scene hab1
    
    show Trent 
    b " Me siento aliviado pero hay muchos propositos que cumplir"
    hide Trent
    
    show Artamiel 
    e " Y muchos adventuras que descubrir"
    hide Artamiel 
     
    f "FIN"
    
    return    
        
    label pasaje:
    
    scene hab4
    
    show Trent at truecenter 
    b " Que encontraremos en este lugar Artamiel?"
    b " No se mira peligroso"
    hide Trent
    
    show Artamiel at truecenter 
    e " No es nada peligroso solo tengo cuentas pendientes con un viejo amigo"
    hide Artamiel
    
    c " Hooo... Hola te has perdidos en tus adventuras, verdad patán "
    
    show razer at truecenter 
    r " Hace mucho tiempo ha pasado desde que eramos niños Artamiel"
    hide razer
    
    show franklin at truecenter 
    s "oye quien es ese gato...."
    hide franklin
    
    show Trent at truecenter 
    b " A quien le dices gato"
    hide Trent
    
    show Artamiel at truecenter 
    e " Enonces Razer y Frenlkin listos para acompañaernos en nuestras a adventuras "
    hide Artamiel
    
    show razer at truecenter 
    r " Claro que si hermano "
    hide razer
    
    scene hab2
    
    n " En esta historia se Trata de una nueva vida entre los humanos y criaturas, con su hermano Razer, franlkin y Scar encontraran el camino a la paz y orden"
   
    f "FIN"    
    
    return
