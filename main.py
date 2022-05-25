def main():
    year = 12
    valueKilometer = int(input('Please enter total kilometer: '))
    priceOil = float(input('Please enter price- Oil: '))
    pricePetrol = 53.80 #float(input('Please enter price- Petrol: '))
    priceInsurance = float(input('Please enter price- Insurance: '))
    priceTires = float(input('Please enter price- Tires: '))
    priceMaintenance = float(input('Please enter prise- Maintenance: '))

    totalPetrol = getTotalPetrol(valueKilometer)
    totalYearPricePetrol = getYearPricePetrol(pricePetrol, totalPetrol)
    totalMonthPriceInsurance = getMonthPrice(priceInsurance, year)
    totalMonthPricePetrol = getMonthPrice(totalYearPricePetrol, year)
    totalMonthPriceOil = getMonthPrice(priceOil, year)
    totalMonthPriceTires = getMonthPrice(priceTires, year)
    totalMonthMaintenance = getMonthPrice(priceMaintenance, year)
    totalMonth = getTotal(totalMonthPricePetrol, totalMonthPriceOil, totalMonthPriceInsurance, totalMonthPriceTires,
                          totalMonthMaintenance)
    totalYear = getTotal(priceOil, priceInsurance, priceTires, priceMaintenance, totalYearPricePetrol)

    print('')
    print('Total car expenses!')
    print('\t', '\t', '\t', 'Month ', '\t''\t', 'Year')
    print('Petrol: ''\t', format(totalMonthPricePetrol, ',.1f'), '\t''\t', format(totalYearPricePetrol, ',.1f'))
    print('Oil: ''\t''\t', format(totalMonthPriceOil, ',.1f'), '\t''\t''\t', format(priceOil, ',.1f'))
    print('Insurance: ''\t', format(totalMonthPriceInsurance, ',.1f'), '\t''\t''\t', format(priceInsurance, ',.1f'))
    print('Tires:''\t''\t', format(totalMonthPriceTires, ',.1f'), '\t''\t''\t', format(priceTires, ',.1f'))
    print('Maintenance:', format(totalMonthMaintenance, ',.1f'), '\t''\t''\t', format(priceMaintenance, ',.1f'))
    print('Total month''\t',format(totalMonth, ',.1f'), '\t''\t', format(totalYear, ',.1f'))
    return


def getMonthPrice(priceOil, year):
    return priceOil / year


def getYearPricePetrol(pricePetrol, totalPetrol):
    return pricePetrol * totalPetrol



def getTotalPetrol(valueKilometer):
    value = valueKilometer / 100 * 9
    return value

def getTotal(totalMonthMaintenance,totalMonthPriceTires,totalMonthPriceInsurance,totalMonthPriceOil,totalMothPricePetrol):
    return totalMonthMaintenance + totalMonthPriceTires + totalMothPricePetrol + totalMonthPriceInsurance + totalMonthPriceOil

print(main())