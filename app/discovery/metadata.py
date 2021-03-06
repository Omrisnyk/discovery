
from categories import models as categories
from vendors import models as vendors
from contracts import models as contracts


class DiscoveryMetadata(object):
    
    def __init__(self):
        sam_md = vendors.SamLoad.objects.exclude(load_time__isnull=True).order_by('-load_time')
        fpds_md = contracts.FPDSLoad.objects.exclude(load_date__isnull=True).order_by('-load_date')
        
        if len(sam_md) > 0:
            self.sam_load_date = sam_md[0].load_time.date()
        else: 
            self.sam_load_date = None
        if len(fpds_md) > 0:
            self.fpds_load_date = fpds_md[0].load_date
        else:
            self.fpds_load_date = None
