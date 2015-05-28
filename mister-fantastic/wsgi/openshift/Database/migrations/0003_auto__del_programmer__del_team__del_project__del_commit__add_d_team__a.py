# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Programmer'
        db.delete_table(u'Database_programmer')

        # Deleting model 'Team'
        db.delete_table(u'Database_team')

        # Deleting model 'Project'
        db.delete_table(u'Database_project')

        # Deleting model 'Commit'
        db.delete_table(u'Database_commit')

        # Adding model 'D_TEAM'
        db.create_table(u'Database_d_team', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('NAME', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('PORJECT', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Database.D_PROJECT'])),
        ))
        db.send_create_signal(u'Database', ['D_TEAM'])

        # Adding model 'D_PROJECT'
        db.create_table(u'Database_d_project', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('LINK', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'Database', ['D_PROJECT'])

        # Adding model 'D_COMMIT'
        db.create_table(u'Database_d_commit', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('PROGRAMMER', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Database.D_PROGRAMMER'])),
            ('DATE', self.gf('django.db.models.fields.DateTimeField')()),
            ('NEW', self.gf('django.db.models.fields.IntegerField')()),
            ('DEL', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'Database', ['D_COMMIT'])

        # Adding model 'D_PROGRAMMER'
        db.create_table(u'Database_d_programmer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('NAME', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('TEAM', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Database.D_TEAM'])),
        ))
        db.send_create_signal(u'Database', ['D_PROGRAMMER'])


    def backwards(self, orm):
        # Adding model 'Programmer'
        db.create_table(u'Database_programmer', (
            ('team', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Database.Team'])),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('programmer_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'Database', ['Programmer'])

        # Adding model 'Team'
        db.create_table(u'Database_team', (
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Database.Project'])),
            ('team_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'Database', ['Team'])

        # Adding model 'Project'
        db.create_table(u'Database_project', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('project_link', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'Database', ['Project'])

        # Adding model 'Commit'
        db.create_table(u'Database_commit', (
            ('commit_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('commit_del', self.gf('django.db.models.fields.IntegerField')()),
            ('programmer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Database.Programmer'])),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('commit_changes', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'Database', ['Commit'])

        # Deleting model 'D_TEAM'
        db.delete_table(u'Database_d_team')

        # Deleting model 'D_PROJECT'
        db.delete_table(u'Database_d_project')

        # Deleting model 'D_COMMIT'
        db.delete_table(u'Database_d_commit')

        # Deleting model 'D_PROGRAMMER'
        db.delete_table(u'Database_d_programmer')


    models = {
        u'Database.d_commit': {
            'DATE': ('django.db.models.fields.DateTimeField', [], {}),
            'DEL': ('django.db.models.fields.IntegerField', [], {}),
            'Meta': {'object_name': 'D_COMMIT'},
            'NEW': ('django.db.models.fields.IntegerField', [], {}),
            'PROGRAMMER': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Database.D_PROGRAMMER']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'Database.d_programmer': {
            'Meta': {'object_name': 'D_PROGRAMMER'},
            'NAME': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'TEAM': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Database.D_TEAM']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'Database.d_project': {
            'LINK': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'Meta': {'object_name': 'D_PROJECT'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'Database.d_team': {
            'Meta': {'object_name': 'D_TEAM'},
            'NAME': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'PORJECT': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Database.D_PROJECT']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['Database']