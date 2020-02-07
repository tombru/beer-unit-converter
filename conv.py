import logging

logger = logging.getLogger(__name__)


def l_to_ebc(l):
    return round((2.65 * float(l)) - 1.2)


def srm_to_ebc(srm):
    return round(float(srm) * 1.97)