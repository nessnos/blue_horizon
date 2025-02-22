import sqlite3

def connect_to_db(db_path="Waterbase_v2023_1_WISE6.sqlite"):
    """Connect to the SQLite database and return the connection and cursor."""
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        return conn, cursor
    except Exception as e:
        print("Error connecting to the database:", e)
        return None, None

def get_total_chemicals_monitored(cursor, country_code=None):
    """Return the total number of distinct chemicals monitored, optionally filtered by country."""
    try:
        query = """
        SELECT COUNT(DISTINCT observedPropertyDeterminandLabel) FROM T_WISE6_AggregatedData 
        WHERE metadata_observationStatus != 'V'
        AND 1=1"""
        params = []
        if country_code is not None:
            query += " AND countryCode = ?"
            params.append(country_code)
        cursor.execute(query, tuple(params))
        result = cursor.fetchone()
        return result[0] if result else 0
    except Exception as e:
        print("Error in get_total_chemicals_monitored:", e)
        return None


def get_total_monitoring_sites(cursor, country_code=None):
    """Return the total number of distinct monitoring sites, optionally filtered by country."""
    try:
        query = """
        SELECT COUNT(DISTINCT monitoringSiteIdentifier) FROM T_WISE6_AggregatedData 
        WHERE metadata_observationStatus != 'V'
        AND 1=1"""
        params = []
        if country_code is not None:
            query += " AND countryCode = ?"
            params.append(country_code)
        cursor.execute(query, tuple(params))
        result = cursor.fetchone()
        return result[0] if result else 0
    except Exception as e:
        print("Error in get_total_monitoring_sites:", e)
        return None    

def get_total_monitoring_sites_from_spatial_table(cursor, country_code=None):
    """Return the total number of distinct monitoring sites from spatial table, optionally filtered by country."""
    try:
        query = """
        SELECT COUNT(DISTINCT monitoringSiteIdentifier) FROM S_WISE6_SpatialObject_DerivedData
        WHERE 
        1=1"""
        params = []
        if country_code is not None:
            query += " AND countryCode = ?"
            params.append(country_code)
        cursor.execute(query, tuple(params))
        result = cursor.fetchone()
        return result[0] if result else 0
    except Exception as e:
        print("Error in get_total_monitoring_sites_from_spatial_table:", e)
        return None

def get_total_distinct_water_bodies(cursor, country_code=None):
    """Return the total number of distinct water bodies, optionally filtered by country."""
    try:
        query = """
        SELECT COUNT(DISTINCT waterBodyIdentifier) FROM T_WISE6_AggregatedDataByWaterBody 
        WHERE metadata_observationStatus != 'V'
        AND 1=1"""
        params = []
        if country_code is not None:
            query += " AND countryCode = ?"
            params.append(country_code)
        cursor.execute(query, tuple(params))
        result = cursor.fetchone()
        return result[0] if result else 0
    except Exception as e:
        print("Error in get_total_distinct_water_bodies:", e)
        return None

def get_record_count_by_category(cursor, country_code=None):
    """
    Return a list of tuples with water body category and the count of records
    in that category, optionally filtered by country.
    """
    try:
        query = """
            SELECT parameterWaterBodyCategory, COUNT(*) AS recordCount
            FROM T_WISE6_AggregatedDataByWaterBody
            WHERE metadata_observationStatus != 'V'
            AND 1=1
        """
        params = []
        if country_code is not None:
            query += " AND countryCode = ?"
            params.append(country_code)
        query += " GROUP BY parameterWaterBodyCategory"
        cursor.execute(query, tuple(params))
        return cursor.fetchall()
    except Exception as e:
        print("Error in get_record_count_by_category:", e)
        return None

def get_water_body_measurements(cursor, country_code=None):
    """
    For each water body, compute the average measurement value and the average standard deviation,
    optionally filtered by country.
    """
    try:
        query = """
            SELECT waterBodyIdentifier,
                   AVG(resultMeanValue) AS avgMean,
                   AVG(resultStandardDeviationValue) AS avgStdDev
            FROM T_WISE6_AggregatedDataByWaterBody
            WHERE resultMeanValue IS NOT NULL AND resultStandardDeviationValue IS NOT NULL
            AND metadata_observationStatus != 'V'
            AND 1=1
        """
        params = []
        if country_code is not None:
            query += " AND countryCode = ?"
            params.append(country_code)
        query += " GROUP BY waterBodyIdentifier ORDER BY waterBodyIdentifier"
        cursor.execute(query, tuple(params))
        return cursor.fetchall()
    except Exception as e:
        print("Error in get_water_body_measurements:", e)
        return None

