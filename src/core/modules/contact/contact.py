from typing import TYPE_CHECKING
from ...base_module import BaseModule
from .address import AddressSniffer
from.email import EmailSniffer
from.phone import PhoneSniffer

if TYPE_CHECKING:
    from ...tweaker import Tweaker


class ContactSniffer(BaseModule):
    
    def __init__(self, tweaker: "Tweaker"):
        super().__init__(tweaker=tweaker)
        self.address = AddressSniffer(self.tweaker)
        self.email = EmailSniffer(self.tweaker)
        self.phone = PhoneSniffer(self.tweaker)