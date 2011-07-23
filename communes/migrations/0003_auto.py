# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding index on 'Commune', fields ['insee_code']
        db.create_index('communes_commune', ['insee_code'])

        # Adding index on 'Commune', fields ['postal_code']
        db.create_index('communes_commune', ['postal_code'])

        # Adding index on 'Commune', fields ['population']
        db.create_index('communes_commune', ['population'])


    def backwards(self, orm):
        
        # Removing index on 'Commune', fields ['population']
        db.delete_index('communes_commune', ['population'])

        # Removing index on 'Commune', fields ['postal_code']
        db.delete_index('communes_commune', ['postal_code'])

        # Removing index on 'Commune', fields ['insee_code']
        db.delete_index('communes_commune', ['insee_code'])


    models = {
        'communes.commune': {
            'Meta': {'object_name': 'Commune'},
            'accuracy': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'insee_code': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '10', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'point': ('django.contrib.gis.db.models.fields.PointField', [], {'null': 'True', 'blank': 'True'}),
            'population': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_index': 'True'}),
            'postal_code': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '10', 'blank': 'True'})
        }
    }

    complete_apps = ['communes']
