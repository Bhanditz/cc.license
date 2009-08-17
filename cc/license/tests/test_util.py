from nose.tools import assert_equal

from cc.license import util


UNSTRIPPED_TEMPLATE_OUTPUT = """ <html xmlns="http://www.w3.org/1999/xhtml" xmlns:dc="http://purl.org/dc/elements/1.1/title">
  <a rel="license" href="http://creativecommons.org/licenses/by/3.0/">
    <img alt="Creative Commons License" style="border-width:0" />
  </a>
  <br />

  
  
  
  
  <span xmlns:dc="http://purl.org/dc/elements/1.1/" property="dc:title" rel="dc:type" href="http://purl.org/dc/dcmitype/StillImage">TITLE</span>
  
  by
  <a xmlns:cc="http://creativecommons.org/ns#" property="cc:attributionName" rel="cc:attributionURL" href="ATTR_URL">ATTR_NAME</a>
  is licensed under a
  <a rel="license" href="http://creativecommons.org/licenses/by/3.0/">
    Creative Commons
    Attribution
    3.0
    Unported
    License
  </a>.

</html>
"""

EXPECTED_STRIPPED_OUTPUT = '<a rel="license" href="http://creativecommons.org/licenses/by/3.0/"><img alt="Creative Commons License" style="border-width:0" /></a><br /><span xmlns:dc="http://purl.org/dc/elements/1.1/" property="dc:title" rel="dc:type" href="http://purl.org/dc/dcmitype/StillImage">TITLE</span> by <a xmlns:cc="http://creativecommons.org/ns#" property="cc:attributionName" rel="cc:attributionURL" href="ATTR_URL">ATTR_NAME</a> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/3.0/">Creative Commons Attribution 3.0 Unported License</a>.'


def test_output_stripping():
    stripped_output = util.stripped_inner_xml(UNSTRIPPED_TEMPLATE_OUTPUT)
    assert_equal(stripped_output, EXPECTED_STRIPPED_OUTPUT)
