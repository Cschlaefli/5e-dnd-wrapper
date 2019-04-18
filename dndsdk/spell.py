#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of mtgsdk.
# https://github.com/MagicTheGathering/mtg-sdk-python

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2016, Andrew Backes <backes.andrew@gmail.com>

from dndsdk.querybuilder import QueryBuilder
from string import ascii_uppercase, ascii_lowercase


class Spell(object):
    RESOURCE = 'spells'

    """Usual attributes :
    _id, index, name, desc, higher_level, page, range, components
    material, ritual, duration, concentration, casting_time, level
    school, classes, subclasses, url
    See online docs for details."""

    # some keys in the response_dict are of the form fooBarBaz ;
    # we want them as foo_bar_baz
    trans = str.maketrans({u:"_"+l for u,l in zip(ascii_uppercase, ascii_lowercase)})

    def __new__(cls, response_dict=dict()) :
        obj = object.__new__(__class__)
        response_dict = {k.translate(__class__.trans):v for k,v in response_dict.items()}
        obj.__dict__ = response_dict
        return obj
    def __str__(self):
        return str(self.__dict__)

    @staticmethod
    def find(id=False, name=False):
        return QueryBuilder(__class__).find(id)

    @staticmethod
    def where(**kwargs):
        return QueryBuilder(__class__).where(**kwargs)

    @staticmethod
    def all():
        return QueryBuilder(__class__).all()
