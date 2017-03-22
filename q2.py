bands = ['Led Zeppelin', 'Pink Floyd', 'The Doors', 'Pearl Jam', 'The Beatles']

## remove by index (remember index starts from 0!)
del bands[2]

## add two more bands
bands.append('Last Second Band')
bands.append('Last Band')

## print (remember index starts from 0!)
print("Your #2 favorite band in this list is " + bands[1] + " . Your least favorite band in this list is " + bands[len(bands) - 1])