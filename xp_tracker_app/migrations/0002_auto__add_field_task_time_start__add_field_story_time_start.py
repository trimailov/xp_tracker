# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Task.time_start'
        db.add_column('xp_tracker_app_task', 'time_start',
                      self.gf('django.db.models.fields.DateField')(blank=True, auto_now_add=True, default=datetime.datetime(2014, 5, 30, 0, 0)),
                      keep_default=False)

        # Adding field 'Story.time_start'
        db.add_column('xp_tracker_app_story', 'time_start',
                      self.gf('django.db.models.fields.DateField')(blank=True, auto_now_add=True, default=datetime.datetime(2014, 5, 30, 0, 0)),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Task.time_start'
        db.delete_column('xp_tracker_app_task', 'time_start')

        # Deleting field 'Story.time_start'
        db.delete_column('xp_tracker_app_story', 'time_start')


    models = {
        'xp_tracker_app.story': {
            'Meta': {'object_name': 'Story'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'story_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'time_est': ('django.db.models.fields.DateField', [], {}),
            'time_start': ('django.db.models.fields.DateField', [], {'blank': 'True', 'auto_now_add': 'True'})
        },
        'xp_tracker_app.task': {
            'Meta': {'object_name': 'Task'},
            'developer': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'iteration': ('django.db.models.fields.IntegerField', [], {}),
            'task_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'time_est': ('django.db.models.fields.DateField', [], {}),
            'time_fin': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'null': 'True'}),
            'time_start': ('django.db.models.fields.DateField', [], {'blank': 'True', 'auto_now_add': 'True'})
        }
    }

    complete_apps = ['xp_tracker_app']