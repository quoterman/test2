# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Project'
        db.create_table(u'Database_project', (
            ('Project_id', self.gf('django.db.models.fields.AutoField')(max_length=10, primary_key=True)),
            ('Project_link', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'Database', ['Project'])

        # Adding model 'Team'
        db.create_table(u'Database_team', (
            ('Team_id', self.gf('django.db.models.fields.AutoField')(max_length=10, primary_key=True)),
            ('Team_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Database.Project'])),
        ))
        db.send_create_signal(u'Database', ['Team'])

        # Adding model 'Programmer'
        db.create_table(u'Database_programmer', (
            ('Programmer_id', self.gf('django.db.models.fields.AutoField')(max_length=10, primary_key=True)),
            ('Programmer_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('team', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Database.Team'])),
        ))
        db.send_create_signal(u'Database', ['Programmer'])

        # Adding model 'Commit'
        db.create_table(u'Database_commit', (
            ('Commit_id', self.gf('django.db.models.fields.AutoField')(max_length=10, primary_key=True)),
            ('programmer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Database.Programmer'])),
            ('Commit_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('Commit_changes', self.gf('django.db.models.fields.IntegerField')()),
            ('Commit_del', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'Database', ['Commit'])


    def backwards(self, orm):
        # Deleting model 'Project'
        db.delete_table(u'Database_project')

        # Deleting model 'Team'
        db.delete_table(u'Database_team')

        # Deleting model 'Programmer'
        db.delete_table(u'Database_programmer')

        # Deleting model 'Commit'
        db.delete_table(u'Database_commit')


    models = {
        u'Database.commit': {
            'Commit_changes': ('django.db.models.fields.IntegerField', [], {}),
            'Commit_date': ('django.db.models.fields.DateTimeField', [], {}),
            'Commit_del': ('django.db.models.fields.IntegerField', [], {}),
            'Commit_id': ('django.db.models.fields.AutoField', [], {'max_length': '10', 'primary_key': 'True'}),
            'Meta': {'object_name': 'Commit'},
            'programmer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Database.Programmer']"})
        },
        u'Database.programmer': {
            'Meta': {'object_name': 'Programmer'},
            'Programmer_id': ('django.db.models.fields.AutoField', [], {'max_length': '10', 'primary_key': 'True'}),
            'Programmer_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Database.Team']"})
        },
        u'Database.project': {
            'Meta': {'object_name': 'Project'},
            'Project_id': ('django.db.models.fields.AutoField', [], {'max_length': '10', 'primary_key': 'True'}),
            'Project_link': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'Database.team': {
            'Meta': {'object_name': 'Team'},
            'Team_id': ('django.db.models.fields.AutoField', [], {'max_length': '10', 'primary_key': 'True'}),
            'Team_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Database.Project']"})
        }
    }

    complete_apps = ['Database']