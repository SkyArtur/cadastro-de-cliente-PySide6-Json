from .filer import Filer
from managers.objects import Client


class FilerAccount(Client, Filer):
    def __init__(self):
        super().__init__()

