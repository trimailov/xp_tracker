# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TaskFinishingHistory'
        db.create_table('xp_tracker_app_taskfinishinghistory', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('task', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['xp_tracker_app.Task'])),
            ('time_fin', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('xp_tracker_app', ['TaskFinishingHistory'])


    def backwards(self, orm):
        # Deleting model 'TaskFinishingHistory'
        db.delete_table('xp_tracker_app_taskfinishinghistory')


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
            'story': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['xp_tracker_app.Story']"}),
            'task_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'time_est': ('django.db.models.fields.DateTimeField', [], {}),
            'time_fin': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'time_start': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        'xp_tracker_app.taskfinishinghistory': {
            'Meta': {'object_name': 'TaskFinishingHistory'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'task': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['xp_tracker_app.Task']"}),
            'time_fin': ('django.db.models.fields.DateTimeField', [], {})
        }
    }

    complete_apps = ['xp_tracker_app']