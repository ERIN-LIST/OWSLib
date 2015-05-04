# =============================================================================
# Copyright (c) 2015 Luís de Sousa
#
# Authors : 
#          Luís de Sousa <luis.a.de.sousa@gmail.com>
#
# Contact email: luis.a.de.sousa@gmail.com
# =============================================================================

##########NOTE: Does not conform to new interfaces yet #################

from wcs110 import WebCoverageService_1_1_0, ServiceProvider, ContactMetadata, ContentMetadata

def nsWCS(tag):
    return '{http://www.opengis.net/wcs/1.1.1}'+tag

def nsWCS_OWS(tag):
    return '{http://www.opengis.net/wcs/1.1.1/ows}'+tag

def nsOWS(tag):
    return '{http://www.opengis.net/ows/1.1.1}'+tag


class WebCoverageService_1_1_1(WebCoverageService_1_1_0):
    """Abstraction for OGC Web Coverage Service (WCS), version 1.1.1
    Implements IWebCoverageService.
    """
    self.version='1.1.1'
    
            
class Operation(wcs110.Operation):
    """Abstraction for operation metadata    
    Implements IOperationMetadata.
    """


class ServiceIdentification(wcs110.ServiceIdentification):
    """ Abstraction for ServiceIdentification Metadata 
    implements IServiceIdentificationMetadata"""
    self.version="1.1.1"
       
       
class ServiceProvider(wcs110.ServiceProvider):
    """ Abstraction for ServiceProvider metadata 
    implements IServiceProviderMetadata """


class ContactMetadata(wcs110.ContactMetadata):
    ''' implements IContactMetadata'''


class ContentMetadata(wcs110.ContentMetadata):
    """Abstraction for WCS ContentMetadata
    Implements IContentMetadata
    """
        
        