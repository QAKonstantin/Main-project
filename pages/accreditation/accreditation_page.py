from pages.accreditation.locators.accreditation_base import Accreditation_set
from pages.accreditation.locators.accreditation_ul import Accreditation_ul
from pages.base_locators import Locators
from pages.accreditation.locators.accreditation_fiz import Accreditation_fiz


class Accreditation(Accreditation_fiz, Accreditation_ul, Accreditation_set, Locators):
    pass
