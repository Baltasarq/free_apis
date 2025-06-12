# Demo Free API (c) 2025 Baltasar MIT License <baltasarq@gmail.com>


import urllib.request as request
import urllib
import json


def get_data_from_url(url: str) -> dict:
    toret = {"request": {"url": url}, "data": None}

    try:
        with request.urlopen(url) as response:
            if response.status == 200:
                toret["data"] = json.loads(response.read().decode())
                toret["request"]["response"] = 200
            else:
                toret["request"]["response"] = response.status
            ...
        ...
    except Exception as err:
        if isinstance(err, urllib.error.URLError):
            toret["request"]["response"] = err.code
        ...
        
        toret["request"]["message"] = str(err)
    ...
    
    return toret
...


if __name__ == "__main__":
    APIS: dict[str, str] = {
        "countries": "https://restcountries.com/v3.1/name/",
        "sunrise/sunset": "https://api.sunrise-sunset.org/json"
    }

    op = 1
    while op > 0:
        print("1. Countries\n2. Sunrise/sunset\n0. exit")
        op = input("?: ")
        op = 99 if not op else int(float(op))
        
        match op:
            case 1:
                name = input("Name of the country in English: ").strip()
                name = "spain" if not name else name
                print(
                    json.dumps(
                        get_data_from_url(APIS["countries"] + name),
                        indent=4))
            case 2:
                print("From url: https://sunrise-sunset.org/")
                lat_str = input("Lat: ")
                lng_str = input("Long: ")
                lat = 40.4378373 if not lat_str else float(lat_str)
                lng = -3.8443425 if not lat_str else float(lng_str)
                print(
                    json.dumps(
                        get_data_from_url(APIS["sunrise/sunset"]
                            + f"?lat={lat}&lng={lng}&formatted=0"),
                        indent=4))
                            
            case 3:
                print("whatever")
        ...
    ...
...
