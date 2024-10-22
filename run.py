# -*- coding: utf-8 -*-
"""
Created on Fri Nov 1 08:22:56 2024

@author: olmel6349

Jeg har valgt å programmere på engelsk, med bruk av funksjoner, mer om det står i README.md
"""
#Du kan selv velge antall kjørte km/år ut fra din typiske bilbruk. Ev. (hvis du ikke har bil) kan du anta 10.000 km
ANNUAL_MILEAGE_IN_KM = 10000

#Forsikring: Elbil: 5000 kr/år. 
ANNUAL_INSURANCE_ELECTRIC = 5000

#Forsikring: Bensinbil: 7500 kr/år.
ANNUAL_INSURANCE_PETROL = 7500

#Trafikkforsikringsavgift: 8,38 kr/dag for både elbil og bensinbil.
TRAFFIC_INSURANCE_FEE = 8.38

#Forbruk: Bensinbil: 1,0 kr/km.
FUEL_CONSUMPTION_IN_KR = 1.0

#Forbruk: Elbil: 0,2 kWh/km
ENERGY_CONSUMPTION_ELECTRIC_KM_KWH = 0.2

#Strømpris (antar kun hjemmelading): 2.00 kr/kWh
ENERGY_PRICE_FOR_EACH_KWH = 2.0

#Bomavgift: Elbil: 0,1 kr/km. 
ROAD_TAX_ELECTRIC = 0.1

#Bomavgift: Bensinbil: 0,3 kr/km.
ROAD_TAX_PETROL = 0.3 

"""
Kalkulerer forsikring, trafikkforsikringsavgift, forbruk og bomavgift for bensinbil
Returnerer totalsum som blir brukt til å regne ut kostnadsdifferanse
"""
def calculate_annual_expence_for_petrol_car():
    print("############### Bensinbil ###################")
    
    #Forsikring
    annual_insurance = ANNUAL_INSURANCE_PETROL
    print(f"Forsikring: {annual_insurance} kr")
    
    #Trafikkforsikringsavgift
    annual_traffic_insurance_fee = calculate_traffic_insurance_fee()
    print(f"Trafikkforsikringsavgift: {annual_traffic_insurance_fee} kr")
    
    #Utregning av forbruk med avrunning ved bruk av round funksjonen
    annual_fuel_consumption = round(ANNUAL_MILEAGE_IN_KM * FUEL_CONSUMPTION_IN_KR)
    print(f"Forbruk: {annual_fuel_consumption} kr")
    
    #Utregning av bomavgift med avrunning ved bruk av round funksjonen
    road_tax = round(ROAD_TAX_PETROL * ANNUAL_MILEAGE_IN_KM)
    print(f"Bomavgift: {road_tax} kr")
    
    #Sum
    return total(annual_insurance, annual_traffic_insurance_fee, annual_fuel_consumption, road_tax)

"""
Kalkulerer forsikring, trafikkforsikringsavgift, forbruk og bomavgift for bensinbil
Returnerer totalsum som blir brukt til å regne ut kostnadsdifferanse
"""
def calculate_annual_expence_for_electric_car():
    print("############### Elbil ###################")
    
    #Forsikring
    annual_insurance = ANNUAL_INSURANCE_ELECTRIC
    print(f"Forsikring: {annual_insurance} kr")
    
    #Trafikkforsikringsavgift
    annual_traffic_insurance_fee = calculate_traffic_insurance_fee()
    print(f"Trafikkforsikringsavgift: {annual_traffic_insurance_fee} kr")
    
    #Utregning av forbruk med avrunning ved bruk av round funksjonen
    annual_fuel_consumption = round(ANNUAL_MILEAGE_IN_KM * ENERGY_CONSUMPTION_ELECTRIC_KM_KWH * ENERGY_PRICE_FOR_EACH_KWH)
    print(f"Forbruk: {annual_fuel_consumption} kr")
    
    #Utregning av bomavgift med avrunning ved bruk av round funksjonen
    road_tax = round(ROAD_TAX_ELECTRIC * ANNUAL_MILEAGE_IN_KM)
    print(f"Bomavgift: {road_tax} kr")
    
    #Sum
    return total(annual_insurance, annual_traffic_insurance_fee, annual_fuel_consumption, road_tax)

"""
Kalkulerer årlig trafikkforsikringsavgift
Returnerer årlig trafikkforsikringsavgift avrunnet som blir brukt i summeringen av totalen
"""
def calculate_traffic_insurance_fee(): 
    return round(TRAFFIC_INSURANCE_FEE * 365)

"""
Kalkulerer summen av forsikring, trafikkforsikringsavgift, forbruk og bomavgift
Returnerer totalsum
"""
def total(annual_insurance, annual_traffic_insurance_fee, annaual_fuel_consumption, road_tax):
    return annual_insurance + annual_traffic_insurance_fee + annaual_fuel_consumption + road_tax

"""
Printer ut totalkostand for hver bil og årlig kostnadsdifferanse
"""
def main():     
    #Kaller på funksjon som regner ut årlig kostnad for bensinbil
    annual_expence_for_petrol_car = calculate_annual_expence_for_petrol_car()
    print(f"Årlige kostnader bensinbil: {annual_expence_for_petrol_car} kr")
    
    #Ny linje i konsollet
    print()
    
    #Kaller på funksjon som regner ut årlig kostnad for elbil
    annual_expence_for_electric_car = calculate_annual_expence_for_electric_car()
    print(f"Årlige kostnader elbil: {annual_expence_for_electric_car} kr")
    
    #Regner ut differansen mellom bensin og elbil
    diff = annual_expence_for_petrol_car - annual_expence_for_electric_car
    
    #Ny linje i konsollet
    print()
    
    print("############### Årlig kostnadsdifferanse ###################")
    print(f"Du vil spare {diff} kr i året på å kjøre elbil")

"""
Funksjonen som kjører programmet
"""
main()