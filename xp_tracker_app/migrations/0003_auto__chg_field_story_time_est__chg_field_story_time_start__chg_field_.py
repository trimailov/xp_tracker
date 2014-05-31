# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Story.time_est'
        db.alter_column('xp_tracker_app_story', 'time_est', self.gf('django.db.models.fields.DateTimeField')())

        # Changing field 'Story.time_start'
        db.alter_column('xp_tracker_app_story', 'time_start', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True))

        # Changing field 'Task.time_est'
        db.alter_column('xp_tracker_app_task', 'time_est', self.gf('django.db.models.fields.DateTimeField')())

        # Changing field 'Task.time_start'
        db.alter_column('xp_tracker_app_task', 'time_start', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True))

    def backwards(self, orm):

        # Changing field 'Story.time_est'
        db.alter_column('xp_tracker_app_story', 'time_est', self.gf('django.db.models.fields.DateField')())

        # Changing field 'Story.time_start'
        db.alter_column('xp_tracker_app_story', 'time_start', self.gf('django.db.models.fields.DateField')(auto_now_add=True))

        # Changing field 'Task.time_est'
        db.alter_column('xp_tracker_app_task', 'time_est', self.gf('django.db.models.fields.DateField')())

        # Changing field 'Task.time_start'
        db.alter_column('xp_tracker_app_task', 'time_start', self.gf('django.db.models.fields.DateField')(auto_now_add=True))

    models = {
        'xp_tracker_app.story': {
            'Meta': {'object_name': 'Story'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'story_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'time_est': ('django.db.models.fields.DateTimeField', [], {}),
            'time_start': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        'xp_tracker_app.task': {
            'Meta': {'object_name': 'Task'},
            'developer': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'iteration': ('django.db.models.fields.IntegerField', [], {}),
            'task_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'time_est': ('django.db.models.fields.DateTimeField', [], {}),
            'time_fin': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'null': 'True'}),
            'time_start': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['xp_tracker_app']