def get_chemical_statistics(cursor, country_code=None):
    """
    For each chemical (observedPropertyDeterminandLabel), compute:
      - Total number of samples,
      - Average measurement value,
      - Minimum and maximum observed values,
      - Total number of monitoring sites (summing Class1...Class5 counts),
    optionally filtered by country.
    """
    try:
        query = """
            SELECT observedPropertyDeterminandLabel,
                   SUM(resultNumberOfSamples) AS totalSamples,
                   AVG(resultMeanValue) AS avgMeanValue,
                   MIN(resultMinimumValue) AS minValue,
                   MAX(resultMaximumValue) AS maxValue,
                   SUM(
                       resultNumberOfSitesClass1 +
                       resultNumberOfSitesClass2 +
                       resultNumberOfSitesClass3 +
                       resultNumberOfSitesClass4 +
                       resultNumberOfSitesClass5
                   ) AS totalSites
            FROM T_WISE6_AggregatedDataByWaterBody
            WHERE metadata_observationStatus != 'V'
            AND 1=1
        """
        params = []
        if country_code is not None:
            query += " AND countryCode = ?"
            params.append(country_code)
        query += " GROUP BY observedPropertyDeterminandLabel ORDER BY totalSamples DESC"
        cursor.execute(query, tuple(params))
        return cursor.fetchall()
    except Exception as e:
        print("Error in get_chemical_statistics:", e)
        return None

def get_time_series_stats(cursor, country_code=None):
    """
    Return average measurement values over time broken down by water body category.
    This shows how the average resultMeanValue changes per sampling year.
    """
    try:
        query = """
            SELECT phenomenonTimeReferenceYear,
                   parameterWaterBodyCategory,
                   AVG(resultMeanValue) AS avgMeanValue
            FROM T_WISE6_AggregatedDataByWaterBody
            WHERE phenomenonTimeReferenceYear IS NOT NULL
            AND metadata_observationStatus != 'V'
            AND 1=1
        """
        params = []
        if country_code is not None:
            query += " AND countryCode = ?"
            params.append(country_code)
        query += """
            GROUP BY phenomenonTimeReferenceYear, parameterWaterBodyCategory
            ORDER BY phenomenonTimeReferenceYear, parameterWaterBodyCategory
        """
        cursor.execute(query, tuple(params))
        return cursor.fetchall()
    except Exception as e:
        print("Error in get_time_series_stats:", e)
        return None


def get_total_samples(cursor, country_code=None):
    """
    Return the total number of samples from resultNumberOfSamples.
    """
    try:
        query = "SELECT SUM(resultNumberOfSamples) FROM T_WISE6_AggregatedData WHERE 1=1"
        params = []
        if country_code is not None:
            query += " AND countryCode = ?"
            params.append(country_code)
        cursor.execute(query, tuple(params))
        result = cursor.fetchone()
        return result[0] if result and result[0] is not None else 0
    except Exception as e:
        print("Error in get_total_samples:", e)
        return None

def get_proportion_below_loq(cursor, country_code=None):
    """
    Calculate the percentage of samples below the LOQ.
    This is computed as:
      (SUM(resultQualityNumberOfSamplesBelowLOQ) / SUM(resultNumberOfSamples)) * 100
    """
    try:
        query = """
            SELECT CASE 
                     WHEN SUM(resultNumberOfSamples) > 0
                     THEN (SUM(resultQualityNumberOfSamplesBelowLOQ) * 1.0 / SUM(resultNumberOfSamples)) * 100
                     ELSE 0
                   END AS belowLOQPct
            FROM T_WISE6_AggregatedData
            WHERE 1=1
        """
        params = []
        if country_code is not None:
            query += " AND countryCode = ?"
            params.append(country_code)
        cursor.execute(query, tuple(params))
        result = cursor.fetchone()
        return result[0] if result and result[0] is not None else 0
    except Exception as e:
        print("Error in get_proportion_below_loq:", e)
        return None

