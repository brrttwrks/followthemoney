from normality import stringify
from schwifty import IBAN

from followthemoney.types.common import PropertyType


class IbanType(PropertyType):

    def validate(self, iban, **kwargs):
        iban = stringify(iban)
        if iban is None:
            return False
        try:
            IBAN(iban)
            return True
        except ValueError as ex:
            print(ex)
            return False

    def clean_text(self, text, **kwargs):
        """Create a more clean, but still user-facing version of an
        instance of the type."""
        return text.replace(" ", "").upper()