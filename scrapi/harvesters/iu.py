'''
Harvester for the IUScholarWorks Repository for the SHARE project

Example API call: https://scholarworks.iu.edu/dspace-oai/request?verb=ListRecords&metadataPrefix=oai_dc
'''
from __future__ import unicode_literals

from scrapi.base import OAIHarvester


class IuHarvester(OAIHarvester):
    short_name = 'iu'
    long_name = "Indiana University Libraries' IUScholarWorks"
    url = 'https://scholarworks.iu.edu'

    base_url = 'https://scholarworks.iu.edu/dspace-oai/request'
    property_list = ['date', 'format', 'identifier', 'type', 'relation', 'setSpec', 'language', 'rights']

    approved_sets = [
        u'com_2022_14017',
        u'com_2022_21',
        u'com_2022_9004',
        u'com_2022_3298',
        u'com_2022_315',
        u'com_2022_6637',
        u'com_2022_705',
        u'com_2022_13581',
        u'com_2022_12958',
        u'com_2022_7910',
        u'com_2022_3579',
        u'com_2022_6876',
        u'com_2022_6461',
        u'com_2022_13582',
        u'com_2022_12993',
        u'com_2022_3127',
        u'com_2022_301',
        u'com_2022_310',
        u'com_2022_151',
        u'com_2022_440',
        u'com_2022_14048',
        u'com_2022_3088',
        u'com_2022_14124',
        u'com_2022_13583',
        u'com_2022_13982',
        u'com_2022_1129',
        u'com_2022_12970',
        u'com_2022_1168',
        u'com_2022_2566',
        u'com_2022_3849',
        u'com_2022_28',
        u'com_2022_706',
        u'com_2022_3833',
        u'com_2022_8934',
        u'com_2022_443',
        u'com_2022_13587',
        u'com_2022_3193',
        u'com_2022_17',
        u'com_2022_6464',
        u'com_2022_314',
        u'com_2022_6775',
        u'com_2022_154',
        u'com_2022_9015',
        u'com_2022_9016',
        u'com_2022_3386',
        u'com_2022_3787',
        u'com_2022_13580',
        u'com_2022_8494',
        u'com_2022_439',
        u'com_2022_6792',
        u'com_2022_324',
        u'com_2022_3160',
        u'com_2022_13436',
        u'com_2022_6745',
        u'com_2022_7911',
        u'com_2022_14208',
        u'com_2022_186',
        u'com_2022_320',
        u'com_2022_3789',
        u'com_2022_13590',
        u'com_2022_14242',
        u'com_2022_13588',
        u'com_2022_13431',
        u'com_2022_14015',
        u'com_2022_1026',
        u'com_2022_3092',
        u'com_2022_13584',
        u'com_2022_12995',
        u'com_2022_13057',
        u'com_2022_356',
        u'com_2022_357',
        u'com_2022_14235',
        u'com_2022_14205',
        u'com_2022_3377',
        u'com_2022_13984',
        u'com_2022_13432',
        u'com_2022_12992',
        u'com_2022_145',
        u'com_2022_185',
        u'com_2022_13945',
        u'com_2022_3788',
        u'com_2022_13585',
        u'com_2022_600',
        u'com_2022_3376',
        u'com_2022_188',
        u'com_2022_14241',
        u'com_2022_13586',
        u'com_2022_14236',
        u'com_2022_12971',
        u'com_2022_3850',
        u'com_2022_3631',
        u'com_2022_13589',
        u'com_2022_3084',
        u'com_2022_14076',
        u'com_2022_13056',
        u'com_2022_3129',
        u'com_2022_3131',
        u'com_2022_8979',
        u'com_2022_12991',
        u'com_2022_12994'
    ]

    timezone_granularity = True