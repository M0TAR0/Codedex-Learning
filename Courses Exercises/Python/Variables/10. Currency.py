#Conversion rates
COLOMBIANPESOS_CONVERSION_USD = 0.00027 #USD
PERUVIANSOLES_CONVERSION_USD = 0.30 #USD
BRAZILIANREAIS_CONVERSION_USD = 0.19 #USD

#User input "How many left?"
PesosLeft = int(input("How many pesos left? "))
SolesLeft = int(input("How many soles left? "))
ReaisLeft = int(input("How many reais left? "))

#Conversions
TotalUSD = (PesosLeft*COLOMBIANPESOS_CONVERSION_USD) + (SolesLeft * PERUVIANSOLES_CONVERSION_USD) + (ReaisLeft * BRAZILIANREAIS_CONVERSION_USD)

#User output
print(TotalUSD)
