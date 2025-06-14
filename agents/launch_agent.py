import requests

class LaunchInfoAgent:
    def get_launch_details(self):
        print("[LaunchInfoAgent] Fetching next SpaceX launch details...")
        url = "https://api.spacexdata.com/v5/launches/upcoming"
        res = requests.get(url)
        data = res.json()
        next_launch = sorted(data, key=lambda x: x['date_utc'])[0]

        name = next_launch['name']
        date = next_launch['date_utc']
        location = next_launch['launchpad']

        # Get launchpad details
        launchpad_url = f"https://api.spacexdata.com/v4/launchpads/{location}"
        pad_res = requests.get(launchpad_url)
        pad_data = pad_res.json()
        lat = pad_data['latitude']
        lon = pad_data['longitude']
        site_name = pad_data['name']

        result = {
            "name": name,
            "date": date,
            "lat": lat,
            "lon": lon,
            "site": site_name
        }
        print(f"  -> Launch: {name} at {site_name} on {date}")
        return result
