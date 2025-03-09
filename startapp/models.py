import uuid
from django.db import models
from django.utils.timezone import now

# WATER DATA RELATED
class Country(models.Model):
    isoalpha2 = models.CharField(max_length=2, primary_key=True)
    country = models.CharField(max_length=100)

    class Meta:
        db_table = 'countries'
        managed = False 

class WaterData(models.Model):
    countryCode = models.CharField(max_length=255, null=False, blank=False)
    monitoringSiteIdentifier = models.CharField(max_length=255, null=True, blank=True)
    monitoringSiteIdentifierScheme = models.CharField(max_length=255, null=True, blank=True)
    parameterWaterBodyCategory = models.CharField(max_length=255, null=True, blank=True)
    observedPropertyDeterminandCode = models.CharField(max_length=255, null=True, blank=True)
    observedPropertyDeterminandLabel = models.CharField(max_length=255, null=True, blank=True)
    procedureAnalysedMatrix = models.CharField(max_length=255, null=True, blank=True)
    resultUom = models.CharField(max_length=255, null=True, blank=True)
    phenomenonTimeReferenceYear = models.IntegerField(null=True, blank=True)
    parameterSamplingPeriod = models.CharField(max_length=100, null=True, blank=True)
    procedureLOQValue = models.FloatField(null=True, blank=True)
    resultNumberOfSamples = models.FloatField(null=True, blank=True)
    resultQualityNumberOfSamplesBelowLOQ = models.IntegerField(null=True, blank=True)
    resultQualityMinimumBelowLOQ = models.IntegerField(null=True, blank=True)
    resultMinimumValue = models.FloatField(null=True, blank=True)
    resultQualityMeanBelowLOQ = models.IntegerField(null=True, blank=True)
    resultMeanValue = models.FloatField(null=True, blank=True)
    resultQualityMaximumBelowLOQ = models.IntegerField(null=True, blank=True)
    resultMaximumValue = models.FloatField(null=True, blank=True)
    resultQualityMedianBelowLOQ = models.IntegerField(null=True, blank=True)
    resultMedianValue = models.FloatField(null=True, blank=True)
    resultStandardDeviationValue = models.FloatField(null=True, blank=True)
    procedureAnalyticalMethod = models.CharField(max_length=255, null=True, blank=True)
    parameterSampleDepth = models.FloatField(null=True, blank=True)
    resultObservationStatus = models.CharField(max_length=1, null=True,blank=True)
    remarks = models.TextField(null=True, blank=True)
    UID = models.CharField(unique=True, primary_key=True)


