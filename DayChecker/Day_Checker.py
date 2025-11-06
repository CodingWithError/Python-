import requests
from dotenv import load_dotenv
import os
import sys

class Day_Checker:
  def __init__(self):
    load_dotenv()
    self.base_url="https://holidays.abstractapi.com/v1/"
    self.__api_key=os.getenv("API_KEY")

  
  def what_day(self, country, year, month, day):
    response = requests.get(f"{self.base_url}?api_key={self.__api_key}&country={country}&year={year}&month={month}&day={day}")
    if response.status_code == 200:
      Day = response.json()
      return Day
    else:
      print("Error:", response.status_code)
      print("Notifing developer...")
      return []

  def all_country(self):
    hash_map = {
      "Afghanistan": "AF",
      "Albania": "AL",
      "Algeria": "DZ",
      "American Samoa": "AS",
      "Andorra": "AD",
      "Angola": "AO",
      "Anguilla": "AI",
      "Antigua and Barbuda": "AG",
      "Argentina": "AR",
      "Armenia": "AM",
      "Aruba": "AW",
      "Australia": "AU",
      "Austria": "AT",
      "Azerbaijan": "AZ",
      "Bahrain": "BH",
      "Bangladesh": "BD",
      "Barbados": "BB",
      "Belarus": "BY",
      "Belgium": "BE",
      "Belize": "BZ",
      "Benin": "BJ",
      "Bermuda": "BM",
      "Bhutan": "BT",
      "Bolivia": "BO",
      "Bosnia and Herzegovina": "BA",
      "Botswana": "BW",
      "Brazil": "BR",
      "British Virgin Islands": "VG",
      "Brunei": "BN",
      "Bulgaria": "BG",
      "Burkina Faso": "BF",
      "Burundi": "BI",
      "Cabo Verde": "CV",
      "Cambodia": "KH",
      "Cameroon": "CM",
      "Canada": "CA",
      "Cayman Islands": "KY",
      "Central African Republic": "CF",
      "Chad": "TD",
      "Chile": "CL",
      "China": "CN",
      "Colombia": "CO",
      "Comoros": "KM",
      "Congo": "CG",
      "Congo Democratic Republic": "CD",
      "Cook Islands": "CK",
      "Costa Rica": "CR",
      "Cote d'Ivoire": "CI",
      "Croatia": "HR",
      "Cuba": "CU",
      "Curaçao": "CW",
      "Cyprus": "CY",
      "Czechia": "CZ",
      "Denmark": "DK",
      "Djibouti": "DJ",
      "Dominica": "DM",
      "Dominican Republic": "DO",
      "East Timor": "TL",
      "Ecuador": "EC",
      "Egypt": "EG",
      "El Salvador": "SV",
      "Equatorial Guinea": "GQ",
      "Eritrea": "ER",
      "Estonia": "EE",
      "eSwatini": "SZ",
      "Ethiopia": "ET",
      "Falkland Islands": "FK",
      "Faroe Islands": "FO",
      "Fiji": "FJ",
      "Finland": "FI",
      "France": "FR",
      "French Guiana": "GF",
      "French Polynesia": "PF",
      "Gabon": "GA",
      "Gambia": "GM",
      "Georgia": "GE",
      "Germany": "DE",
      "Ghana": "GH",
      "Gibraltar": "GI",
      "Greece": "GR",
      "Greenland": "GL",
      "Grenada": "GD",
      "Guadeloupe": "GP",
      "Guam": "GU",
      "Guatemala": "GT",
      "Guernsey": "GG",
      "Guinea": "GN",
      "Guinea Bissau": "GW",
      "Guyana": "GY",
      "Haiti": "HT",
      "Honduras": "HN",
      "Hong Kong": "HK",
      "Hungary": "HU",
      "Iceland": "IS",
      "India": "IN",
      "Indonesia": "ID",
      "Iran": "IR",
      "Iraq": "IQ",
      "Ireland": "IE",
      "Isle of Man": "IM",
      "Israel": "IL",
      "Italy": "IT",
      "Jamaica": "JM",
      "Japan": "JP",
      "Jersey": "JE",
      "Jordan": "JO",
      "Kazakhstan": "KZ",
      "Kenya": "KE",
      "Kiribati": "KI",
      "Kosovo": "XK",
      "Kuwait": "KW",
      "Kyrgyzstan": "KG",
      "Laos": "LA",
      "Latvia": "LV",
      "Lebanon": "LB",
      "Lesotho": "LS",
      "Liberia": "LR",
      "Libya": "LY",
      "Liechtenstein": "LI",
      "Lithuania": "LT",
      "Luxembourg": "LU",
      "Macau": "MO",
      "Madagascar": "MG",
      "Malawi": "MW",
      "Malaysia": "MY",
      "Maldives": "MV",
      "Mali": "ML",
      "Malta": "MT",
      "Marshall Islands": "MH",
      "Martinique": "MQ",
      "Mauritania": "MR",
      "Mauritius": "MU",
      "Mayotte": "YT",
      "Mexico": "MX",
      "Micronesia": "FM",
      "Moldova": "MD",
      "Monaco": "MC",
      "Mongolia": "MN",
      "Montenegro": "ME",
      "Montserrat": "MS",
      "Morocco": "MA",
      "Mozambique": "MZ",
      "Myanmar": "MM",
      "Namibia": "NA",
      "Nauru": "NR",
      "Nepal": "NP",
      "Netherlands": "NL",
      "New Caledonia": "NC",
      "New Zealand": "NZ",
      "Nicaragua": "NI",
      "Niger": "NE",
      "Nigeria": "NG",
      "North Korea": "KP",
      "North Macedonia": "MK",
      "Northern Mariana Islands": "MP",
      "Norway": "NO",
      "Oman": "OM",
      "Pakistan": "PK",
      "Palau": "PW",
      "Panama": "PA",
      "Papua New Guinea": "PG",
      "Paraguay": "PY",
      "Peru": "PE",
      "Philippines": "PH",
      "Poland": "PL",
      "Portugal": "PT",
      "Puerto Rico": "PR",
      "Qatar": "QA",
      "Reunion": "RE",
      "Romania": "RO",
      "Russia": "RU",
      "Rwanda": "RW",
      "Saint Helena": "SH",
      "Saint Kitts and Nevis": "KN",
      "Saint Lucia": "LC",
      "Saint Martin": "MF",
      "Saint Pierre and Miquelon": "PM",
      "Saint Vincent and the Grenadines": "VC",
      "Samoa": "WS",
      "San Marino": "SM",
      "Sao Tome and Principe": "ST",
      "Saudi Arabia": "SA",
      "Senegal": "SN",
      "Serbia": "RS",
      "Seychelles": "SC",
      "Sierra Leone": "SL",
      "Singapore": "SG",
      "Sint Maarten": "SX",
      "Slovakia": "SK",
      "Slovenia": "SI",
      "Solomon Islands": "SB",
      "Somalia": "SO",
      "South Africa": "ZA",
      "South Korea": "KR",
      "South Sudan": "SS",
      "Spain": "ES",
      "Sri Lanka": "LK",
      "St. Barts": "BL",
      "Sudan": "SD",
      "Suriname": "SR",
      "Sweden": "SE",
      "Switzerland": "CH",
      "Syria": "SY",
      "Taiwan": "TW",
      "Tajikistan": "TJ",
      "Tanzania": "TZ",
      "Thailand": "TH",
      "The Bahamas": "BS",
      "Togo": "TG",
      "Tonga": "TO",
      "Trinidad and Tobago": "TT",
      "Tunisia": "TN",
      "Turkey": "TR",
      "Turkmenistan": "TM",
      "Turks and Caicos Islands": "TC",
      "Tuvalu": "TV",
      "Uganda": "UG",
      "Ukraine": "UA",
      "United Arab Emirates": "AE",
      "United Kingdom": "GB",
      "United States": "US",
      "Uruguay": "UY",
      "US Virgin Islands": "VI",
      "Uzbekistan": "UZ",
      "Vanuatu": "VU",
      "Vatican City (Holy See)": "VA",
      "Venezuela": "VE",
      "Vietnam": "VN",
      "Wallis and Futuna": "WF",
      "Yemen": "YE",
      "Zambia": "ZM",
      "Zimbabwe": "ZW"
    }
    return hash_map


  def view_Country_Codes(self):
    hash_map = self.all_country()
    for country, code in hash_map.items():
      print(f"{country}: {code}")

  def search_Country_Code(self, country_name):
    if country_name=="":
      print("Please enter a valid country name.")
      return
    hash_map=self.all_country()
    if country_name in hash_map:
      print(f"The country code for {country_name} is {hash_map[country_name]}.")
    else:
      print("There is no country or check the spelling")

if __name__ == "__main__":
  Day_check = Day_Checker()
  while True:
    print("Check what day it is today!\n")
    print("Press 1 to view the list of country codes.")
    print("Press 2 to search for a country code.")
    print("Press 3 to check whats special about today")
    print("Press 4 to exit.\n")

    choice=input("Enter your choice: ")
    if choice=="4":
      sys.exit()
    elif choice=="3":
      print("Enter the country code: ")
      country=str(input()).strip().upper()
      print()
      print("Enter the year (YYYY): ")
      year=int(input().strip())
      print()
      print("Enter the month (MM): ")
      month=int(input().strip())
      print()
      print("Enter the day (DD): ")
      day=int(input().strip())
      print()
      Day_info = Day_check.what_day(country, year, month, day)
      if Day_info==[]:
        print("There is nothing special about this day or the data is not available.\n")
      else:
        print(Day_info)
    elif choice=="1":
      Day_check.view_Country_Codes()
    elif choice=="2": 
      print("Enter the country name: ")
      country_name=str(input()).strip()
      Day_check.search_Country_Code(country_name)