def get_missing_data_percentage(cursor, country_code=None):
    """
    Calculate the percentage of records considered missing based on resultObservationStatus.
    We consider statuses 'L', 'M', 'N', 'O', 'W', 'X', 'Y' as missing.
    """
    try:
        query_total = "SELECT COUNT(*) FROM T_WISE6_AggregatedData WHERE 1=1"
        query_missing = """
            SELECT COUNT(*) FROM T_WISE6_AggregatedData 
            WHERE resultObservationStatus IN ('L','M','N','O','W','X','Y') AND 1=1
        """
        params_total = []
        params_missing = []
        if country_code is not None:
            query_total += " AND countryCode = ?"
            query_missing += " AND countryCode = ?"
            params_total.append(country_code)
            params_missing.append(country_code)
        cursor.execute(query_total, tuple(params_total))
        total = cursor.fetchone()[0]
        cursor.execute(query_missing, tuple(params_missing))
        missing = cursor.fetchone()[0]
        return (missing / total) * 100 if total > 0 else 0
    except Exception as e:
        print("Error in get_missing_data_percentage:", e)
        return None

def get_chemical_stats_above_loq(cursor, country_code=None):
    """
    Return aggregated statistics for each chemical (observedPropertyDeterminandLabel)
    considering only records with mean values above the LOQ (resultQualityMeanBelowLOQ = 0).
    
    Returns for each chemical:
      - Total number of samples
      - Average of resultMeanValue
      - Minimum and maximum observed values
      - Average standard deviation
    """
    try:
        query = """
            SELECT observedPropertyDeterminandLabel,
                   SUM(resultNumberOfSamples) AS totalSamples,
                   AVG(resultMeanValue) AS avgMean,
                   MIN(resultMinimumValue) AS minVal,
                   MAX(resultMaximumValue) AS maxVal,
                   AVG(resultStandardDeviationValue) AS avgStdDev
            FROM T_WISE6_AggregatedData
            WHERE resultQualityMeanBelowLOQ = 0
        """
        params = []
        if country_code is not None:
            query += " AND countryCode = ?"
            params.append(country_code)
        query += " GROUP BY observedPropertyDeterminandLabel ORDER BY totalSamples DESC"
        cursor.execute(query, tuple(params))
        return cursor.fetchall()
    except Exception as e:
        print("Error in get_chemical_stats_above_loq:", e)
        return None

def get_weighted_class_distribution(cursor, country_code=None):
    """
    For each chemical (observedPropertyDeterminandLabel), calculate:
      - The raw total monitoring sites, as the sum of the five class counts.
      - A weighted score based on pre-defined weights:
          * Class 1: 1.0
          * Class 2: 0.8
          * Class 3: 0.6
          * Class 4: 0.4
          * Class 5: 0.2
    The weights reflect that higher classes are "better" (i.e. more reliable).
    If a class count is NULL, it is treated as 0.
    
    Returns:
        A list of tuples:
        (observedPropertyDeterminandLabel, raw_total, weighted_score)
    """
    try:
        query = """
            SELECT observedPropertyDeterminandLabel,
                   SUM(
                       COALESCE(resultNumberOfSitesClass1, 0) +
                       COALESCE(resultNumberOfSitesClass2, 0) +
                       COALESCE(resultNumberOfSitesClass3, 0) +
                       COALESCE(resultNumberOfSitesClass4, 0) +
                       COALESCE(resultNumberOfSitesClass5, 0)
                   ) AS raw_total,
                   SUM(
                       COALESCE(resultNumberOfSitesClass1, 0) * 1.0 +
                       COALESCE(resultNumberOfSitesClass2, 0) * 0.8 +
                       COALESCE(resultNumberOfSitesClass3, 0) * 0.6 +
                       COALESCE(resultNumberOfSitesClass4, 0) * 0.4 +
                       COALESCE(resultNumberOfSitesClass5, 0) * 0.2
                   ) AS weightedScore
            FROM T_WISE6_AggregatedDataByWaterBody
            WHERE 1=1
        """
        params = []
        if country_code is not None:
            query += " AND countryCode = ?"
            params.append(country_code)
        query += " GROUP BY observedPropertyDeterminandLabel ORDER BY weightedScore DESC"
        cursor.execute(query, tuple(params))
        return cursor.fetchall()
    except Exception as e:
        print("Error in get_weighted_class_distribution:", e)
        return None


