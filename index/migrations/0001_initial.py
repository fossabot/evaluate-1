# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-09-28 09:23
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True, verbose_name='企业名称')),
                ('create_date', models.DateField(blank=True, null=True, verbose_name='成立时间')),
                ('registered_capital', models.IntegerField(blank=True, null=True, verbose_name='注册资本（万元）')),
                ('paid_in_capital', models.IntegerField(blank=True, null=True, verbose_name='实收资本（万元）')),
                ('major_business', models.CharField(blank=True, max_length=50, null=True, verbose_name='主营产品（或服务）')),
                ('work_force', models.IntegerField(blank=True, null=True, verbose_name='职工总数')),
                ('junior_college_number', models.IntegerField(blank=True, null=True, verbose_name='大专以上学历人数')),
                ('developer_number', models.IntegerField(blank=True, null=True, verbose_name='从事研发人员数')),
                ('is_high_tech_enterprise', models.BooleanField(verbose_name='是否是高新技术企业')),
                ('abouts', models.CharField(blank=True, max_length=500, null=True, verbose_name='企业简介')),
                ('field_1', models.SmallIntegerField(blank=True, null=True, verbose_name='行业领域1')),
                ('field_2', models.CharField(blank=True, max_length=20, null=True, verbose_name='行业领域2')),
                ('x1', models.SmallIntegerField(blank=True, choices=[(1, '集成电路布图'), (2, '其他')], null=True, verbose_name='')),
                ('technical_source', models.SmallIntegerField(blank=True, null=True, verbose_name='技术来源')),
                ('SOAT', models.SmallIntegerField(blank=True, null=True, verbose_name='成果转化来源')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': '一、基本信息',
                'verbose_name': '一、基本信息',
            },
        ),
        migrations.CreateModel(
            name='CoreMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True, verbose_name='姓名')),
                ('gender', models.SmallIntegerField(blank=True, null=True, verbose_name='性别')),
                ('age', models.SmallIntegerField(blank=True, null=True, verbose_name='年龄')),
                ('position', models.CharField(blank=True, max_length=50, null=True, verbose_name='职位')),
                ('is_study_abroad', models.BooleanField(verbose_name='留学经历')),
                ('entrepreneurial_times', models.SmallIntegerField(blank=True, null=True, verbose_name='创业次数')),
                ('experience', models.CharField(blank=True, max_length=500, null=True, verbose_name='谈对自己创业最重要的一个经历')),
                ('companyInfo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='index.CompanyInfo', verbose_name='企业')),
            ],
            options={
                'verbose_name_plural': '核心团队（至少填三人）',
                'verbose_name': '核心团队（至少填三人）',
            },
        ),
        migrations.CreateModel(
            name='DrugApproval',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50, null=True, verbose_name='药品名称')),
                ('new_drug', models.CharField(blank=True, max_length=50, null=True, verbose_name='国家新药')),
                ('c_drug', models.CharField(blank=True, max_length=50, null=True, verbose_name='国家一级中药保护品种')),
                ('num', models.CharField(blank=True, max_length=50, null=True, verbose_name='  药品批准文号 ')),
                ('effective_date', models.DateField(blank=True, null=True, verbose_name='有效日期')),
                ('companyInfo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='index.CompanyInfo', verbose_name='企业')),
            ],
            options={
                'verbose_name_plural': '药品批文',
                'verbose_name': '药品批文',
            },
        ),
        migrations.CreateModel(
            name='EducationExperience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('education', models.CharField(blank=True, max_length=50, null=True, verbose_name='学历')),
                ('university', models.CharField(blank=True, max_length=50, null=True, verbose_name='毕业院校')),
                ('major', models.CharField(blank=True, max_length=50, null=True, verbose_name='专业')),
                ('core_member', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='index.CoreMember', verbose_name='核心团队')),
            ],
            options={
                'verbose_name_plural': '教育经历（可增加）',
                'verbose_name': '教育经历（可增加）',
            },
        ),
        migrations.CreateModel(
            name='EnterpriseAwards',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(blank=True, max_length=10, null=True, verbose_name='获奖级别')),
                ('title', models.CharField(blank=True, max_length=50, null=True, verbose_name='获奖名称')),
                ('date', models.DateField(blank=True, null=True, verbose_name='获奖时间')),
                ('companyInfo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='index.CompanyInfo', verbose_name='企业')),
            ],
            options={
                'verbose_name_plural': '企业获奖情况',
                'verbose_name': '企业获奖情况',
            },
        ),
        migrations.CreateModel(
            name='EvaluationOfEnterprises',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('external_environment', models.SmallIntegerField(blank=True, null=True, verbose_name='外部环境（20）')),
                ('products_and_market', models.SmallIntegerField(blank=True, null=True, verbose_name='企业主营产品及市场开拓（20）')),
                ('technology_R_D', models.SmallIntegerField(blank=True, null=True, verbose_name='企业核心技术及研发实力（20）')),
                ('team', models.SmallIntegerField(blank=True, null=True, verbose_name='企业经营及管理团队（40）')),
            ],
        ),
        migrations.CreateModel(
            name='FinancialSituation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('income', models.IntegerField(blank=True, null=True, verbose_name='累计销售收入')),
                ('profit', models.IntegerField(blank=True, null=True, verbose_name='累计净利润')),
                ('total', models.IntegerField(blank=True, null=True, verbose_name='期末总资产')),
                ('r_d_cost', models.IntegerField(blank=True, null=True, verbose_name='研发费用总额')),
                ('companyInfo', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='index.CompanyInfo', verbose_name='企业')),
            ],
            options={
                'verbose_name_plural': '二、财务状况',
                'verbose_name': '二、财务状况',
            },
        ),
        migrations.CreateModel(
            name='IndependentEvaluationOfEnterprises',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('external_environment', models.SmallIntegerField(blank=True, null=True, verbose_name='企业所处外部环境（权重：2）')),
                ('products_and_market', models.SmallIntegerField(blank=True, null=True, verbose_name='企业主营产品及市场开拓（权重：2）')),
                ('technology_R_D', models.SmallIntegerField(blank=True, null=True, verbose_name='企业核心技术及研发实力（权重：2）')),
                ('team', models.SmallIntegerField(blank=True, null=True, verbose_name='企业经营及管理团队（权重：4）')),
            ],
        ),
        migrations.CreateModel(
            name='MIRC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50, null=True, verbose_name='产品名称')),
                ('num', models.CharField(blank=True, max_length=50, null=True, verbose_name='  医疗器械注册号 ')),
                ('effective_date', models.DateField(blank=True, null=True, verbose_name='有效日期')),
                ('companyInfo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='index.CompanyInfo', verbose_name='企业')),
            ],
            options={
                'verbose_name_plural': '医疗器械注册证',
                'verbose_name': '医疗器械注册证',
            },
        ),
        migrations.CreateModel(
            name='Patent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50, null=True, verbose_name='专利名')),
                ('_type', models.CharField(blank=True, max_length=50, null=True, verbose_name='专利类型')),
                ('num', models.CharField(blank=True, max_length=50, null=True, verbose_name='专利号')),
                ('date', models.DateField(blank=True, null=True, verbose_name='获得时间')),
                ('companyInfo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='index.CompanyInfo', verbose_name='企业')),
            ],
            options={
                'verbose_name_plural': '专利',
                'verbose_name': '专利',
            },
        ),
        migrations.CreateModel(
            name='PersonalAwards',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=10, null=True, verbose_name='获奖人')),
                ('level_title', models.CharField(blank=True, max_length=50, null=True, verbose_name='获奖级别/名称')),
                ('date', models.DateField(blank=True, null=True, verbose_name='获奖时间')),
                ('companyInfo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='index.CompanyInfo', verbose_name='企业')),
            ],
            options={
                'verbose_name_plural': '核心团队个人获奖情况',
                'verbose_name': '核心团队个人获奖情况',
            },
        ),
        migrations.CreateModel(
            name='ProductsAndMarket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(blank=True, max_length=500, null=True, verbose_name='主营产品（或服务）')),
                ('model', models.CharField(blank=True, max_length=500, null=True, verbose_name='商业模式')),
                ('analysis_forecast', models.CharField(blank=True, max_length=500, null=True, verbose_name='市场分析及前景预测')),
                ('companyInfo', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='index.CompanyInfo', verbose_name='企业')),
            ],
            options={
                'verbose_name_plural': '三、产品与市场',
                'verbose_name': '三、产品与市场',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_type', models.CharField(blank=True, max_length=10, null=True, verbose_name='计划类别')),
                ('title', models.CharField(blank=True, max_length=50, null=True, verbose_name='立项名称')),
                ('create_date', models.DateField(blank=True, null=True, verbose_name='立项时间')),
                ('finished_date_and_conclusion', models.CharField(blank=True, max_length=50, null=True, verbose_name='结项时间/结论')),
                ('companyInfo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='index.CompanyInfo', verbose_name='企业')),
            ],
            options={
                'verbose_name_plural': '企业曾经承担或正在承担的科技计划项目',
                'verbose_name': '企业曾经承担或正在承担的科技计划项目',
            },
        ),
        migrations.CreateModel(
            name='ServerRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(blank=True, null=True, verbose_name='融资金额（万元）')),
                ('duration', models.SmallIntegerField(blank=True, null=True, verbose_name='融资时间')),
                ('ratio', models.FloatField(blank=True, null=True, verbose_name='拟出让股权比例')),
                ('interest_rate', models.FloatField(blank=True, null=True, verbose_name='可以接受的最高年利率%')),
                ('plan', models.CharField(blank=True, max_length=500, null=True, verbose_name='资金使用计划')),
                ('small_loan', models.SmallIntegerField(blank=True, null=True, verbose_name='小额贷款')),
                ('share_model', models.SmallIntegerField(blank=True, null=True, verbose_name='股改、挂牌、上市')),
                ('request', models.CharField(blank=True, max_length=20, null=True, verbose_name='金融服务需求')),
                ('companyInfo', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='index.CompanyInfo', verbose_name='企业')),
            ],
            options={
                'verbose_name_plural': '五、服务需求',
                'verbose_name': '五、服务需求',
            },
        ),
        migrations.CreateModel(
            name='Shareholder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True, verbose_name='股东名称')),
                ('share_ratio', models.FloatField(blank=True, null=True, verbose_name='股权比例')),
                ('form_of_contribution', models.SmallIntegerField(blank=True, null=True, verbose_name='出资形式')),
                ('companyInfo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='index.CompanyInfo', verbose_name='企业')),
            ],
            options={
                'verbose_name_plural': '主要股东及股权比例（前五名）',
                'verbose_name': '主要股东及股权比例（前五名）',
            },
        ),
        migrations.CreateModel(
            name='StandardSetting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50, null=True, verbose_name='标准名称')),
                ('level', models.CharField(blank=True, max_length=10, null=True, verbose_name='标准级别')),
                ('num', models.CharField(blank=True, max_length=50, null=True, verbose_name='  标准编号 ')),
                ('status', models.SmallIntegerField(blank=True, null=True, verbose_name='起草单位中的地位')),
                ('companyInfo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='index.CompanyInfo', verbose_name='企业')),
            ],
            options={
                'verbose_name_plural': '标准制定情况',
                'verbose_name': '标准制定情况',
            },
        ),
        migrations.CreateModel(
            name='TechnologyRD',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(blank=True, max_length=500, null=True, verbose_name='核心技术及研发情况')),
                ('companyInfo', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='index.CompanyInfo', verbose_name='企业')),
            ],
            options={
                'verbose_name_plural': '四、技术与研发',
                'verbose_name': '四、技术与研发',
            },
        ),
        migrations.CreateModel(
            name='WorkExperience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(blank=True, max_length=50, null=True, verbose_name='工作单位')),
                ('position', models.CharField(blank=True, max_length=50, null=True, verbose_name='职位')),
                ('date_s', models.DateField(blank=True, null=True, verbose_name='工作时间_开始')),
                ('date_e', models.DateField(blank=True, null=True, verbose_name='工作时间_结束')),
                ('core_member', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='index.CoreMember', verbose_name='核心团队')),
            ],
            options={
                'verbose_name_plural': '工作经历（可增加）',
                'verbose_name': '工作经历（可增加）',
            },
        ),
    ]
