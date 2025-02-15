import requests

# API URL
TOPUP_API_URL = "https://topup.pk/api/auth/player_id_login"

# Headers (Ensure the correct headers are added)
HEADERS = {
    "Accept": "application/json, text/plain, */*",
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36"
}

# Function to get player info by UID
def get_player_info(uid):
    data = {"player_id": uid}
    
    try:
        response = requests.post(TOPUP_API_URL, headers=HEADERS, json=data)
        if response.status_code == 200:
            result = response.json()
            return result
        else:
            return {"error": f"Error {response.status_code}"}
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

# Example usage: Replace with actual UID
uid = "123456789"  # Replace with the UID you want to check
player_info = get_player_info(uid)
print(f"Player Info for UID {uid}: {player_info}")
