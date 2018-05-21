#!/bin/bash

# Conversor de Markdown a HTML.

# Read markdown file
text=$(<README.md)
text=${text//\"/\\\"}
text=${text//	/\\\t}
text=${text//
/\\\n}

# Convert markdown to html using Github API v3
result=$(curl --silent https://api.github.com/markdown -d "{\"text\": \"$text\", \"mode\": \"gfm\", \"context\": \"\"}")

# Cambiar la dirección para la imagen (el diagrama de funcionamiento).
result=${result//Im%C3%A1genes\/diagrama.jpg/..\/static\/images\/diagram.jpg}

# Output html
printf '<!DOCTYPE HTML>
<html lang="en-US">
<head>
<meta charset="UTF-8">
<title>Documentacion</title>
' >> documentacion.html

# Añadir hoja de estilos.
printf "<link rel=\"stylesheet\" type=\"text/css\" href=\"../static/css/style_documentation.css\">" >> documentacion.html

# Escribir el html que está guardado en 'result'.
printf "\n </head>
<body>
  <p class=\"title1\">Smart_Hours.</p>
  <br>
  <div id=\"wrapper\">%s</div>
</body>
</html>" "$result" >> documentacion.html

# Mover el archivo al servidor (a la carpeta templates).
mv documentacion.html Servidor/app/templates/
