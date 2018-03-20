from test import cases as case


class BaseVendorTest(case.VendorAPITestCase):
    def initialize(self):
        self.router = 'vendors'
        
    def validate_object(self, resp, base_key = []):
        resp.is_not_empty(base_key + ['name'])
        resp.is_int(base_key + ['duns'])
        resp.is_int(base_key + ['duns_4'])
                
        if resp.check('is_not_in', base_key + ['duns'], ('830341645', '614155380', '605119932', '933706141')):
            resp.is_not_empty(base_key + ['cage'])
            resp.is_not_empty(base_key + ['sam_status'])
            resp.is_not_none(base_key + ['sam_exclusion'])
            resp.is_not_empty(base_key + ['sam_activation_date'])
            resp.is_not_empty(base_key + ['sam_expiration_date'])


class VendorListTest(BaseVendorTest):  
    def schema(self):
        return {
            'ordering': (
                'name', 'duns', 'cage', 
                'sam_status', 'sam_exclusion', 'sam_url',
                'sam_location__address', 
                'sam_location__city', 
                'sam_location__state', 
                'sam_location__zipcode', 
                'sam_location__congressional_district', 
                'sam_location_citystate',
                'annual_revenue', 
                'number_of_employees', 
                'number_of_contracts'
            ),
            'pagination': {
                '@no_args': {},
                '@page': {'page': 3},
                '@count': {'count': 50},
                '@mixed': {'page': 2, 'count': 50}
            },
            'search': {
                '@search1': ('name', 'matches', 'Services'),
                '*search2': ('duns', 'equal', '181423372'),
                '*search3': ('cage', 'equal', '3K773')
            },
            'fields': {
                'name': {
                    '*exact': 'Zero Waste Solutions',
                    '@iexact': 'urs federal services, inc.',
                    '@in': ('Suntiva', 'Trademasters', 'PowerTrain'),
                    '@contains': 'Research',
                    '@icontains': 'technologies',
                    '@startswith': 'M',
                    '@istartswith': 'global',
                    '@endswith': 'LLC',
                    '@iendswith': 'llc',
                    '@regex': '\d+',
                    '@iregex': 'inc\.?$'
                },
                'duns': {
                    '@lt': '193460839',
                    '@lte': '193460839', 
                    '@gt': '193460839', 
                    '@gte': '193460839',
                    '@range': '074108176,196004394',
                    '@in': ('114896066', '555498187', '790984186')
                },
                'cage': {
                    '*exact': '4WPK2',
                    '*iexact': '4WPK2',
                    '@in': ('1RUU6', '4ZSH3', '4YAG9')
                },
                'sam_status': {
                    '@exact': 'ACTIVE',
                    '@iexact': 'active',
                    '@in': "ACTIVE"
                },
                'sam_activation_date': {
                    '@date': '2018-02-09',
                    '@year': '2018',
                    '@month': '2',
                    '@day': '9',
                    '@week': '5',
                    '@week_day': '2',
                    '@quarter': '1'
                },
                'sam_expiration_date': {
                    '@date': '2019-02-09',
                    '@year': '2019',
                    '@month': '2',
                    '@day': '9',
                    '@week': '5',
                    '@week_day': '3',
                    '@quarter': '1'
                },
                'sam_exclusion': {
                    '-exact': True,
                    '@exact': False,
                },
                'sam_url': {
                    '@exact': 'http://www.act-corp.com',
                    '@iexact': 'http://WWW.ACT-CORP.COM',
                    '@in': ("http://www.sainc.com", "https://www.atlasresearch.us"),
                    '@contains': 'sys',
                    '@icontains': 'SYS',
                    '@startswith': 'http://www.',
                    '@istartswith': 'HTTP://WWW.',
                    '@endswith': '.com',
                    '@iendswith': '.COM',
                    '@regex': '\d+',
                    '@iregex': 'www\.[^\.]+\.com'
                },
                'sam_location__address': {
                    '@exact': '7000 Muirkirk Meadows Dr',
                    '@iexact': '7000 muirkirk meadows dr',
                    '@in': ("1002 Explorer Blvd", "8600 Boeing Dr"),
                    '@contains': 'Northbrook',
                    '@icontains': 'dEErfield pOnd',
                    '@startswith': '7500',
                    '@istartswith': '360a',
                    '@endswith': 'Ave',
                    '@iendswith': 'ave',
                    '@regex': 'Ste \d+$',
                    '@iregex': 'ste \d+$'
                },
                'sam_location__city': {
                    '@exact': 'Lexington',
                    '@iexact': 'vienna',
                    '@in': ("Lanham", "Frederick", "Huntsville"),
                    '@contains': 'vill',
                    '@icontains': 'of',
                    '@startswith': 'Mc',
                    '@istartswith': 'mc',
                    '@endswith': 'polis',
                    '@iendswith': 'POLIS',
                    '@regex': 'City',
                    '@iregex': 'TOWN'
                },
                'sam_location__state': {
                    '@exact': 'DC',
                    '@iexact': 'dc',
                    '@in': ("DC","CA","TX","VA")
                },
                'sam_location__zipcode': {
                    '@exact': '20190',
                    '@iexact': '20190',
                    '@in': ("20190", "93033", "22102"),
                    '@contains': '210',
                    '@icontains': '210',
                    '@startswith': '35',
                    '@istartswith': '35',
                    '@endswith': '710',
                    '@iendswith': '710',
                    '@regex': '^[13579]+',
                    '@iregex': '^[13579]+'
                },
                'sam_location__congressional_district': {
                    '@exact': '07',
                    '@iexact': '07',
                    '@in': ("07", "04", "08", "01")
                },
                'pools__pool__id': {
                    '@exact': 'BMO_SB_10',
                    '@iexact': 'hcaTs_Sb_2',
                    '@in': ("BMO_8", "OASIS_4", "HCATS_SB_1")
                },
                'pools__piid': {
                    '@exact': 'GS00Q14OADS121',
                    '@iexact': 'gs00q14Oads121',
                    '@in': ("GS00Q14OADS121", "GS00Q14OADS608"),
                    '@contains': 'OAD',
                    '@icontains': 'Oad',
                    '@startswith': 'GS02',
                    '@istartswith': 'gs02',
                    '@endswith': '102',
                    '@iendswith': 's102',
                    '@regex': '^GS\d+',
                    '@iregex': '^(gs06|gs00)'
                },
                'pools__pool__name': {
                    '@exact': 'Elevator Maintenance',
                    '@iexact': 'janitoRial',
                    '@in': ("Roofing Services", "Plumbing and Pipefitting"),
                    '@contains': 'Waste',
                    '@icontains': 'energy engineering',
                    '@startswith': 'HVAC',
                    '@istartswith': 'hvac',
                    '@endswith': 'Maintenance',
                    '@iendswith': 'dEVelopment',
                    '@regex': '\d+$',
                    '@iregex': 'air.*development$'
                },
                'pools__pool__number': {
                    '@exact': '8',
                    '@iexact': '9',
                    '@in': ('1', '3', '5B', '16')
                },
                'pools__pool__vehicle': {
                    '@exact': 'OASIS_SB',
                    '@iexact': 'oasis',
                    '@in': ("HCATS", "BMO_SB"),
                    '@contains': 'SB',
                    '@icontains': 'oasis',
                    '@startswith': 'O',
                    '@istartswith': 'bm',
                    '@endswith': 'SB',
                    '@iendswith': '_sb',
                    '@regex': '^(OASIS|HCATS)_SB$',
                    '@iregex': '^(oaSis|hCaTs)_Sb$'
                },
                'pools__pool__threshold': {
                    '@exact': '$15 million',
                    '@iexact': '$7.5 MILLION',
                    '@in': ("1000 employee", "$18 million", "500 employee"),
                    '@contains': 'employee',
                    '@icontains': 'EmplOYeE',
                    '@startswith': '$38.5',
                    '@istartswith': '$38.5',
                    '@endswith': 'million',
                    '@iendswith': 'MillIon',
                    '@regex': '^\d+\s+',
                    '@iregex': '(500 EMPLOYEE|MILLION)'
                },
                'pools__pool__naics__code': {
                    '@exact': '541330',
                    '@iexact': '541712c',
                    '@in': ("541711", "238290", "561730B"),
                    '@contains': '622',
                    '@icontains': 'b',
                    '@startswith': '54',
                    '@istartswith': '2382',
                    '@endswith': 'A',
                    '@iendswith': 'c',
                    '@regex': '[^\d]+$',
                    '@iregex': '^(23|56)'
                },
                'pools__pool__naics__root_code': {
                    '@exact': '541330',
                    '@iexact': '541712',
                    '@in': ("541711", "238290", "561730"),
                    '@contains': '622',
                    '@icontains': '990',
                    '@startswith': '61',
                    '@istartswith': '5617',
                    '@endswith': '10',
                    '@iendswith': '20',
                    '@regex': '^[\d]+$',
                    '@iregex': '^(23|56)'
                },
                'pools__pool__naics__description': {
                    '@exact': 'Outdoor Advertising',
                    '@iexact': 'hvac maintenance',
                    '@in': ("Payroll Services", "Commissioning Services", "Testing Laboratories"),
                    '@contains': 'Accounting',
                    '@icontains': 'rEPair',
                    '@startswith': 'Engineering',
                    '@istartswith': 'r',
                    '@endswith': 'Services',
                    '@iendswith': 'advertIsing',
                    '@regex': '[/]+',
                    '@iregex': 'water\s+based'
                },
                'pools__setasides__code': {
                    '@exact': 'QF',
                    '@iexact': 'a2',
                    '@in': ('XX', 'A5', '27')
                },
                'pools__setasides__name': {
                    '@exact': 'WO',
                    '@iexact': 'hubz',
                    '@in': ('8(A)', 'SDVO', 'HubZ')
                },
                'pools__setasides__description': {
                    '@exact': 'Veteran Owned',
                    '@iexact': 'hubzone',
                    '@in': ("8(A)", "Woman Owned", "Small Disadvantaged Business"),
                    '@contains': 'Disadvantaged',
                    '@icontains': 'woman',
                    '@startswith': '8',
                    '@istartswith': 'hu',
                    '@endswith': 'Owned',
                    '@iendswith': 'owned',
                    '@regex': '^\d+',
                    '@iregex': 'Vet(eran)?'
                },
                'pools__setasides__far_order': {
                    '@exact': 3,
                    '@lt': 4,
                    '@lte': 4, 
                    '@gt': 3, 
                    '@gte': 3,
                    '@range': (2, 5),
                    '@in': (2, 3, 5)
                },
                'pools__zones__id': {
                    '@exact': 2,
                    '@lt': 4,
                    '@lte': 4, 
                    '@gt': 3, 
                    '@gte': 3,
                    '@range': (2, 5),
                    '@in': (2, 3, 5)
                },
                'pools__zones__state': {
                    '@exact': 'PA',
                    '@iexact': 'mE',
                    '@in': ('PA', 'NC', 'TX', 'NY')
                },
                'pools__cms__name': {
                    '@exact': 'Ken Scott',
                    '@iexact': 'daniel eke',
                    '@in': ("Ken Scott", "Daniel Eke"),
                    '@contains': 'Taylor',
                    '@icontains': 'taylor',
                    '@startswith': 'Ben',
                    '@istartswith': 'ben',
                    '@endswith': 'Shea',
                    '@iendswith': 'shea',
                    '@regex': '^[A-Za-z]{4}\s+',
                    '@iregex': '^da(n|na)'
                },
                'pools__cms__phone': {
                    '@exact': '703-821-0678',
                    '@iexact': '703-821-0678',
                    '@in': ("703-821-0678", "571-262-3144", "937-912-6102"),
                    '@contains': '-426-',
                    '@icontains': '-426-',
                    '@startswith': '757',
                    '@istartswith': '757',
                    '@endswith': '6551',
                    '@iendswith': '6551',
                    '@regex': 'x\d+$',
                    '@iregex': '(304|703)-\d{3}'
                },
                'pools__cms__email': {
                    '@exact': 'OASIS@act-i.com',
                    '@iexact': 'oasis@act-i.com',
                    '@in': ("OASIS@act-i.com", "hcats_sb@deepmile.com", "Finance@exemplarent.com"),
                    '@contains': 'ibm',
                    '@icontains': 'IbM',
                    '@startswith': 'hcats',
                    '@istartswith': 'HcAtS',
                    '@endswith': 'com',
                    '@iendswith': 'cOM',
                    '@regex': '\d+',
                    '@iregex': '\.(com|net)$'
                },
                'pools__pms__name': {
                    '@exact': 'Phil Sahady',
                    '@iexact': 'phil sahady',
                    '@in': ("Phil Sahady", "Charles A. Colon,  III"),
                    '@contains': 'Glass',
                    '@icontains': 'glass',
                    '@startswith': 'John',
                    '@istartswith': 'john',
                    '@endswith': 'Carroll',
                    '@iendswith': 'carroll',
                    '@regex': '^[A-Za-z]{4}\s+',
                    '@iregex': '^dr\.?'
                },
                'pools__pms__phone': {
                    '@exact': '703-642-2380',
                    '@iexact': '703-642-2380',
                    '@in': ("703-642-2380", "937-912-6102", "703-435-2260"),
                    '@contains': '-824-',
                    '@icontains': '-824-',
                    '@startswith': '719',
                    '@istartswith': '719',
                    '@endswith': '6102',
                    '@iendswith': '6102',
                    '@regex': 'x\d+$',
                    '@iregex': '(937|703)-\d{3}'
                },
                'pools__pms__email': {
                    '@exact': 'OASIS@niksoft.com',
                    '@iexact': 'oasis@niksoft.com',
                    '@in': ("OASIS@niksoft.com", "OASISSB@integrity-apps.com", "hcats@arcaspicio.com"),
                    '@contains': 'apps',
                    '@icontains': 'APPS',
                    '@startswith': 'hcats',
                    '@istartswith': 'HcAtS',
                    '@endswith': 'com',
                    '@iendswith': 'cOM',
                    '@regex': '\d+',
                    '@iregex': '\.(com|net)$'
                }
            }
        }


class VendorRetrieveTest(BaseVendorTest):
    def schema(self):
        return {
            'object': {
                '&007901598': ('name', 'equal', 'Battelle Memorial Institute'),
                '&132220604': ('name', 'equal', 'Censeo Consulting Group'),
                '&001014182': ('name', 'equal', 'Dynamics Research Corporation'),
                '#345': (),
                '#ABCDEFG': ()
            }
        }
