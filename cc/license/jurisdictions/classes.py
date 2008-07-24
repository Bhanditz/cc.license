import zope.interface
import RDF

import cc.license
from cc.license.lib.exceptions import NoValuesFoundError, CCLicenseError
from cc.license.lib import interfaces, rdf_helper

class Jurisdiction(object):
    zope.interface.implements(interfaces.IJurisdiction)

    def __init__(self, uri):
        """Creates an object representing a jurisdiction, given
           a valid jurisdiction URI. For a complete list, see
           cc.license.jurisdictions.list_uris()"""
        if not uri.startswith('http://creativecommons.org/international/') \
           or not uri.endswith('/'):
            raise CCLicenseError, "Malformed jurisdiction URI: <%s>" % uri
        self.code = cc.license.jurisdictions.uri2code(uri)
        self.id = uri
        self._titles = rdf_helper.get_titles(rdf_helper.JURI_MODEL, self.id)
        id_uri = RDF.Uri(self.id)
        try:
            self.local_url = rdf_helper.query_to_single_value(
                rdf_helper.JURI_MODEL, id_uri,
                RDF.Uri(rdf_helper.NS_CC + 'jurisdictionSite'), None)
        except NoValuesFoundError:
            self.local_url = None
        try:
            self.launched = rdf_helper.query_to_single_value(
                rdf_helper.JURI_MODEL, id_uri,
                RDF.Uri(rdf_helper.NS_CC + 'launched'), None)
        except NoValuesFoundError:
            self.launched = None

    def title(self, language='en'):
        try:
            return self._titles[language]
        except KeyError, e:
            import sys
            tb = sys.exc_info()[2]
            msg = "Language %s does not exist for jurisdiction %s"
            raise CCLicenseError, msg % (language, self.code), tb
