import csv
from datetime import datetime

from gardnr import drivers, logger, metrics


class BluelabConnect(drivers.Sensor):

    def setup(self):
        pass

    def read(self):
        with open(self.log_file) as csv_file:
            reader = csv.reader(csv_file, delimiter=',')

            # skip the header line
            next(reader)

            for row in reader:
                timestamp = datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S')
                ec = float(row[3])
                ph = float(row[4])
                temp = float(row[5])

                metrics.create_metric_log(self.ec_metric, ec,
                                          timestamp=timestamp)
                metrics.create_metric_log(self.ph_metric, ph,
                                          timestamp=timestamp)
                metrics.create_metric_log(self.temp_metric, temp,
                                          timestamp=timestamp)
