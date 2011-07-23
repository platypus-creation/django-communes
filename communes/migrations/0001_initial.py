# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Commune'
        db.create_table('communes_commune', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('postal_code', self.gf('django.db.models.fields.CharField')(max_length=10, blank=True)),
            ('insee_code', self.gf('django.db.models.fields.CharField')(max_length=10, blank=True)),
            ('population', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('point', self.gf('django.contrib.gis.db.models.fields.PointField')(null=True, blank=True)),
            ('accuracy', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal('communes', ['Commune'])


    def backwards(self, orm):
        
        # Deleting model 'Commune'
        db.delete_table('communes_commune')


    models = {
        'communes.commune': {
            'Meta': {'object_name': 'Commune'},
            'accuracy': ('django.db.models.fields.FloatField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'insee_code': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'point': ('django.contrib.gis.db.models.fields.PointField', [], {'null': 'True', 'blank': 'True'}),
            'population': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'postal_code': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'})
        }
    }

    complete_apps = ['communes']
