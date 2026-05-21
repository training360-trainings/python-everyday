import urllib.request
import urllib.error
import json

# def fetch_json_placeholder_data(endpoint):
#     base_url = "https://jsonplaceholder.typicode.com"
#     url = f"{base_url}/{endpoint}"

#     try:
#         response = requests.get(url)
#         response.raise_for_status()
#         return response.json()
#     except requests.exceptions.RequestException as e:
#         print(f"API error: {e}")
#         return None


def fetch_json_placeholder_data(endpoint):
    base_url = "https://jsonplaceholder.typicode.com"
    url = f"{base_url}/{endpoint}"

    try:
        with urllib.request.urlopen(url) as response:
            data = response.read().decode("utf-8")
            return json.loads(data)
    except urllib.error.HTTPError as e:
        print(f"HTTP error: {e.code} {e.reason}")
        return None
    except urllib.error.URLError as e:
        print(f"URL error: {e.reason}")
        return None
    except json.JSONDecodeError as e:
        print(f"JSON error: {e}")
        return None


if __name__ == "__main__":
    endpoint = "posts"
    data = fetch_json_placeholder_data(endpoint)

    if data:
        print(json.dumps(data, indent=4))  # Pretty print the JSON data
