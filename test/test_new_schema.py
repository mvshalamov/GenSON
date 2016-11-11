from . import base


class TestBasicTypes(base.SchemaTestCase):

    def test_generate_real(self):
        self.add_object({"type": "object", "properties": {}})
        self.add_object({"hi": "REAL"})
        self.add_object({"hi": None})
        self.assertResult(
            {'properties': {'hi': {'anyOf': [{'type': 'number'},
                            {'pattern': '^[+-]?([0-9]*[.])?[0-9]+$',
                                  'type': 'string'},
                                 {'type': 'null'}]},
                'properties': {'properties': {}, 'type': 'object'},
                 'type': {'type': 'string'}},
              'type': 'object'})