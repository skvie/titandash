# Generated by Django 2.1.7 on 2019-06-29 12:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artifact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Specify the name of this artifact.', max_length=255, verbose_name='Name')),
                ('key', models.PositiveIntegerField(help_text='Specify the key of this artifact.', verbose_name='Key')),
                ('image', models.CharField(help_text='Specify the image path that leads to this artifact.', max_length=255, verbose_name='Image')),
            ],
            options={
                'verbose_name': 'Artifact',
                'verbose_name_plural': 'Artifacts',
            },
        ),
        migrations.CreateModel(
            name='ArtifactOwned',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owned', models.BooleanField(default=False, help_text='Specify if this artifact is owned or not.', verbose_name='Owned')),
                ('artifact', models.ForeignKey(help_text='Specify the artifact being used.', on_delete=django.db.models.deletion.CASCADE, to='titandash.Artifact', verbose_name='Artifact')),
            ],
            options={
                'verbose_name': 'Artifact Owned',
                'verbose_name_plural': 'Artifacts Owned',
            },
        ),
        migrations.CreateModel(
            name='ArtifactStatistics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artifacts', models.ManyToManyField(help_text='Choose the artifacts associated with this artifact statistics instance.', to='titandash.ArtifactOwned', verbose_name='Artifacts')),
            ],
            options={
                'verbose_name': 'Artifact Statistics',
                'verbose_name_plural': 'Artifact Statistics',
            },
        ),
        migrations.CreateModel(
            name='BotInstance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(choices=[('running', 'RUNNING'), ('paused', 'PAUSED'), ('stopped', 'STOPPED')], default='stopped', help_text='Current state of the bot.', max_length=255, verbose_name='State')),
                ('started', models.DateTimeField(blank=True, help_text='The date that the bot was started.', null=True, verbose_name='Started')),
                ('current_function', models.CharField(blank=True, help_text='The current function being executed by the bot.', max_length=255, null=True, verbose_name='Current Function')),
                ('current_stage', models.PositiveIntegerField(blank=True, null=True, verbose_name='Current Stage')),
                ('next_action_run', models.DateTimeField(blank=True, null=True, verbose_name='Next Action Run')),
                ('next_prestige', models.DateTimeField(blank=True, null=True, verbose_name='Next Timed Prestige')),
                ('next_stats_update', models.DateTimeField(blank=True, null=True, verbose_name='Next Stats Update')),
                ('next_recovery_reset', models.DateTimeField(blank=True, null=True, verbose_name='Next Recovery Reset')),
                ('next_daily_achievement_check', models.DateTimeField(blank=True, null=True, verbose_name='Next Daily Achievement Check')),
                ('next_heavenly_strike', models.DateTimeField(blank=True, null=True, verbose_name='Next Heavenly Strike')),
                ('next_deadly_strike', models.DateTimeField(blank=True, null=True, verbose_name='Next Deadly Strike')),
                ('next_hand_of_midas', models.DateTimeField(blank=True, null=True, verbose_name='Next Hand Of Midas')),
                ('next_fire_sword', models.DateTimeField(blank=True, null=True, verbose_name='Next Fire Sword')),
                ('next_war_cry', models.DateTimeField(blank=True, null=True, verbose_name='Next War Cry')),
                ('next_shadow_clone', models.DateTimeField(blank=True, null=True, verbose_name='Next Shadow Clone')),
                ('next_artifact_upgrade', models.CharField(blank=True, max_length=255, null=True, verbose_name='Next Artifact Upgrade')),
            ],
            options={
                'verbose_name': 'Bot Instance',
                'verbose_name_plural': 'Bot Instances',
            },
        ),
        migrations.CreateModel(
            name='BotStatistics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('premium_ads', models.PositiveIntegerField(default=0, help_text='How many premium ads have been earned and tracked by the bot.', verbose_name='Premium Ads')),
                ('actions', models.PositiveIntegerField(default=0, help_text='How many sets of actions have been ran by the bot.', verbose_name='Actions')),
                ('updates', models.PositiveIntegerField(default=0, help_text='How many times has bot statistics been updated.', verbose_name='Updates')),
            ],
            options={
                'verbose_name': 'Bot Statistics',
                'verbose_name_plural': 'Bot Statistics',
            },
        ),
        migrations.CreateModel(
            name='Configuration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('soft_shutdown_on_critical_error', models.BooleanField(default=False, help_text='Should a soft shutdown be performed if the bot runs into a critical error during a session.', verbose_name='Soft Shutdown On Critical Error')),
                ('soft_shutdown_update_stats', models.BooleanField(default=True, help_text='Enable stats updates when a soft shutdown is performed.', verbose_name='Update Stats On Soft Shutdown')),
                ('post_action_min_wait_time', models.PositiveIntegerField(default=0, help_text='Determine the minimum amount of seconds to wait after an in game function is finished executing.', verbose_name='Post Action Min Wait Time')),
                ('post_action_max_wait_time', models.PositiveIntegerField(default=1, help_text='Determine the maximum amount of seconds to wait after an in game function is finished executing.', verbose_name='Post Action Max Wait Time')),
                ('emulator', models.CharField(choices=[('nox', 'Nox Emulator')], default='nox', help_text='Which emulator service is being used?', max_length=255, verbose_name='Emulator')),
                ('enable_premium_ad_collect', models.BooleanField(default=True, help_text='Enable the premium ad collection, Note: This will only work if you have unlocked the ability to skip ads, watching ads is not supported.', verbose_name='Enable Premium Ad Collection')),
                ('enable_egg_collection', models.BooleanField(default=True, help_text='Enable the ability to collect and hatch eggs in game.', verbose_name='Enable Egg Collection')),
                ('enable_tapping', models.BooleanField(default=True, help_text='Enable the ability to tap on titans (This also enables the clicking of fairies in game).', verbose_name='Enable Tapping')),
                ('enable_tournaments', models.BooleanField(default=True, help_text='Enable the ability to enter and participate in tournaments.', verbose_name='Enable Tournaments')),
                ('enable_daily_achievements', models.BooleanField(default=True, help_text='Enable the ability to check and collect daily achievements in game.', verbose_name='Enable Daily Achievements')),
                ('daily_achievements_check_on_start', models.BooleanField(default=False, help_text='Should daily achievements being checked for when a session is started.', verbose_name='Check Daily Achievements On Session Start')),
                ('daily_achievements_check_every_x_hours', models.PositiveIntegerField(default=1, help_text='Determine how many hours between each daily achievement check.', verbose_name='Check Daily Achievements Every X Hours')),
                ('run_actions_every_x_seconds', models.PositiveIntegerField(default=25, help_text='Determine how many seconds between each execution of all in game actions.', verbose_name='Run Actions Every X Seconds')),
                ('run_actions_on_start', models.BooleanField(default=False, help_text='Should all actions be executed when a session is started.', verbose_name='Run Actions On Session Start')),
                ('order_level_heroes', models.PositiveIntegerField(choices=[(1, '1'), (2, '2'), (3, '3')], default=1, help_text='Select the order that heroes will be levelled in game (1, 2, 3).')),
                ('order_level_master', models.PositiveIntegerField(choices=[(1, '1'), (2, '2'), (3, '3')], default=2, help_text='Select the order that the sword master will be levelled in game (1, 2, 3).')),
                ('order_level_skills', models.PositiveIntegerField(choices=[(1, '1'), (2, '2'), (3, '3')], default=3, help_text='Select the order that skills will be levelled in game (1, 2, 3).')),
                ('enable_master', models.BooleanField(default=True, help_text='Enable the ability to level the sword master in game.', verbose_name='Enable Master')),
                ('master_level_intensity', models.PositiveIntegerField(default=5, help_text='Determine the amount of clicks performed whenever the sword master is levelled.', verbose_name='Master Level Intensity')),
                ('enable_heroes', models.BooleanField(default=True, help_text='Enable the ability level heroes in game.', verbose_name='Enable Heroes')),
                ('hero_level_intensity', models.PositiveIntegerField(default=3, help_text='Determine the amount of clicks performed on each hero when they are levelled.', verbose_name='Hero Level Intensity')),
                ('enable_skills', models.BooleanField(default=True, help_text='Enable the ability to level and activate skills in game.', verbose_name='Enable Skills')),
                ('activate_skills_on_start', models.BooleanField(default=True, help_text='Should skills be activated when a session is started.', verbose_name='Activate Skills On Session Start')),
                ('interval_heavenly_strike', models.PositiveIntegerField(default=0, help_text='How many seconds between each activation of the heavenly strike skill.', verbose_name='Heavenly Strike Interval')),
                ('interval_deadly_strike', models.PositiveIntegerField(default=20, help_text='How many seconds between each activation of the deadly strike skill.', verbose_name='Deadly Strike Interval')),
                ('interval_hand_of_midas', models.PositiveIntegerField(default=30, help_text='How many seconds between each activation of the hand of midas skill.', verbose_name='Hand Of Midas Interval')),
                ('interval_fire_sword', models.PositiveIntegerField(default=40, help_text='How many seconds between each activation of the fire sword skill.', verbose_name='Fire Sword Interval')),
                ('interval_war_cry', models.PositiveIntegerField(default=50, help_text='How many seconds between each activation of the war cry skill.', verbose_name='War Cry Interval')),
                ('interval_shadow_clone', models.PositiveIntegerField(default=60, help_text='How many seconds between each activation of the shadow clone skill.', verbose_name='Shadow Clone Interval')),
                ('force_enabled_skills_wait', models.BooleanField(default=False, help_text='Based on the intervals determined above, should skill activation wait until the largest interval is surpassed.', verbose_name='Force Enabled Skills Wait')),
                ('max_skill_if_possible', models.BooleanField(default=True, help_text="Should a skill be levelled to it's maximum available amount if the option is present when a single level is bought.", verbose_name='Max Skill If Possible')),
                ('skill_level_intensity', models.PositiveIntegerField(default=10, help_text='Determine the amount of clicks performed on each skill when levelled.', verbose_name='Skill Level Intensity')),
                ('enable_auto_prestige', models.BooleanField(default=True, help_text='Enable the ability to automatically prestige in game.', verbose_name='Enable Auto Prestige')),
                ('prestige_x_minutes', models.PositiveIntegerField(default=45, help_text="Determine the amount of minutes between each auto prestige process. This can be used for farming, or as a hard limit that is used if the thresholds below aren't met within this time. (0 = off).", verbose_name='Prestige In X Minutes')),
                ('prestige_at_stage', models.PositiveIntegerField(default=0, help_text='Determine the stage needed before the prestige process is started (Once you reach/pass this stage, you will prestige). (0 = off).', verbose_name='Prestige At Stage')),
                ('prestige_at_max_stage', models.BooleanField(default=False, help_text='Should a prestige take place once your max stage has been reached? (Stats must be up to date).', verbose_name='Prestige At Max Stage')),
                ('prestige_at_max_stage_percent', models.DecimalField(decimal_places=3, default=0, help_text='Determine if you would like to perform an automatic prestige once a certain percent of your max stage has been reached. You may use values larger than 100 here to push your max stage. (0 = off).', max_digits=255, verbose_name='Prestige At Max Stage Percent')),
                ('enable_artifact_purchase', models.BooleanField(default=True, help_text='Enable the ability to purchase artifacts in game after a prestige has taken place.', verbose_name='Enable Artifact Purchase')),
                ('upgrade_owned_artifacts', models.BooleanField(default=True, help_text='Enable the ability to iterate through currently owned artifacts and upgrade them iteratively.', verbose_name='Upgrade Owned Artifacts')),
                ('shuffle_artifacts', models.BooleanField(default=True, help_text='Should owned artifacts be shuffled once calculated.', verbose_name='Shuffle Artifacts')),
                ('enable_stats', models.BooleanField(default=True, help_text='Enable the ability to update statistics during game sessions.', verbose_name='Enable Stats')),
                ('update_stats_on_start', models.BooleanField(default=False, help_text='Should stats be updated when a session is started.', verbose_name='Update Stats On Session Start')),
                ('update_stats_every_x_minutes', models.PositiveIntegerField(default=60, help_text='Determine how many minutes between each stats update in game.', verbose_name='Update Stats Every X Minutes')),
                ('recovery_check_interval_minutes', models.PositiveIntegerField(default=5, help_text='Determine how many minutes between each check that determines if the game has crashed/broke.', verbose_name='Recovery Check Interval Minutes')),
                ('recovery_allowed_failures', models.PositiveIntegerField(default=45, help_text='How many failures are allowed before the recovery process is started.', verbose_name='Recovery Allowed Failures')),
                ('enable_logging', models.BooleanField(default=True, help_text='Enable logging of information during sessions.', verbose_name='Enable Logging')),
                ('logging_level', models.CharField(choices=[('DEBUG', 'Debug'), ('INFO', 'Info'), ('WARNING', 'Warning'), ('ERROR', 'Error'), ('CRITICAL', 'Critical')], default='INFO', help_text='Determine the logging level used during sessions.', max_length=255, verbose_name='Logging Level')),
                ('bottom_artifact', models.ForeignKey(help_text='Specify which artifact is currently at the bottom of the artifact list. This is used to determine when to full stop during artifact parsing.', on_delete=django.db.models.deletion.CASCADE, related_name='bottom_artifact', to='titandash.Artifact', verbose_name='Bottom Artifact')),
                ('ignore_artifacts', models.ManyToManyField(blank=True, help_text='Should any specific artifacts be ignored regardless of them being owned or not.', related_name='ignore_artifacts', to='titandash.Artifact', verbose_name='Ignore Artifacts')),
                ('upgrade_artifacts', models.ManyToManyField(blank=True, help_text='Should any artifacts be specifically upgraded, disabling the above settings and choosing an artifact here will only upgrade this artifact.', related_name='upgrade_artifacts', to='titandash.Artifact', verbose_name='Upgrade Artifacts')),
            ],
            options={
                'verbose_name': 'Configuration',
                'verbose_name_plural': 'Configurations',
            },
        ),
        migrations.CreateModel(
            name='GameStatistics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('highest_stage_reached', models.CharField(blank=True, help_text='Highest stage reached in game overall.', max_length=255, null=True, verbose_name='Highest Stage Reached')),
                ('total_pet_level', models.CharField(blank=True, help_text='Total pet level reached in game overall.', max_length=255, null=True, verbose_name='Total Pet Level')),
                ('gold_earned', models.CharField(blank=True, help_text='How much gold has been earned in game overall.', max_length=255, null=True, verbose_name='Gold Earned')),
                ('taps', models.CharField(blank=True, help_text='How many taps have taken place in game overall.', max_length=255, null=True, verbose_name='Taps')),
                ('titans_killed', models.CharField(blank=True, help_text='How many titans have been killed in game overall.', max_length=255, null=True, verbose_name='Titans Killed')),
                ('bosses_killed', models.CharField(blank=True, help_text='How many bosses have been killed in game overall.', max_length=255, null=True, verbose_name='Bosses Killed')),
                ('critical_hits', models.CharField(blank=True, help_text='How many critical hits have been scored in game overall.', max_length=255, null=True, verbose_name='Critical Hits')),
                ('chestersons_killed', models.CharField(blank=True, help_text='How many chestersons have been killed in game overall.', max_length=255, null=True, verbose_name='Chestersons Killed')),
                ('prestiges', models.CharField(blank=True, help_text='How many total prestiges have taken place in game overall.', max_length=255, null=True, verbose_name='Prestiges')),
                ('play_time', models.CharField(blank=True, help_text='How much active play time has been accrued in game overall.', max_length=255, null=True, verbose_name='Play Time')),
                ('relics_earned', models.CharField(blank=True, help_text='How many relics have been earned game overall.', max_length=255, null=True, verbose_name='Relics Earned')),
                ('fairies_tapped', models.CharField(blank=True, help_text='How many fairies have been tapped on in game overall.', max_length=255, null=True, verbose_name='Fairies Tapped')),
                ('daily_achievements', models.CharField(blank=True, help_text='How many daily achievements have been completed in game overall.', max_length=255, null=True, verbose_name='Daily Achievements')),
            ],
            options={
                'verbose_name': 'Game Statistics',
                'verbose_name_plural': 'Game Statistics',
            },
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('log_file', models.CharField(max_length=255, verbose_name='Log File')),
            ],
            options={
                'verbose_name': 'Log',
                'verbose_name_plural': 'Logs',
            },
        ),
        migrations.CreateModel(
            name='Prestige',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True, help_text='Timestamp representing when this prestige took place.', verbose_name='Timestamp')),
                ('time', models.DurationField(help_text='The time/duration of the prestige.', verbose_name='Duration')),
                ('stage', models.PositiveIntegerField(blank=True, help_text='The stage that was reached when the prestige took place.', null=True, verbose_name='Stage')),
                ('artifact', models.ForeignKey(help_text='The artifact upgraded following this prestige.', on_delete=django.db.models.deletion.CASCADE, to='titandash.Artifact', verbose_name='Artifact Upgraded')),
            ],
            options={
                'verbose_name': 'Prestige',
                'verbose_name_plural': 'Prestiges',
            },
        ),
        migrations.CreateModel(
            name='PrestigeStatistics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prestiges', models.ManyToManyField(blank=True, help_text='Choose the prestiges that are associated with this prestige statistics instance.', to='titandash.Prestige', verbose_name='Prestiges')),
            ],
            options={
                'verbose_name': 'Prestige Statistics',
                'verbose_name_plural': 'Prestige Statistics',
            },
        ),
        migrations.CreateModel(
            name='Queue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('function', models.CharField(help_text='Name of the function you would like to execute as soon as possible.', max_length=255, verbose_name='Function')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='When was this queue instance generated.', verbose_name='Created')),
            ],
            options={
                'verbose_name': 'Queued Function',
                'verbose_name_plural': 'Queued Functions',
            },
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.CharField(blank=True, help_text='Specify the unique identifier for this session.', max_length=255, null=True, verbose_name='Unique Identifier')),
                ('version', models.CharField(blank=True, help_text='Specify the version of the bot during this session.', max_length=255, null=True, verbose_name='Version')),
                ('start', models.DateTimeField(blank=True, help_text='Start datetime for this session.', null=True, verbose_name='Start Date')),
                ('end', models.DateTimeField(blank=True, help_text='End datetime for this session.', null=True, verbose_name='End Date')),
                ('configuration', models.ForeignKey(blank=True, help_text='Config instance associated with this session.', null=True, on_delete=django.db.models.deletion.CASCADE, to='titandash.Configuration', verbose_name='Configuration')),
                ('log', models.ForeignKey(blank=True, help_text='Specify the file path to the log file associated with this session.', max_length=255, null=True, on_delete=django.db.models.deletion.CASCADE, to='titandash.Log', verbose_name='Log File')),
            ],
            options={
                'verbose_name': 'Session',
                'verbose_name_plural': 'Sessions',
            },
        ),
        migrations.CreateModel(
            name='Statistics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bot_statistics', models.ForeignKey(blank=True, help_text='Bot Statistics associated with this statistics instance.', null=True, on_delete=django.db.models.deletion.CASCADE, to='titandash.BotStatistics', verbose_name='Bot Statistics')),
                ('game_statistics', models.ForeignKey(blank=True, help_text='Game Statistics associated with this statistics instance.', null=True, on_delete=django.db.models.deletion.CASCADE, to='titandash.GameStatistics', verbose_name='Game Statistics')),
                ('sessions', models.ManyToManyField(blank=True, help_text='Sessions associated with this statistics instance.', to='titandash.Session', verbose_name='Sessions')),
            ],
            options={
                'verbose_name': 'Statistics',
                'verbose_name_plural': 'Statistics',
            },
        ),
        migrations.CreateModel(
            name='Tier',
            fields=[
                ('tier', models.CharField(help_text='Specify the tier.', max_length=255, primary_key=True, serialize=False, verbose_name='Tier')),
                ('name', models.CharField(help_text='Specify the readable name associated with this tier.', max_length=255, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Tier',
                'verbose_name_plural': 'Tiers',
            },
        ),
        migrations.AddField(
            model_name='prestige',
            name='session',
            field=models.ForeignKey(help_text='The session associated with this prestige.', on_delete=django.db.models.deletion.CASCADE, to='titandash.Session', verbose_name='Session'),
        ),
        migrations.AddField(
            model_name='configuration',
            name='upgrade_owned_tier',
            field=models.ManyToManyField(blank=True, help_text='Upgrade a specific tier (or tiers) of artifacts only.', related_name='upgrade_tiers', to='titandash.Tier', verbose_name='Upgrade Owned Tier'),
        ),
        migrations.AddField(
            model_name='botinstance',
            name='configuration',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='titandash.Configuration', verbose_name='Current Configuration'),
        ),
        migrations.AddField(
            model_name='botinstance',
            name='log',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='titandash.Log', verbose_name='Current Log'),
        ),
        migrations.AddField(
            model_name='botinstance',
            name='session',
            field=models.ForeignKey(blank=True, help_text='Session associated with the current bot instance.', null=True, on_delete=django.db.models.deletion.CASCADE, to='titandash.Session', verbose_name='Session'),
        ),
        migrations.AddField(
            model_name='artifact',
            name='tier',
            field=models.ForeignKey(help_text='Specify the tier associated with this artifact.', on_delete=django.db.models.deletion.CASCADE, to='titandash.Tier', verbose_name='Tier'),
        ),
    ]
