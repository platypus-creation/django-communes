# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'Commune.accuracy'
        db.alter_column('communes_commune', 'accuracy', self.gf('django.db.models.fields.FloatField')(null=True))


    def backwards(self, orm):
        
        # Changing field 'Commune.accuracy'
        db.alter_column('communes_commune', 'accuracy', self.gf('django.db.models.fields.FloatField')(default=1))


    models = {
        'communes.commune': {
            'Meta': {'object_name': 'Commune'},
            'accuracy': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'insee_code': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'point': ('django.contrib.gis.db.models.fields.PointField', [], {'null': 'True', 'blank': 'True'}),
            'population': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'postal_code': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'})
        }
    }

    complete_apps = ['communes']
