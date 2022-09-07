from GUI import execute_app
from filer import Filer
from managers import ManagerOperations
client = {
        "id": 1,
        "num": "001-1",
        "opening": "07/09/2022",
        "holder": "artur dos santos shon",
        "balance": 2000.0,
        "credits": 1000.0,
        "available": 3000.0
    }

if __name__ == "__main__":
    Filer()
    execute_app()
    # manager = ManagerOperations()
    # manager.data_client = client
    # print(manager.get_statement())


