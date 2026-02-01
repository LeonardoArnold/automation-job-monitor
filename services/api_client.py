import requests
import time

class APIClient:
    def __init__(self):
        self.base_url = "https://dummyjson.com/products"

    def fetch_data(self):
        start_time = time.time()
        try:
            response = requests.get(self.base_url, timeout=10)
            response.raise_for_status()
            duration = time.time() - start_time
            
            return {
                "status": "success",
                "data": response.json(),
                "duration": round(duration, 2)
            }
        except Exception as e:
            return {
                "status": "failed",
                "error": str(e),
                "duration": round(time.time() - start_time, 2)
            }