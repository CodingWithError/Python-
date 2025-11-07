import sys
import os
import geocoder
import requests
from dotenv import load_dotenv
import urllib.parse

class FindGeolocation:
  def __init__(self):
    load_dotenv()
    self.__API_KEY = os.getenv("API_KEY")
    self.base_url = "https://ipgeolocation.abstractapi.com/v1/"

  def get_geolocation_data(self, ip, fields):
    if not ip or not fields:
      return "Please provide valid IP address and fields."

    encoded_fields = urllib.parse.quote(",".join(fields))
    try:
      response = requests.get(
        f"{self.base_url}?api_key={self.__API_KEY}&ip_address={ip}&fields={encoded_fields}",
        timeout=10
      )
      if response.status_code == 200:
        return response.json()
      else:
        return f"Error: Unable to fetch data (status code {response.status_code})."
    except requests.RequestException as e:
      return f"Request error: {e}"

  def get_your_ip_address(self):
    g = geocoder.ip('me')
    return g.ip

  def info_information(self, details):
    if not details:
      return "No data found."
    print("1. Basic Information\n2. Security Information\n3. Name Information\n4. Current Time Information\n5. Connection Data Information\n6. Exit")
    if details == "1":
      info_list = [
        "ip_address", "city", "city_geoname_id", "region", "region_iso_code",
        "region_geoname_id", "postal_code", "country", "country_code",
        "country_geoname_id", "country_is_eu", "continent", "continent_code",
        "continent_geoname_id", "longitude", "latitude"
      ]
      return info_list

    elif details == "2":
      user_input = input("Do you want complete information of security? (yes/no): ").lower().strip()
      if user_input == "yes":
        list_security = ["is_vpn"]
        return list_security
      elif user_input == "no":
        return "Then use 'security' directly."

    elif details == "3":
      user_input = input("Do you want complete information of name? (yes/no): ").lower().strip()
      if user_input == "yes":
        list_name = ["abbreviation", "gmt_offset"]
        return list_name
      elif user_input == "no":
        return "Then use 'name' directly."

    elif details == "4":
      user_input = input("Do you want complete information of current_time? (yes/no): ").lower().strip()
      if user_input == "yes":
        list_current_time = [
          "is_dst", "flag", "emoji", "unicode", "png", "svg",
          "currency", "currency_name", "currency_code"
        ]
        return list_current_time
      elif user_input == "no":
        return "Then use 'current_time' directly."

    elif details == "5":
      user_input = input("Do you want complete information of connection data? (yes/no): ").lower().strip()
      if user_input == "yes":
        list_connection = [
          "autonomous_system_number", "autonomous_system_organization",
          "connection_type", "isp_name", "organization_name"
        ]
        return list_connection
      elif user_input == "no":
        return "Then use 'connection' directly."
    elif details == "6":
      return "Exiting information details."
    else:
      return "Invalid option. Please choose between 1–5."


if __name__ == "__main__":
  try:
    geo = FindGeolocation()
    while True:
      print("\n===== Geolocation Finder =====")
      print("1. Get your IP address")
      print("2. Get geolocation details for an IP")
      print("3. Get information structure (info_information)")
      print("4. Exit\n")

      choice = input("Enter your choice (1-4): ").strip()

      if choice == "1":
        try:
          ip = geo.get_your_ip_address()
          if ip:
            print(f"Your IP Address: {ip}")
          else:
            print("Could not retrieve your IP.")
        except Exception as e:
          print(f"Error while fetching your IP: {e}")
          sys.exit(1)

      elif choice == "2":
        ip = input("Enter the IP address to lookup: ").strip()
        fields = input("Enter comma-separated fields (e.g., city,country,latitude,longitude): ").split(",")
        try:
          data = geo.get_geolocation_data(ip, [f.strip() for f in fields])
          print("\nResult:\n", data)
        except Exception as e:
          print(f"Error fetching geolocation: {e}")
          sys.exit(1)

      elif choice == "3":
        details = input("Enter detail option (1-5): ").strip()
        try:
          result = geo.info_information(details)
          print("Information Result:", result)
        except Exception as e:
          print(f"Error fetching information details: {e}")
          sys.exit(1)

      elif choice == "4":
        print("Exiting program. Goodbye!")
        break

      else:
        print("Invalid choice, please select 1–4.")

  except KeyboardInterrupt:
    print("\nProgram interrupted by user.")
    sys.exit(0)

  except Exception as main_error:
    print(f"Unexpected error: {main_error}")
    sys.exit(1)
