def main():
    year = 12
    valueKilometer = int(input('Please enter total kilometer: '))
    priceOil = float(input('Please enter price- Oil: '))
    pricePetrol = 53.80 #float(input('Please enter price- Petrol: '))
    priceInsurance = float(input('Please enter price- Insurance: '))
    # priceTires = float(input('Please enter price- Tires: '))
    # priceMaintenance = float(input('Please enter prise- Maintenance: '))
    #totalPriceOil = getMonthPriceOil(priceOil)
    totalPetrol = getTotalPetrol(valueKilometer)
    totalYearPricePetrol = getYearPricePetrol(pricePetrol, totalPetrol)
    totalMonthPriceInsurance = getMonthPrice(priceInsurance, year)
    totalMonthPricePetrol = getMonthPrice(totalYearPricePetrol, year)
    totalMonthPriceOil = getMonthPrice(priceOil, year)

    print('')
    print('Total car expenses!')
    print('\t', '\t', 'Month ', '\t', 'Year')
    print('Petrol: ', format(totalMonthPricePetrol, ',.1f'), '\t', format(totalYearPricePetrol, ',.1f'))
    print('Oil: ', '\t', format(totalMonthPriceOil, ',.1f'), '\t''\t', format(priceOil, ',.1f'))
    print('Insurance: ', '\t', format(totalMonthPriceInsurance, ',.1f'))
    return

#def getMonthPriceOil(priceOil):
    #return priceOil / 12


def getMonthPrice(priceOil, year):
    return priceOil / year


def getYearPricePetrol(pricePetrol, totalPetrol):
    return pricePetrol * totalPetrol


def getTotalPetrol(valueKilometer):
    value = valueKilometer / 100 * 9
    return value


print(main())