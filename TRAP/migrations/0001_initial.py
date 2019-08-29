# Generated by Django 2.1.4 on 2019-05-02 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tsetse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caseno2', models.CharField(blank=True, max_length=50, null=True)),
                ('vpn', models.CharField(blank=True, max_length=50, null=True)),
                ('volume', models.CharField(blank=True, max_length=50, null=True)),
                ('page', models.CharField(blank=True, max_length=50, null=True)),
                ('number_on_page', models.CharField(blank=True, max_length=50, null=True)),
                ('capture_day_of_month', models.CharField(blank=True, max_length=50, null=True)),
                ('capture_month_year', models.CharField(blank=True, max_length=50, null=True)),
                ('capture_year', models.CharField(blank=True, max_length=50, null=True)),
                ('experimental_month', models.CharField(blank=True, max_length=50, null=True)),
                ('capture_days_since_01011960', models.CharField(blank=True, max_length=50, null=True)),
                ('disector_code', models.CharField(blank=True, max_length=50, null=True)),
                ('microscope', models.CharField(blank=True, max_length=50, null=True)),
                ('capture_sites', models.CharField(blank=True, max_length=50, null=True)),
                ('capture_method_code', models.CharField(blank=True, max_length=50, null=True)),
                ('capture_start_time', models.CharField(blank=True, max_length=50, null=True)),
                ('capture_end_time', models.CharField(blank=True, max_length=50, null=True)),
                ('dissection_day', models.CharField(blank=True, max_length=50, null=True)),
                ('dissection_month', models.CharField(blank=True, max_length=50, null=True)),
                ('time_of_disection_am_or_pm', models.CharField(blank=True, max_length=50, null=True)),
                ('genus', models.CharField(blank=True, max_length=50, null=True)),
                ('sex', models.CharField(blank=True, max_length=50, null=True)),
                ('largest_ooctye_length_mm_x100', models.CharField(blank=True, max_length=50, null=True)),
                ('largest_ooctye_diameter_mm_x100', models.CharField(blank=True, max_length=50, null=True)),
                ('second_largest_ooctye_length_mm_x100', models.CharField(blank=True, max_length=50, null=True)),
                ('ovarian_category', models.CharField(blank=True, max_length=50, null=True)),
                ('uterine_content', models.CharField(blank=True, max_length=50, null=True)),
                ('uterine_length_ulm_mm_x100', models.CharField(blank=True, max_length=50, null=True)),
                ('uterine_length_udm_mm_x100', models.CharField(blank=True, max_length=50, null=True)),
                ('left_spermatophore_content_0_to_10', models.CharField(blank=True, max_length=50, null=True)),
                ('right_spermatophore_content_0_to_10', models.CharField(blank=True, max_length=50, null=True)),
                ('hunger_stage', models.CharField(blank=True, max_length=50, null=True)),
                ('wing_length_scale_wl', models.CharField(blank=True, max_length=50, null=True)),
                ('wing_length_mm_x100_wlm', models.CharField(blank=True, max_length=50, null=True)),
                ('facwlmnew', models.CharField(blank=True, max_length=50, null=True)),
                ('wing_length_mm_x100_wlm2', models.CharField(blank=True, max_length=50, null=True)),
                ('wing_fray_1_to_6', models.CharField(blank=True, max_length=50, null=True)),
                ('determinant_for_pregnancy_stage', models.CharField(blank=True, max_length=50, null=True)),
                ('percent_pregnancy_completed', models.CharField(blank=True, max_length=50, null=True)),
                ('inter_larval_period', models.CharField(blank=True, max_length=50, null=True)),
                ('estimated_day_of_pregnancy', models.CharField(blank=True, max_length=50, null=True)),
                ('estimated_age_days', models.CharField(blank=True, max_length=50, null=True)),
                ('estimated_birth_day_julian', models.CharField(blank=True, max_length=50, null=True)),
                ('cut_off_al_length_for_deciding_if_fly_aborted', models.CharField(blank=True, max_length=50, null=True)),
                ('error_code_1', models.CharField(blank=True, max_length=50, null=True)),
                ('error_code_2', models.CharField(blank=True, max_length=50, null=True)),
                ('r_is_1_if_disector_noted_a_problem_r_is_0_otherwise', models.CharField(blank=True, max_length=50, null=True)),
                ('tube_number', models.CharField(blank=True, max_length=50, null=True)),
                ('alphanumeric_label_for_tube', models.CharField(blank=True, max_length=50, null=True)),
                ('pteridine', models.CharField(blank=True, max_length=50, null=True)),
                ('mother_thorasic_residue_dry_weight', models.CharField(blank=True, max_length=50, null=True)),
                ('mark', models.CharField(blank=True, max_length=50, null=True)),
                ('uterine_volume', models.CharField(blank=True, max_length=50, null=True)),
                ('dwu', models.CharField(blank=True, max_length=50, null=True)),
                ('rdwu', models.CharField(blank=True, max_length=50, null=True)),
                ('fatu', models.CharField(blank=True, max_length=50, null=True)),
                ('fwu', models.CharField(blank=True, max_length=50, null=True)),
                ('tr', models.CharField(blank=True, max_length=50, null=True)),
                ('mothers_dry_weight', models.CharField(blank=True, max_length=50, null=True)),
                ('mothers_resid_dry_weight', models.CharField(blank=True, max_length=50, null=True)),
                ('mothers_fat_weight', models.CharField(blank=True, max_length=50, null=True)),
                ('mothers_abdominal_resid_dry_weight', models.CharField(blank=True, max_length=50, null=True)),
                ('mothers_haematin', models.CharField(blank=True, max_length=50, null=True)),
                ('mother_plus_pupa_dry_weight', models.CharField(blank=True, max_length=50, null=True)),
                ('mother_plus_pupa_resid_dry_weight', models.CharField(blank=True, max_length=50, null=True)),
                ('mother_plus_pupa_fat_weight', models.CharField(blank=True, max_length=50, null=True)),
                ('uterine_dry_weight_est_from_volume', models.CharField(blank=True, max_length=50, null=True)),
                ('uterine_resid_dry_weight_est_from_volume', models.CharField(blank=True, max_length=50, null=True)),
                ('uterine_fat_weight_est_from_volume', models.CharField(blank=True, max_length=50, null=True)),
                ('uterine_fresh_weight_est_from_volume', models.CharField(blank=True, max_length=50, null=True)),
                ('puparial_length_mm_x100_lpm', models.CharField(blank=True, max_length=50, null=True)),
                ('puparial_length_mm_x100_dpm', models.CharField(blank=True, max_length=50, null=True)),
                ('uterine_volume_volp', models.CharField(blank=True, max_length=50, null=True)),
                ('puparial_dry_weight_dwp', models.CharField(blank=True, max_length=50, null=True)),
                ('puparial_resid_dry_weight_rdwp', models.CharField(blank=True, max_length=50, null=True)),
                ('puparial_fat_weight_fatp', models.CharField(blank=True, max_length=50, null=True)),
                ('puparial_fat_weight_corrected_for_process_delay_fatp0', models.CharField(blank=True, max_length=50, null=True)),
                ('puparial_fresh_weight_fwp', models.CharField(blank=True, max_length=50, null=True)),
                ('puparial_dry_weight_est_from_volume_edwp', models.CharField(blank=True, max_length=50, null=True)),
                ('puparial_resid_dry_weight_est_from_volume_erdwp', models.CharField(blank=True, max_length=50, null=True)),
                ('puparial_fat_weight_est_from_volume_efatp', models.CharField(blank=True, max_length=50, null=True)),
                ('puparial_fresh_weight_est_from_volume_efwp', models.CharField(blank=True, max_length=50, null=True)),
                ('fd', models.CharField(blank=True, max_length=50, null=True)),
                ('fjd', models.CharField(blank=True, max_length=50, null=True)),
                ('idd', models.CharField(blank=True, max_length=50, null=True)),
                ('im', models.CharField(blank=True, max_length=50, null=True)),
                ('ijd', models.CharField(blank=True, max_length=50, null=True)),
                ('ep', models.CharField(blank=True, max_length=50, null=True)),
                ('presence_of_adult_mx', models.CharField(blank=True, max_length=50, null=True)),
                ('presence_of_pupa_px', models.CharField(blank=True, max_length=50, null=True)),
                ('mother_plus_pupa_totfat0', models.CharField(blank=True, max_length=50, null=True)),
                ('estimated_mother_plus_pupa_dry_weight_etotdw', models.CharField(blank=True, max_length=50, null=True)),
                ('estimated_mother_plus_pupa_resid_dry_weight_etotrdw', models.CharField(blank=True, max_length=50, null=True)),
                ('estimated_mother_plus_pupa_fat_weight_etotfat', models.CharField(blank=True, max_length=50, null=True)),
                ('bt', models.CharField(blank=True, max_length=50, null=True)),
                ('capture_month_of_experiment_cms', models.CharField(blank=True, max_length=50, null=True)),
                ('birth_month_different_definition_from_bm_bm2', models.CharField(blank=True, max_length=50, null=True)),
                ('birth_month_bm', models.CharField(blank=True, max_length=50, null=True)),
                ('birth_year_by', models.CharField(blank=True, max_length=50, null=True)),
                ('birth_month_for_female_born_in_month_cms_bms', models.CharField(blank=True, max_length=50, null=True)),
                ('pooled_capture_sites_sitep', models.CharField(blank=True, max_length=50, null=True)),
                ('pooled_capture_methods_mdp', models.CharField(blank=True, max_length=50, null=True)),
                ('estimated_age_negative_changed_to_0_age0', models.CharField(blank=True, max_length=50, null=True)),
                ('year_of_dissection_dy', models.CharField(blank=True, max_length=50, null=True)),
                ('days_delay_in_dissection_del', models.CharField(blank=True, max_length=50, null=True)),
                ('sperm_left_plus_right_slr', models.CharField(blank=True, max_length=50, null=True)),
                ('total_sperm_pooled_units_4_slrp', models.CharField(blank=True, max_length=50, null=True)),
                ('total_sperm_pooled_0_1to8_9to16_17to20', models.CharField(blank=True, max_length=50, null=True)),
                ('day_of_the_year_dofy', models.CharField(blank=True, max_length=50, null=True)),
                ('day_of_the_year_9_day_pool_dofy9', models.CharField(blank=True, max_length=50, null=True)),
                ('pyriproxyfen_traps_or_targets_used_pyri', models.CharField(blank=True, max_length=50, null=True)),
                ('methods_pooled_major_mdpall', models.CharField(blank=True, max_length=50, null=True)),
                ('log_10_of_haematin_in_nanograms_log10hm', models.CharField(blank=True, max_length=50, null=True)),
                ('ovcat_where_ppp_files_with_u_0_put_into_next_ovcat_cnu', models.CharField(blank=True, max_length=50, null=True)),
                ('full_term_ppp_pregnant_etc_ftpp', models.CharField(blank=True, max_length=50, null=True)),
                ('full_term_ppp_pregnant_etc_ftppp', models.CharField(blank=True, max_length=50, null=True)),
                ('full_term_ppp_pregnant_etc_ppall', models.CharField(blank=True, max_length=50, null=True)),
                ('pprpl', models.CharField(blank=True, max_length=50, null=True)),
                ('pprpl2', models.CharField(blank=True, max_length=50, null=True)),
                ('runmin9', models.CharField(blank=True, max_length=50, null=True)),
                ('mothers_dry_weight_mg_dwmg', models.CharField(blank=True, max_length=50, null=True)),
                ('residual_dry_weight_mg_rdwmg', models.CharField(blank=True, max_length=50, null=True)),
                ('mothers_fat_weight_mg_fatmg', models.CharField(blank=True, max_length=50, null=True)),
                ('mothers_thoracic_resid_dry_weight_mg_trdwmg', models.CharField(blank=True, max_length=50, null=True)),
                ('mothers_abdominal_resid_dry_weight_mg_ardwmg', models.CharField(blank=True, max_length=50, null=True)),
                ('wing_length_wlmm', models.CharField(blank=True, max_length=50, null=True)),
                ('puparial_fresh_weight_mg_fwpmg', models.CharField(blank=True, max_length=50, null=True)),
                ('puparial_dry_weight_mg_dwpmg', models.CharField(blank=True, max_length=50, null=True)),
                ('puparial_fat_weight_mg_fatpmg', models.CharField(blank=True, max_length=50, null=True)),
                ('puparial_resid_dry_weight_mg_rdwpmg', models.CharField(blank=True, max_length=50, null=True)),
                ('mother_plus_pupa_dry_weight_mg_totdwmg', models.CharField(blank=True, max_length=50, null=True)),
                ('mother_plus_pupa_resid_dry_weight_mg_totrdwmg', models.CharField(blank=True, max_length=50, null=True)),
                ('mother_plus_pupa_fat_weight_mg_totfatmg', models.CharField(blank=True, max_length=50, null=True)),
                ('ctemp', models.CharField(blank=True, max_length=50, null=True)),
                ('cf56', models.CharField(blank=True, max_length=50, null=True)),
                ('cf6', models.CharField(blank=True, max_length=50, null=True)),
                ('testtem', models.DecimalField(blank=True, decimal_places=25, max_digits=25, null=True)),
                ('date_sample_started_datest', models.CharField(blank=True, max_length=50, null=True)),
                ('capture_month_of_year_cctem', models.CharField(blank=True, max_length=50, null=True)),
                ('newpage_numbering_pgall', models.CharField(blank=True, max_length=50, null=True)),
                ('unique_number_for_each_fly_in_file_idfly', models.CharField(blank=True, max_length=50, null=True)),
                ('date_sample_collected_datecap', models.DateField(blank=True, null=True)),
                ('datedis', models.DateField(blank=True, null=True)),
                ('ndvi', models.DecimalField(blank=True, decimal_places=25, max_digits=25, null=True)),
                ('ndvi90', models.DecimalField(blank=True, decimal_places=25, max_digits=25, null=True)),
                ('ndvi91', models.DecimalField(blank=True, decimal_places=25, max_digits=25, null=True)),
                ('ndvi92', models.DecimalField(blank=True, decimal_places=25, max_digits=25, null=True)),
                ('ndvi93', models.DecimalField(blank=True, decimal_places=25, max_digits=25, null=True)),
                ('ndvi94', models.DecimalField(blank=True, decimal_places=25, max_digits=25, null=True)),
                ('ndvi300', models.DecimalField(blank=True, decimal_places=25, max_digits=25, null=True)),
                ('ndvi301', models.DecimalField(blank=True, decimal_places=25, max_digits=25, null=True)),
                ('ndvi302', models.DecimalField(blank=True, decimal_places=25, max_digits=25, null=True)),
                ('ndvi303', models.DecimalField(blank=True, decimal_places=25, max_digits=25, null=True)),
                ('tmax', models.DecimalField(blank=True, decimal_places=3, max_digits=6, null=True)),
                ('tmax90', models.DecimalField(blank=True, decimal_places=3, max_digits=6, null=True)),
                ('tmax91', models.DecimalField(blank=True, decimal_places=3, max_digits=6, null=True)),
                ('tmax92', models.DecimalField(blank=True, decimal_places=3, max_digits=6, null=True)),
                ('tmax93', models.DecimalField(blank=True, decimal_places=3, max_digits=6, null=True)),
                ('tmax94', models.DecimalField(blank=True, decimal_places=3, max_digits=6, null=True)),
                ('tmin', models.DecimalField(blank=True, decimal_places=3, max_digits=6, null=True)),
                ('tmin90', models.DecimalField(blank=True, decimal_places=3, max_digits=6, null=True)),
                ('tmin91', models.DecimalField(blank=True, decimal_places=3, max_digits=6, null=True)),
                ('tmin92', models.DecimalField(blank=True, decimal_places=3, max_digits=6, null=True)),
                ('tmin93', models.DecimalField(blank=True, decimal_places=3, max_digits=6, null=True)),
                ('tmin94', models.DecimalField(blank=True, decimal_places=3, max_digits=6, null=True)),
                ('tbar', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('tbar90', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('tbar91', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('tbar92', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('tbar93', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('tbar94', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('rain', models.DecimalField(blank=True, decimal_places=3, max_digits=6, null=True)),
                ('cf456', models.IntegerField(blank=True, null=True)),
                ('dur', models.IntegerField(blank=True, null=True)),
                ('tbars', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('tbars90', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('tbars91', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('tbars92', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('tbars93', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('tbars94', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('rhbars', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('rhbars90', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('rhbars91', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('rhbars92', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('rhbars93', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('rhbars94', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('sdhgbars', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('sdhgbars90', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('sdhgbars91', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('sdhgbars92', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('sdhgbars93', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('sdhgbars94', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('hmmug', models.CharField(blank=True, max_length=50, null=True)),
                ('day_of_experiment_dj', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('dissected_for_infection_at_all_0_or_1_nf', models.IntegerField(blank=True, null=True)),
                ('infection_code_for_labrum_la', models.CharField(blank=True, max_length=50, null=True)),
                ('infection_code_for_hypopharynx_hp', models.CharField(blank=True, max_length=50, null=True)),
                ('infection_code_for_salivary_glands_sg', models.CharField(blank=True, max_length=50, null=True)),
                ('infection_code_for_midgut_mg', models.CharField(blank=True, max_length=50, null=True)),
                ('infection_0_or_1_for_labrum_la2', models.IntegerField(blank=True, null=True)),
                ('infection_0_or_1_for_hypopharynx_hp2', models.IntegerField(blank=True, null=True)),
                ('infection_0_or_1_for_any_mouthpart_tryps_mpart', models.IntegerField(blank=True, null=True)),
                ('infection_0_or_1_for_midgut_mg2', models.IntegerField(blank=True, null=True)),
                ('infection_0_or_1_for_vivax_vivax', models.IntegerField(blank=True, null=True)),
                ('infection_0_or_1_for_salivary_glands_sg2', models.IntegerField(blank=True, null=True)),
                ('infection_0_or_1_for_congo_congo', models.IntegerField(blank=True, null=True)),
                ('infection_0_or_1_for_brucei_brucei', models.IntegerField(blank=True, null=True)),
                ('infection_0_or_1_for_mixed_congo_or_brucei_brucong', models.IntegerField(blank=True, null=True)),
                ('measured_percent_fat_in_pupa_fatppcg', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('efatp2', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('etotfat2', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('eggooc', models.IntegerField(blank=True, null=True)),
                ('abort', models.IntegerField(blank=True, null=True)),
                ('tbar91p', models.IntegerField(blank=True, null=True)),
                ('cm2', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('umt', models.IntegerField(blank=True, null=True)),
                ('tbar91sq', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('fatppcprdw', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('fatpcrdw', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('propfat', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('fatproptrdw', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('fatranspc', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('etotfat2sq', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('windv', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True, verbose_name='Wind velocity m/s')),
                ('windv9', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True, verbose_name='Wind vel average over prior 9 days')),
                ('soiltem', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True, verbose_name='Soil temp degrees C')),
                ('soiltem9', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True, verbose_name='Soil temp average over prior 9days')),
                ('radiation', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True, verbose_name='Black body radiation degrees C')),
                ('rad9', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True, verbose_name='Black body radiation average over prior 9 days')),
                ('bday9', models.IntegerField(blank=True, null=True, verbose_name='Birthday in 9 day groups')),
                ('bdaydate', models.DateField(blank=True, null=True, verbose_name='Birthday formatted as date')),
                ('bmon', models.IntegerField(blank=True, null=True, verbose_name='Month of the year fly emerged as teneral')),
                ('wlmpl', models.IntegerField(blank=True, null=True)),
                ('nfmmg', models.IntegerField(blank=True, null=True, verbose_name='Mouthparts & midgut BOTH dissected for infection')),
                ('fsq', models.IntegerField(blank=True, null=True)),
                ('cnusq2', models.IntegerField(blank=True, null=True, verbose_name='cnu squared NEW verison Dec 2017')),
                ('tbarm0', models.CharField(blank=True, max_length=50, null=True)),
                ('tbarm1', models.CharField(blank=True, max_length=50, null=True)),
                ('tbarm2', models.CharField(blank=True, max_length=50, null=True)),
                ('rhm0', models.CharField(blank=True, max_length=50, null=True)),
                ('rhm1', models.CharField(blank=True, max_length=50, null=True)),
                ('rhm2', models.CharField(blank=True, max_length=50, null=True)),
                ('sdefm0', models.CharField(blank=True, max_length=50, null=True)),
                ('sdefm1', models.CharField(blank=True, max_length=50, null=True)),
                ('sdefm2', models.CharField(blank=True, max_length=50, null=True)),
                ('mdpall2', models.IntegerField(blank=True, null=True, verbose_name='Methods max pooling')),
                ('ptpl', models.IntegerField(blank=True, null=True)),
                ('wlmnew', models.CharField(blank=True, max_length=50, null=True)),
                ('facwlmold', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
            ],
            options={
                'verbose_name_plural': 'Tsetse data',
            },
        ),
    ]