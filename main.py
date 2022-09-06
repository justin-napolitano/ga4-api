from xml.sax.handler import property_interning_dict
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta import BetaAnalyticsDataAsyncClient
from google.analytics.data_v1beta import BatchRunReportsRequest
from google.analytics.data_v1beta.types import DateRange
from google.analytics.data_v1beta.types import Dimension
from google.analytics.data_v1beta.types import Metric
from google.analytics.data_v1beta.types import RunReportRequest

import os
import logging
from datetime import datetime
import yaml


'''Request Documentation

property
A Google Analytics GA4 property identifier whose events are tracked. Specified in the URL path and not the body. To learn more, see where to find your Property ID. Within a batch request, this property should either be unspecified or consistent with the batch-level property.

Example: properties/1234

Type
str

dimensions
The dimensions requested and displayed.

Type
Sequence[google.analytics.data_v1beta.types.Dimension]

metrics
The metrics requested and displayed.

Type
Sequence[google.analytics.data_v1beta.types.Metric]

date_ranges
Date ranges of data to read. If multiple date ranges are requested, each response row will contain a zero based date range index. If two date ranges overlap, the event data for the overlapping days is included in the response rows for both date ranges. In a cohort request, this dateRanges must be unspecified.

Type
Sequence[google.analytics.data_v1beta.types.DateRange]

dimension_filter
Dimension filters allow you to ask for only specific dimension values in the report. To learn more, see Fundamentals of Dimension Filters for examples. Metrics cannot be used in this filter.

Type
google.analytics.data_v1beta.types.FilterExpression

metric_filter
The filter clause of metrics. Applied at post aggregation phase, similar to SQL having-clause. Dimensions cannot be used in this filter.

Type
google.analytics.data_v1beta.types.FilterExpression

offset
The row count of the start row. The first row is counted as row 0.

When paging, the first request does not specify offset; or equivalently, sets offset to 0; the first request returns the first limit of rows. The second request sets offset to the limit of the first request; the second request returns the second limit of rows.

To learn more about this pagination parameter, see Pagination.

Type
int

limit
The number of rows to return. If unspecified, 10,000 rows are returned. The API returns a maximum of 100,000 rows per request, no matter how many you ask for. limit must be positive.

The API can also return fewer rows than the requested limit, if there aren’t as many dimension values as the limit. For instance, there are fewer than 300 possible values for the dimension country, so when reporting on only country, you can’t get more than 300 rows, even if you set limit to a higher value.

To learn more about this pagination parameter, see Pagination.

Type
int

metric_aggregations
Aggregation of metrics. Aggregated metric values will be shown in rows where the dimension_values are set to “RESERVED_(MetricAggregation)”.

Type
Sequence[google.analytics.data_v1beta.types.MetricAggregation]

order_bys
Specifies how rows are ordered in the response.

Type
Sequence[google.analytics.data_v1beta.types.OrderBy]

currency_code
A currency code in ISO4217 format, such as “AED”, “USD”, “JPY”. If the field is empty, the report uses the property’s default currency.

Type
str

cohort_spec
Cohort group associated with this request. If there is a cohort group in the request the ‘cohort’ dimension must be present.

Type
google.analytics.data_v1beta.types.CohortSpec

keep_empty_rows
If false or unspecified, each row with all metrics equal to 0 will not be returned. If true, these rows will be returned if they are not separately removed by a filter.

Type
bool

return_property_quota
Toggles whether to return the current state of this Analytics Property’s quota. Quota is returned in PropertyQuota.

Type
bool'''







