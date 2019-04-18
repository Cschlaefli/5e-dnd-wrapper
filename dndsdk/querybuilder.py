#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Original version by, Andrew Backes <backes.andrew@gmail.com>
# Modified by Cade Schlaefli <cade.schlaefli@gmail.com>

from dndsdk.restclient import RestClient
from dndsdk.config import __endpoint__

from fuzzywuzzy import fuzz
from fuzzywuzzy import process

class QueryBuilder(object):
    def __init__(self, type):
        self.type = type

    def find(self, id):
        """Get a resource by its id
        Args:
            id (string): Resource id
        Returns:
            object: Instance of the resource type
        """
        url = "{}/{}/{}".format(__endpoint__, self.type.RESOURCE, id)
        response = RestClient.get(url)
        return self.type(response)

    def find(self, name):
        '''Gets a resource by it's name
        Args :
            name (string): name of the resource
            matches (int): number of spells to match if exact match isn't found
        Returns :
            object: Instance of the resource
        '''
        url = "{}/{}/{}".format(__endpoint__, self.type.RESOURCE, id)
        search_list = self.all()
        match = next((item for item in enumerate(search_list) if item[1].name.lower() == name.lower()), None)
        if match :
            return self.find(int(match[0]))
        else :
            return self.type(response_dict={"name":process.extractOne(name, [item.name for item in search_list])[0]})

    def find_many(self, url, type, resource):
        """Get a list of resources
        Args:
            url (string): URL to invoke
            type (class): Class type
            resource (string): The REST Resource
        Returns:
            list of object: List of resource instances
        """
        return [type(item) for item in RestClient.get(url)[resource]]

    def where(self, **kwargs):
        """Adds a parameter to the dictionary of query parameters
        Args:
            **kwargs: Arbitrary keyword arguments.
        Returns:
            QueryBuilder: Instance of the QueryBuilder
        """
        
        self.params.update(kwargs)

        return self

    def all(self):
        """Get all resources, automatically paging through data
        Returns:
            list of object: List of resource objects
        """

        url = "{}/{}".format(__endpoint__, self.type.RESOURCE)
        response = RestClient.get(url)["results"]
        response = [self.type(res) for res in response]
        return response

    def iter(self):
        """Gets all resources, automating paging through data
        Returns:
            iterable of object: Iterable of resource objects
        """

        url = "{}/{}".format(__endpoint__, self.type.RESOURCE)

        response = RestClient.get(url)
        return response

    __iter__ = iter

    def array(self):
        """Get all resources and return the result as an array
        Returns:
            array of str: Array of resources
        """
        url = "{}/{}".format(__endpoint__, self.type.RESOURCE)
        return RestClient.get(url, self.params)[self.type.RESOURCE]
