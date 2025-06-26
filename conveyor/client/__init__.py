"""
The client Library is a component of the driver runtime that contains funtions that interact with the Conveyor CI API Server. 
these are normal HTTP Requests to the API Server. It also has the ability to fetch Conveyor CI API Server metadata like the 
API Host and Port.

    See: https://conveyor.open.ug/blog/contributing-to-the-conveyor-ci-driver-runtime#client-library
"""

import requests
from requests.exceptions import RequestException

class Client:
    """
    The client Library is a component of the driver runtime that contains funtions that interact with the Conveyor CI API Server. these are normal HTTP Requests to the API Server. It also has the ability to fetch Conveyor CI API Server metadata like the API Host and Port.

    See: https://conveyor.open.ug/blog/contributing-to-the-conveyor-ci-driver-runtime#client-library
    """
    api_host: str
    api_port: int

    def __init__(self, api_host: str = "localhost", api_port: int = 8080):
        self.api_host = api_host
        self.api_port = api_port

    def get_api_url(self) -> str:
        """
        Returns the full API URL for the Conveyor CI API Server.
        """
        return f"http://{self.api_host}:{self.api_port}"
    

    def create_resource(self, resource: dict) -> requests.Response:
        """
        Creates a resource on the Conveyor CI API Server.
        
        :param resource: The resource,defines the automation pipeline (what to run, when, and how)
        :return: The response from the Conveyor API Server.
        """
    
        url = f"{self.get_api_url()}/resources/"
        try:
            response = requests.post(url, json=resource)
            response.raise_for_status()
            return response
        except RequestException as e:
            print(f"Request failed: {e}")  
            raise

        