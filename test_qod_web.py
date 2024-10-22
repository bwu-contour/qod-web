import pytest
import requests
import platform

ENDPOINT = "http://localhost:8080"
  
@pytest.mark.repeat(10)  # Run the test 10 times
def test_get_random_quote():
    if "https" in ENDPOINT.lower():
        response = requests.get(ENDPOINT + "/random", verify=False)
    else:
        response = requests.get(ENDPOINT + "/random")
    assert response.status_code == 200
    
    print("This request is being served by server: " + platform.node())
    
    print(response.text)