# -*- coding: utf-8 -*-
"""Family module for Anarchopedia wiki."""
#
# (C) Pywikibot team, 2006-2015
#
# Distributed under the terms of the MIT license.
#
from __future__ import absolute_import, unicode_literals

__version__ = '$Id: acdf1ce1983f17eb0fdff98f7d870994140b0d45 $'

from pywikibot import family


# The Anarchopedia family
class Family(family.SubdomainFamily):

    """Family class for Anarchopedia wiki."""

    name = 'anarchopedia'
    domain = 'anarchopedia.org'

    interwiki_replacements = {
        # ISO 639-2 -> ISO 639-1 mappings
        'ara': 'ar',
        'chi': 'zh',
        'dan': 'da',
        'deu': 'de',
        'dut': 'nl',
        'ell': 'el',
        'eng': 'en',
        'epo': 'eo',
        'fas': 'fa',
        'fin': 'fi',
        'fra': 'fr',
        'ger': 'de',
        'gre': 'el',
        'heb': 'he',
        'hye': 'hy',
        'ind': 'id',
        'ita': 'it',
        'jpn': 'ja',
        'kor': 'ko',
        'lav': 'lv',
        'lit': 'lt',
        'nno': 'no',
        'nob': 'no',
        'nor': 'no',
        'pol': 'pl',
        'por': 'pt',
        'rum': 'ro',
        'rus': 'ru',
        'spa': 'es',
        'srp': 'sr',
        'sqi': 'sq',
        'swe': 'sv',
        'tur': 'tr',
        'zho': 'zh',

        # ISO 639-1 -> ISO 639-1 mappings
        'bs': 'hr',

        # Non-compliant mappings
        'bos': 'hr',
        'nsh': 'hr',
    }

    def __init__(self):
        """Constructor."""
        self.languages_by_size = [
            'ar', 'en', 'de', 'nl', 'el', 'it', 'fa', 'fi', 'fr', 'he', 'es',
            'hy', 'id', 'meta', 'ja', 'ko', 'lv', 'lt', 'no', 'hr', 'pl', 'pt',
            'ro', 'ru', 'hrv', 'sq', 'sr', 'sv', 'tr', 'zh', 'eo', 'da',
        ]

        super(Family, self).__init__()

        self.nocapitalize = list(self.langs.keys())

    def force_version(self, code):
        """Return the version for this family."""
        return '1.14'

    def scriptpath(self, code):
        """Return the script path for this family."""
        return ''
