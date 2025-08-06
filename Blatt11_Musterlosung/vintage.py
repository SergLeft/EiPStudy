def merge(source : dict, dest : dict):
    for k,v in source.items():
        dest[k] = v
    return dest

def deep_merge(source : dict, dest : dict):
    for k,v in source.items():
        if k in dest and isinstance(v, dict) and isinstance(dest[k], dict):
            dest[k] = deep_merge(v, dest[k])
        else:
            dest[k] = v
    return dest


destination = {'Bett': 'groß',
      'Teppich': 'kurz',
      'Schrank': {
          'Shirt': 'blau',
          'Werkzeug': {
             'Schraubenzieher': 'Kreuz',
             'Nippelspanner': '3,23 mm'
          },
          'Hose': 'gelb'
      }
    }
source = {'Bett': 'groß',
      'Teppich': 'flauschig',
      'Fahrrad': 'Tandem',
      'Schrank': {
          'Hose': 'grün',
          'Werkzeug': {
            'Schraubenzieher': 'Torx',
            'Hammer': 'klein'
          }
      }
    }


print(merge(source.copy(), destination.copy()))


print(deep_merge(source, destination))
