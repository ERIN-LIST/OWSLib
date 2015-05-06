# -*- coding: ISO-8859-15 -*-
# =============================================================================
# Copyright (c) 2015 Luís de Sousa
#
# Authors : 
#          Luís de Sousa <luis.a.de.sousa@gmail.com>
#
# Contact email: luis.a.de.sousa@gmail.com
# =============================================================================

##########NOTE: Does not conform to new interfaces yet #################

import wcs110
#from wcs110 import WebCoverageService_1_1_0, ServiceProvider, ContactMetadata, ContentMetadata

class Namespaces_1_1_1():
    
    def WCS(self, tag):
        return '{http://www.opengis.net/wcs/1.1.1}'+tag
    
    def WCS_OWS(self, tag):
        return '{http://www.opengis.net/wcs/1.1.1/ows}'+tag
    
    def OWS(self, tag):
        return '{http://www.opengis.net/ows/1.1}'+tag


class WebCoverageService_1_1_1(wcs110.WebCoverageService_1_1_0):
    """Abstraction for OGC Web Coverage Service (WCS), version 1.1.1
    Implements IWebCoverageService.
    """
    version='1.1.1'
    ns = Namespaces_1_1_1()
    
            
# class Operation(wcs110.Operation):
#     """Abstraction for operation metadata    
#     Implements IOperationMetadata.
#     """
#     ns = Namespaces_1_1_1()
# 
# 
# class ServiceIdentification(wcs110.ServiceIdentification):
#     """ Abstraction for ServiceIdentification Metadata 
#     implements IServiceIdentificationMetadata"""
#     version="1.1.1"
#     ns = Namespaces_1_1_1() 
#        
#        
# class ServiceProvider(wcs110.ServiceProvider):
#     """ Abstraction for ServiceProvider metadata 
#     implements IServiceProviderMetadata """
#     ns = Namespaces_1_1_1()
#     
# 
# class ContactMetadata(wcs110.ContactMetadata):
#     ''' implements IContactMetadata'''
#     ns = Namespaces_1_1_1()
#     
# 
# class ContentMetadata(wcs110.ContentMetadata):
#     """Abstraction for WCS ContentMetadata
#     Implements IContentMetadata
#     """
#     ns = Namespaces_1_1_1()
        
        