# WEBAPP PIPELINE RELATED
class PipelineRun(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('STARTED', 'Started'),
        ('SUCCESS', 'Success'),
        ('FAILURE', 'Failure'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    task_id = models.CharField(max_length=255, unique=True, help_text="Celery task ID")
    model_name = models.CharField(max_length=100, blank=False, null=False, default='Unknown')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING')
    started_at = models.DateTimeField(null=True, blank=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    results = models.JSONField(help_text="Stores the results of the pipeline", default='')

    def mark_started(self):
        """Mark the pipeline as started"""
        self.status = 'STARTED'
        self.started_at = now()
        self.save()

    def mark_completed(self, success=True):
        """Mark the pipeline as completed"""
        self.status = 'SUCCESS' if success else 'FAILURE'
        self.completed_at = now()
        self.save()

    def __str__(self):
        return f"Pipeline {self.task_id} - {self.status}"
    
    
# MATERIALIZED VIEWS
class CleanedData(models.Model):
    countryCode = models.CharField(max_length=255, null=False, blank=False)
    monitoringSiteIdentifier = models.CharField(max_length=255, null=True, blank=True)
    monitoringSiteIdentifierScheme = models.CharField(max_length=255, null=True, blank=True)
    parameterWaterBodyCategory = models.CharField(max_length=255, null=True, blank=True)
    observedPropertyDeterminandCode = models.CharField(max_length=255, null=True, blank=True)
    observedPropertyDeterminandLabel = models.CharField(max_length=255, null=True, blank=True)
    procedureAnalysedMatrix = models.CharField(max_length=255, null=True, blank=True)
    resultUom = models.CharField(max_length=255, null=True, blank=True)
    phenomenonTimeReferenceYear = models.IntegerField(null=True, blank=True)
    parameterSamplingPeriod = models.CharField(max_length=100, null=True, blank=True)
    procedureLOQValue = models.FloatField(null=True, blank=True)
    resultNumberOfSamples = models.FloatField(null=True, blank=True)
    resultQualityNumberOfSamplesBelowLOQ = models.IntegerField(null=True, blank=True)
    resultQualityMinimumBelowLOQ = models.IntegerField(null=True, blank=True)
    resultMinimumValue = models.FloatField(null=True, blank=True)
    resultQualityMeanBelowLOQ = models.IntegerField(null=True, blank=True)
    resultMeanValue = models.FloatField(null=True, blank=True)
    resultQualityMaximumBelowLOQ = models.IntegerField(null=True, blank=True)
    resultMaximumValue = models.FloatField(null=True, blank=True)
    resultQualityMedianBelowLOQ = models.IntegerField(null=True, blank=True)
    resultMedianValue = models.FloatField(null=True, blank=True)
    resultStandardDeviationValue = models.FloatField(null=True, blank=True)
    procedureAnalyticalMethod = models.CharField(max_length=255, null=True, blank=True)
    parameterSampleDepth = models.FloatField(null=True, blank=True)
    resultObservationStatus = models.CharField(max_length=1, null=True,blank=True)
    remarks = models.TextField(null=True, blank=True)
    UID = models.CharField(unique=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'cleaned_data'  

class Filters(models.Model):
    id = models.AutoField(primary_key=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    iso_alpha2 = models.CharField(max_length=3, null=True, blank=True)
    observed_property_determinand = models.CharField(max_length=255, null=True, blank=True)
    reference_year = models.IntegerField(null=True, blank=True)
    matrix = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        managed = False
        db_table = "filters"

class CountryStats(models.Model):
    id = models.AutoField(primary_key=True)
    country = models.TextField(null=True, blank=True)
    iso_alpha2 = models.CharField(max_length=3, null=True, blank=True)
    total_monitoring_sites = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    decades_covered = models.TextField(null=True, blank=True)
    water_body_category = models.TextField(null=True, blank=True)
    matrix = models.TextField(null=True, blank=True)
    
    count_of_chemicals_monitored = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    number_of_collected_samples = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    proportion_of_confirmed_samples = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    
    most_monitored_determinand = models.TextField(null=True, blank=True)
    total_samples = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    
    mean_concentration = models.TextField(null=True, blank=True)
    standard_deviation = models.TextField(null=True, blank=True)
    minimum_recorded_value = models.TextField(null=True, blank=True)
    maximum_recorded_value = models.TextField(null=True, blank=True)
    
    unit_of_measure = models.TextField(null=True, blank=True)

    class Meta:
        managed = False
        db_table = "country_stats"


class DashboardData(models.Model):
    id = models.AutoField(primary_key=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    observed_property_determinand = models.CharField(max_length=255, null=True, blank=True)
    reference_year = models.IntegerField(null=True, blank=True)
    matrix = models.CharField(max_length=255, null=True, blank=True)
    
    number_of_collected_samples = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    nominator_of_confirmed_samples = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    denominator_of_confirmed_samples = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    
    result_mean_value = models.DecimalField(max_digits=20, decimal_places=6, null=True, blank=True)
    stddev = models.DecimalField(max_digits=20, decimal_places=6, null=True, blank=True)
    result_minimum_value = models.DecimalField(max_digits=20, decimal_places=6, null=True, blank=True)
    result_maximum_value = models.DecimalField(max_digits=20, decimal_places=6, null=True, blank=True)
    
    uom = models.TextField(null=True, blank=True)
    
    under_loq = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    above_loq = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    
    list_of_water_body_category = models.TextField(null=True, blank=True)
    list_of_monitoring_sites = models.TextField(null=True, blank=True)


    class Meta:
        managed = False 
        db_table = "dashboard_data"


class ChatData(models.Model):
    id = models.AutoField(primary_key=True)
    country = models.TextField(null=True, blank=True)
    isoalpha2 = models.CharField(max_length=2)
    phenomenon_time_reference_year = models.IntegerField(null=True, blank=True)
    observed_property_determinand = models.TextField(null=True, blank=True)
    total_monitoring_sites = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    water_body_category = models.TextField(null=True, blank=True)
    matrix = models.TextField(null=True, blank=True)
    proportion_of_confirmed_samples = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    loq_value = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    number_of_collected_samples = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    number_samples_below_loq = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    mean_concentration = models.TextField(null=True, blank=True)
    number_samples_mean_below_loq = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    median_concentration = models.TextField(null=True, blank=True)
    number_samples_median_below_loq = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    standard_deviation = models.TextField(null=True, blank=True)
    minimum_recorded_value = models.TextField(null=True, blank=True)
    number_samples_min_below_loq = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    maximum_recorded_value = models.TextField(null=True, blank=True)
    number_samples_max_below_loq = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    unit_of_measure = models.TextField(null=True, blank=True)

    class Meta:
        managed = False
        db_table = "chat_data"