def close_connection(conn):
    """Close the database connection."""
    try:
        conn.close()
    except Exception as e:
        print("Error closing connection:", e)

def main():
    conn, cursor = connect_to_db()
    if conn is None or cursor is None:
        return

    # Set a specific country code (e.g., "BE") or None to include all countries
    country_code = "BE" # Change or set to None as needed

    distinct_water_bodies = get_total_distinct_water_bodies(cursor, country_code)
    print(f"Total distinct water bodies: {distinct_water_bodies}")

    records_by_category = get_record_count_by_category(cursor, country_code)
    print("\nRecord count by water body category:")
    if records_by_category:
        for category, count in records_by_category:
            print(f"   Category '{category}': {count} records")
    else:
        print("No data found.")

    water_body_measurements = get_water_body_measurements(cursor, country_code)
    print("\nWater body measurements (first 10):")
    if water_body_measurements:
        for row in water_body_measurements[:10]:
            print(f"   WaterBodyID: {row[0]}, Avg Mean: {row[1]:.5f}, Avg StdDev: {row[2]:.5f}")
    else:
        print("No data found.")

    chemical_stats = get_chemical_statistics(cursor, country_code)
    print("\nChemical statistics (first 10):")
    if chemical_stats:
        for row in chemical_stats[:10]:
            print(f"   Chemical: {row[0]}, Total Samples: {row[1]}, Avg Mean: {row[2]:.5f}, "
                  f"Min: {row[3]}, Max: {row[4]}, Total Sites: {row[5]}")
    else:
        print("No data found.")

    time_series = get_time_series_stats(cursor, country_code)
    print("\nTime series stats (first 10):")
    if time_series:
        for row in time_series[:10]:
            print(f"   Year: {row[0]}, Category: {row[1]}, Avg Mean Value: {row[2]:.5f}")
    else:
        print("No data found.")

    toatl_chemicals_monitored = get_total_chemicals_monitored(cursor, country_code)
    print(f"Total distinct chemicals monitored : {toatl_chemicals_monitored}")

    total_monitoring_sites = get_total_monitoring_sites(cursor, country_code)
    print(f"Total distinct monitoring sites : {total_monitoring_sites}")

    total_monitoring_sites_from_spatial_table = get_total_monitoring_sites_from_spatial_table(cursor, country_code)
    print(f"Total distinct monitoring sites from spatial table : {total_monitoring_sites_from_spatial_table}")


    total_samples = get_total_samples(cursor, country_code)
    print(f"Total samples: {total_samples}")
    
    prop_below_loq = get_proportion_below_loq(cursor, country_code)
    print(f"Proportion below LOQ: {prop_below_loq:.2f}%")
    
    missing_pct = get_missing_data_percentage(cursor, country_code)
    print(f"Missing data percentage: {missing_pct:.2f}%")
    
    chem_stats = get_chemical_stats_above_loq(cursor, country_code)
    print("\nChemical statistics (records with mean above LOQ):")
    if chem_stats:
        for row in chem_stats[:10]:
            print(f"  Chemical: {row[0]}, Total Samples: {row[1]}, "
                  f"Avg Mean: {row[2]:.5f}, Min: {row[3]}, Max: {row[4]}, "
                  f"Avg StdDev: {row[5]:.5f}")
    else:
        print("No chemical statistics available.")
    
    weighted_results = get_weighted_class_distribution(cursor, country_code)
    
    print("\n=== Weighted Class Distribution (per Chemical) ===")
    if weighted_results:
        print("Chemical Name | Raw Monitoring Sites | Weighted Score")
        print("-------------------------------------------------------")
        for row in weighted_results:
            chemical = row[0]
            raw_total = row[1]
            weighted_score = row[2]
            print(f"{chemical:30s} | {raw_total:>6}              | {weighted_score:>6.2f}")
    else:
        print("No weighted class distribution data available.")

    close_connection(conn)

if __name__ == "__main__":
    main()
