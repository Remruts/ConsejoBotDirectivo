# Consejo Bot Directivo
En este repo se encuentra la gramática de [Tracery](http://tracery.io) usada en el bot https://twitter.com/cd_exactas_bot por [@remruts](https://twitter.com/remruts)

El bot original fue hecho con http://cheapbotsdonequick.com y hosteado en la misma página de manera gratuita. La gramática definida en `bot_CD.json` que usa svgs para las imágenes.

El repo trae una implementación de ejemplo en python 3 que genera imágenes en svg a partir de la gramática. Para usarlo, instalar [pytracery](https://github.com/aparrish/pytracery) y ejecutar

    python3 generador.py > mi_resolucion.svg

### Ejemplo de resolución generada con este script:

![ejemplo](ejemplo.svg "sí, puede generar muchas cosas horribles, ja")

## Tutoriales y recursos que usé para esto:
- Cheap Bots Done Quick es una página que hostea gratis bots de Twitter que usan gramáticas de Tracery: http://cheapbotsdonequick.com
- Tutorial de Tracery por su creadora: http://www.crystalcodepalace.com/traceryTut.html
- Tutorial de svg con Tracery: https://github.com/derekahmedzai/cheapbotsdonequick/blob/master/svg-tracery-image-bots.md
- Una respuesta de stackoverflow que perdí que decía que para hacer saltos de línea en svgs tenés que poner el texto entre `<tspan x=\"50\" dy=\"1.2em\">` y `</tspan>`
- Los emojis los saqué de este repo: https://github.com/dariusk/corpora, que tiene corpora lindas de distintos datos, como una lista de emojis, animales, plantas, series de TV, personas, objetos varios, etc.


