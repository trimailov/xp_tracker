# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Story'
        db.create_table('xp_tracker_app_story', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('story_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('time_est', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal('xp_tracker_app', ['Story'])

        # Adding model 'Task'
        db.create_table('xp_tracker_app_task', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('task_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('time_est', self.gf('django.db.models.fields.DateField')()),
            ('time_fin', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('developer', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('iteration', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('xp_tracker_app', ['Task'])


    def backwards(self, orm):
        # Deleting model 'Story'
        db.delete_table('xp_tracker_app_story')

        # Deleting model 'Task'
        db.delete_table('xp_tracker_app_task')


    models = {
        'xp_tracker_app.story': {
            'Meta': {'object_name': 'Story'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'story_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'time_est': ('django.db.models.fields.DateField', [], {})
        },
        'xp_tracker_app.task': {
            'Meta': {'object_name': 'Task'},
            'developer': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'iteration': ('django.db.models.fields.IntegerField', [], {}),
            'task_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'time_est': ('django.db.models.fields.DateField', [], {}),
            'time_fin': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['xp_tracker_app']