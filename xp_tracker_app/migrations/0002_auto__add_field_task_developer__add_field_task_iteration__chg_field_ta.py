# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Task.developer'
        db.add_column('xp_tracker_app_task', 'developer',
                      self.gf('django.db.models.fields.CharField')(max_length=60, default='GvR'),
                      keep_default=False)

        # Adding field 'Task.iteration'
        db.add_column('xp_tracker_app_task', 'iteration',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)


        # Changing field 'Task.task_name'
        db.alter_column('xp_tracker_app_task', 'task_name', self.gf('django.db.models.fields.CharField')(max_length=200))

        # Changing field 'Task.time_fin'
        db.alter_column('xp_tracker_app_task', 'time_fin', self.gf('django.db.models.fields.DateTimeField')(null=True))

        # Changing field 'Story.story_name'
        db.alter_column('xp_tracker_app_story', 'story_name', self.gf('django.db.models.fields.CharField')(max_length=200))

    def backwards(self, orm):
        # Deleting field 'Task.developer'
        db.delete_column('xp_tracker_app_task', 'developer')

        # Deleting field 'Task.iteration'
        db.delete_column('xp_tracker_app_task', 'iteration')


        # Changing field 'Task.task_name'
        db.alter_column('xp_tracker_app_task', 'task_name', self.gf('django.db.models.fields.CharField')(max_length=300))

        # Changing field 'Task.time_fin'
        db.alter_column('xp_tracker_app_task', 'time_fin', self.gf('django.db.models.fields.DateField')(null=True))

        # Changing field 'Story.story_name'
        db.alter_column('xp_tracker_app_story', 'story_name', self.gf('django.db.models.fields.CharField')(max_length=300))

    models = {
        'xp_tracker_app.story': {
            'Meta': {'object_name': 'Story'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'story_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'time_est': ('django.db.models.fields.DateField', [], {})
        },
        'xp_tracker_app.task': {
            'Meta': {'object_name': 'Task'},
            'developer': ('django.db.models.fields.CharField', [], {'max_length': '60', 'default': "'GvR'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'iteration': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'task_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'time_est': ('django.db.models.fields.DateField', [], {}),
            'time_fin': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'null': 'True'})
        }
    }

    complete_apps = ['xp_tracker_app']