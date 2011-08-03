from django.db import models
from django.contrib.gis.db import models as geomodels

class Commune(geomodels.Model):
    """French city"""
    name = models.CharField(blank=True, max_length=100)
    
    postal_code = models.CharField(blank=True, max_length=10, db_index=True)
    insee_code = models.CharField(blank=True, max_length=10, db_index=True)
    population = models.IntegerField(default=0, db_index=True)
    point = geomodels.PointField(null=True, blank=True)
    accuracy = models.FloatField(null=True, blank=True)
    objects = geomodels.GeoManager()
    
    class Meta:
        ordering = ('name',)

    def __unicode__(self):
        return self.name

    def lng_lat(self):
        return map(lambda x : float(x), str(self.point).replace("POINT (", "").replace(")", "").split(" "))
    
    @property
    def latitude(self):
        return self.lng_lat()[1]

    @property
    def longitude(self):
        return self.lng_lat()[0]
