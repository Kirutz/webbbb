######  ESTAS 2 LINEAS SON IMPORTANTES PARA UTILIZAR EL FRAMEWORK " FLASK ".  ######

from flask import Flask, render_template   ### RENDER_TEMPLATE SIRVE PARA UTILIZAR HTML,CSS,ETC EN TU PAG.

app = Flask(__name__)





######  REDIRECCIONES A PAGINAS / DIFERENTES HTML, ETC.  ######

@app.route("/")
def home():
    return render_template("home.html")


######  REDIRECCIONES A PAGINAS / DIFERENTES HTML, ETC.  ######

@app.route("/about")
def about():
    return render_template("about.html")


######  AQUI INICIAMOS NUESTRO SERVIDOR WEB  ######

if __name__ == "__main__":
    #app.run()  ##### SIRVE PARA INICIAR LA WEB, SI HACES CAMBIOS TENDRAS QUE REINICIAR CADA VEZ.
    app.run(debug=True)  ##### PARA INICIAR LA WEB, PERO ESTA SE REINICIARA SOLA SABIENDO QUE ESTAMOS HACIENDO CAMBIOS HABITUALMENTE. 





######### COSAS varias #########

## CARPETA STATIC = PARA ARCHIVOS CSS, JS, ETC ( ARCHIVOS ESTATICOS ) " NOMBRE DE CARPETA PUEDE CAMBIARLO A TU GUSTO"

## CARPETA TEMPLATES = PARA ARCHIVOS HTML " NOMBRE DE LA CARPETA IGUAL PUEDES CAMBIAR A TU GUSTO"


## PAGINA PARA COLORES GRADIENTES    :   https://uigradients.com/#MistyMeadow

## PAGINA PARA EXAMPLES DE PAGINAS WEB   :   https://getbootstrap.com/

## PAGINA PARA SERVIDOR    :    https://www.heroku.com/


######### COSAS DE HTML #########

## LLAVE ESPECIAL PARA HTML, FUNCIONA PARA HACER LLAMADO CON PYTHON : {{ A }}

## PARA HACER EL LLAMADO EN HTML HACIA CSS, USAMOS : 
# <link rel="stylesheet" href="{{ url_for('static', filename='css/home.css') }}>"

## COMANDO HTML:5 Y ENTER, CREAS AUTOMATICAMENTE UNA CABECILLA DE PAGINA WEB.

## EL <TITLE> SIEMPRE DEBE CONTENER EL MISMO NOMBRE PARA TODAS LAS CATEGORIAS QUE GENERES.

## PARA CARGAR SIEMPRE, TEN UN CAMBIO MINIMO EN TU HTML ( SE RECOMIENDA REINICIAR LA PAGINA CON WINDOWS + SHIFT + R ).

## CON <a class="nav-link" href="/about">Features</a> PODEMOS REDIRECCIONAR A OTRA PESTAÑA DE NUESTO SITIO, COMO ABOUT O OTROS CREADOS.
