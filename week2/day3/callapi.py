import requests
def getFlightsSuggestions(dc):
    url = "https://itinerary.buupass.com/schedules/flights/NBO/MBA/"

# Query parameters
    params = {
        "departure_on": "2025-08-27",
        "arrival_on": "2025-08-30",
        "trip_type": "return",
        "adult_count": 1,
        "child_count": 0,
        "infant_count": 0,
        "travel_class": "economy",
        "dc":dc
    }

    # Headers
    headers = {
        "sec-ch-ua-platform": "\"macOS\"",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjbGllbnRfaWQiOiJRc3VfZGdOdTdvYXI3VlB2UnV4TGJnIiwiZXhwIjoxNzU1NTM4MDUyfQ.ctujTWbIqtf8GK-eMo-OmoubcSIHwNIF6b_GUsOqrso",
        "Referer": "https://flights.buupass.com/",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
        "Accept": "application/json, text/plain, */*",
        "sec-ch-ua": "\"Not;A=Brand\";v=\"99\", \"Google Chrome\";v=\"139\", \"Chromium\";v=\"139\"",
        "sec-ch-ua-mobile": "?0"
    }

    # Make request
    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    display = ''
    for i in range(5):
              flight = data["data"][i]
              slic = flight["slices"][0]
              segment = slic["segments"][0]
              marketing_carrier = segment["marketing_carrier"]
              display += "flight : "+ marketing_carrier["name"] + ", price: " + str(flight["total_amount"]) + " KES, Departure Time: "+ segment["departing_at"] + ", Arrival Time: "+ segment["arriving_at"]
              display += "-------------------------------------------\n"
    return display

#getFlightsSuggestions('Mombasa')