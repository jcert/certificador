# certificadorGera certificados de eventos mudando um template em SVG e recebendo dados por CSV

## uso

```python certifica.py <template svg> <commonevent info in csv format> <user data in csv format>```

use a flag `-h` para ver a descrição dos argumentos requeridos pelo programause a flag `-g` para obter um exemplo de como os arquivos csv devem ser formatados

## interpolação

para adicionar um placeholder `ABC` no template em svg adicione a string `^$ABC$&` em algum campo de texto do template. Essa string será substituída de acordo com os valores nos dois arquivos csv usados como argumentos.

veja o arquivo template.svg com um exemplo de uso. 