async def sample_batch_run_reports(property_id):
    ''' Run batch report requests for one property id '''
    '''
    https://googleapis.dev/python/analyticsdata/latest/data_v1beta/beta_analytics_data.html
    async batch_run_reports(request: Optional[Union[google.analytics.data_v1beta.types.analytics_data_api.BatchRunReportsRequest, dict]] = None, *,
    retry: Union[google.api_core.retry.Retry, google.api_core.gapic_v1.method._MethodDefault] = <_MethodDefault._DEFAULT_VALUE: <object object>>, 
    timeout: Optional[float] = None, metadata: Sequence[Tuple[str, str]] = ())'''
    report_list = [RunReportRequest(
        property=f"properties/{property_id}",
        dimensions=[Dimension(name="city")],
        metrics=[Metric(name="activeUsers")],
        date_ranges=[DateRange(start_date="2020-03-31", end_date="today")],
    ), RunReportRequest(
        property=f"properties/{property_id}",
        dimensions=[Dimension(name="city")],
        metrics=[Metric(name="activeUsers")],
        date_ranges=[DateRange(start_date="2020-03-31", end_date="today")],
    )]
    # Create a client
    client = BetaAnalyticsDataAsyncClient(report_list)

    # Initialize request argument(s)
    request = BatchRunReportsRequest()

    # Make the request
    response = await client.batch_run_reports(request=request)

    # Handle the response
    print(response)

def run_standard_report(property_id):

    """
        **Sample Request**  
        https://developers.google.com/analytics/devguides/reporting/data/v1/api-schema
        SAMPLE_REQUST = RunReportRequest(
        property=f"properties/{property_id}",
        dimensions=[Dimension(name="city"), Dimension(name=), Dimension(name=)],
        metrics=[Metric(name="activeUsers")],
        date_ranges=[DateRange(start_date="2020-03-31", end_date="today")],
    )

    """ 
   
    """Runs a simple report on a Google Analytics 4 property."""

    # TODO(developer): Uncomment this variable and replace with your
    #  Google Analytics 4 property ID before running the sample.
    # property_id = "YOUR-GA4-PROPERTY-ID"

    # Using a default constructor instructs the client to use the credentials
    # specified in GOOGLE_APPLICATION_CREDENTIALS environment variable.
    client = BetaAnalyticsDataClient()

    request = RunReportRequest(
        property=f"properties/{property_id}",
        dimensions=[Dimension(name="city")],
        metrics=[Metric(name="activeUsers")],
        date_ranges=[DateRange(start_date="2020-03-31", end_date="today")],
    )
    response = client.run_report(request)

    #print("Report result:")
    #for row in response.rows:
    #    print(row.dimension_values[0].value, row.metric_values[0].value)
    return response

def print_run_report_response(response):
    """Prints results of a runReport call."""
    print(f"{response.row_count} rows received")
    for dimensionHeader in response.dimension_headers:
        print(f"Dimension header name: {dimensionHeader.name}")
    for metricHeader in response.metric_headers:
        metric_type = MetricType(metricHeader.type_).name
        print(f"Metric header name: {metricHeader.name} ({metric_type})")

    print("Report result:")
    for row in response.rows:
        for dimension_value in row.dimension_values:
            print(dimension_value.value)

        for metric_value in row.metric_values:
            print(metric_value.value)

def set_os_environ(creds_file):
    try: 
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = creds_file
        logging.debug("GOOGLE_APPLICATION_CREDENTIALS set to {}".format(creds_file))
    except Exception as e: 
        logging.exception(e)
        raise(e)
        
def set_logging():
    #dt = datetime.now()
    #log_file = dt.strftime("%d-%m-%Y:%H:%M:%S") + ".log"
    log_file = "test.log"
    #print(log_file)
    logging.basicConfig(filename=log_file, 
        encoding='utf-8', 
        level=logging.DEBUG,
        format='%(asctime)s %(levelname)-8s %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S')

def load_config(conf_file):
    #returns a dictionary
    with open(conf_file, "r") as stream:
        try:
            conf = yaml.safe_load(stream)
            logging.debug("config data {}".format(conf))
        except yaml.YAMLError as e:
            logging.error(e)
    return conf

def main():
    #creds ="creds.json"
    conf_file ="config.yaml"
    report_dict = {}
    set_logging()
    conf = load_config(conf_file)
    set_os_environ(conf["creds"])


    for id in conf["properties"]:
        report_dict[id] = run_standard_report(id)
        
# to do for alpha
"""
* enable google data api
*Authorization
* cred.json
* Test a standard report with all properties
"""

# to do for beta

'''
* Make conf a class
* change name to job or service
* make each function a method
* service.init
    loads config
* service.run_standard_report(default = props in config... or props =, dimensions = standard in yaml, oor , and so on)
* service.run_batch_reports
.'''

if __name__ == "__main__":
    main()