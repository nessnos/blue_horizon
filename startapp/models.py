import uuid
from django.db import models
from django.utils.timezone import now

# WATER DATA RELATED

class Country(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    code = models.CharField(max_length=2)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class WaterBodyCategory(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    label = models.CharField(max_length=255)
    notation = models.CharField(max_length=50)

    def __str__(self):
        return self.label

class ObservedProperty(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    label = models.CharField(max_length=255)
    notation = models.CharField(max_length=50)

    def __str__(self):
        return self.label

class Matrix(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    label = models.CharField(max_length=255)
    code = models.CharField(max_length=50)

    def __str__(self):
        return self.label

class UnitOfMeasure(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    label = models.CharField(max_length=255)
    notation = models.CharField(max_length=50)

    def __str__(self):
        return self.label

class WaterData(models.Model):
    uid = models.CharField(max_length=255, unique=True, null=True, blank=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True, blank=True)
    monitoring_site_identifier = models.CharField(max_length=100, null=True, blank=True)
    monitoring_site_identifier_scheme = models.CharField(
        max_length=50,
        choices=[
            ('eionetMonitoringSiteCode', 'EIONET identifier'),
            ('euMonitoringSiteCode', 'WFD identifier')
        ],
        null=True,
        blank=True
    )
    parameter_water_body_category = models.ForeignKey(WaterBodyCategory, on_delete=models.CASCADE, null=True, blank=True)
    observed_property_determinand_code = models.ForeignKey(ObservedProperty, on_delete=models.CASCADE, null=True, blank=True)
    procedure_analysed_matrix = models.ForeignKey(Matrix, on_delete=models.CASCADE, null=True, blank=True)
    result_uom = models.ForeignKey(UnitOfMeasure, on_delete=models.CASCADE, null=True, blank=True)
    phenomenon_time_reference_year = models.IntegerField(null=True, blank=True)
    parameter_sampling_period = models.CharField(max_length=100, null=True, blank=True)
    procedure_loq_value = models.FloatField(null=True, blank=True)
    result_number_of_samples = models.IntegerField(null=True, blank=True)
    result_quality_number_of_samples_below_loq = models.IntegerField(null=True, blank=True)
    result_quality_minimum_below_loq = models.BooleanField(null=True, blank=True)
    result_minimum_value = models.FloatField(null=True, blank=True)
    result_quality_mean_below_loq = models.BooleanField(null=True, blank=True)
    result_mean_value = models.FloatField(null=True, blank=True)
    result_quality_maximum_below_loq = models.BooleanField(null=True, blank=True)
    result_maximum_value = models.FloatField(null=True, blank=True)
    result_quality_median_below_loq = models.BooleanField(null=True, blank=True)
    result_median_value = models.FloatField(null=True, blank=True)
    result_standard_deviation_value = models.FloatField(null=True, blank=True)
    procedure_analytical_method = models.CharField(max_length=255, null=True, blank=True)
    parameter_sample_depth = models.FloatField(null=True, blank=True)
    result_observation_status = models.CharField(
        max_length=1,
        choices=[
            ('A', 'Record is confirmed as correct'),
            ('L', 'Missing observed value, the data were not collected'),
            ('M', 'Missing observed value, the data can not exist'),
            ('N', 'Missing observed value, observed value is not relevant or not significant'),
            ('O', 'Missing observed value, no further information is available'),
            ('W', 'Missing observed value, data are included in another source category'),
            ('X', 'Reported value includes data from another source category'),
            ('Y', 'The source category does not exactly match the standard definition'),
            ('Z', 'Record reported in the past should be deleted'),
        ],
        null=True,
        blank=True
    )
    remarks = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.monitoring_site_identifier} - {self.phenomenon_time_reference_year}"