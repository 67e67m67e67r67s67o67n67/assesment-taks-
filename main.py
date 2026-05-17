import os
import pandas as pd

df = pd.read_csv(r"C:\Users\Emers\OneDrive\Desktop\datattaaaaaaaaaaaaaaa.csv")
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

def quitFunction():
    quitChoice = input("Are you sure you want to quit?(Y/N):").strip().upper()
    if quitChoice == 'Y':
        print("Quitting program")
        raise SystemExit
    elif quitChoice == 'N':
        return
    else:
        print("Error, please try again")
        input("Press any key to continue:")

def searchData():
    searchType = input("What would you like to search by? (Disaster/Year/Country): ").strip().lower()
    
    validSearch = {
        "disaster": "Disaster",
        "year": "Year",
        "country": "Country"
    }
    
    if searchType not in validSearch:
        print("Invalid search type.")
        input("Press Enter to continue")
        return

    searchValue = input("Enter search value: ").strip()
    columnName = validSearch[searchType]
    os.system('cls')
    
    if searchType == "year":
        try:
            searchValue = int(searchValue)
        except ValueError:
            print("Year must be a number.")
            input("Press Enter to continue:")
            return

        result = df[df[columnName] == searchValue]

    else:
        result = df[df[columnName].astype(str).str.lower().str.contains(searchValue.lower(), na=False)]

    if result.empty:
        print("No matching data found.")

    else: 
        print("\nSearch Results:\n")
        print(result)

    input("\nPress Enter to continue")   

def mainMenu():
    while True:
        os.system('cls') 
        print("""
==============================================================
                        Past weather Data
==============================================================
      
What would you like do to?      
    Option 1: Search data set
    Option 2: View instructions
    Option 3: Quit      
              
==============================================================              
""")
        choice = input("Enter choice: ")
        os.system('cls')
        if choice == '1':
            searchData()
        elif choice == '2':
            print("""
==============================================================     
                       Instructions
==============================================================  
      
Select option 1 to search the data set, you can search by country, year, or disaster type.
Year refers to the year that the event happened, Country refers to hwat country it happened in, Magnitude is the magnitude and is based on the magnitude scale that is relevant to the disaster, Deaths is the death toll, Affected shows how many people were affected, Damages shows the cost of the damaged adjusted to the current price in USD.
            
Disaster types include:      
      Air accident
      Animal attack
      Ash fall
      Avalanche
      Bacterial disease
      Bush fire
      Chemical spill
      Cold wave
      Collapse
      Convective storm
      Coastal flood
      Debris flow
      Drought
      Explosion
      Extra-tropical storm
      Fire of domestic structures
      Flash flood
      Fog
      Forest fire
      Geomagnetic storm
      Glacial lake outburst
      Grasshopper infestation
      Ground movement
      Heatwave
      Lahar
      Land fire
      Landslide
      Locust
      Meteorite impact
      Parasitic disease
      Pyroclastic flow
      Radiation
      Rail accident
      Riverine flood
      Road accident
      Rockfall
      Rogue wave
      Severe winter conditions
      Tidal wave
      Tropical cyclone
      Tsunami
      Viral disease
      Water accident
      
==============================================================      
""")
            input("Press any key to continue:")

        elif choice == '3':
           quitFunction()
        else:
            print("Error, please try again")
            input("Press any key to continue:")

mainMenu()