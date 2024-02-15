import json
from jsonschema import validate


schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "nombre": {
            "type": "string",
            "minLength": 1
        },
        "fecha_nacimiento": {
            "type": "string",
            "pattern": "^\\d{2}/\\d{2}/\\d{4}$"
        }
    },
    "required": ["nombre", "fecha_nacimiento"]
}


archivo_json = '''
{
    "nombre": "Juan",
    "fecha_nacimiento":"02/08/1997"
    
    }
    '''

datos_json = json.loads(archivo_json)

validate(instance=datos_json, schema=schema)
