# Permite comentar una sola linea....

"""
     Comentarios con saltos de linea......
     poseee varios saltos de linea... 
     pero no hay lio en "skdfksf"comillas dobles  dentro de los comenatruis
"""

"""
     -----------
"""

#Docstring

def palindromo(sentence:str)->bool:
    """Palindromo e suna función que revisa si una cadena es o no un 
    palindromo.
    
    Args:
        sentence:string

    Returns:
        bool

    Es importante recordar que el comentario se almacena en el atributo __doc__
    
    Examples:
    >>> palindromo("Anita lava la tina")
    True
    """
    sentence=sentence.lower().replace(" ","")
    return sentence == sentence[::-1]
