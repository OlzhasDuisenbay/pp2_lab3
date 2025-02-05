"""Read in a Fahrenheit temperature. Calculate and
display the equivalent centigrade temperature.
The following formula is used for the conversion: C = (5 / 9) * (F – 32)"""
def farenheit_to_celcius(f):
    return 5*(f-32)/9
farenheit = int(input())
celcius = farenheit_to_celcius(farenheit)
print(celcius)
#45 >>> 7.222222222222222
