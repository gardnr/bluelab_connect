import csv
import pickle
from datetime import datetime

from gardnr import drivers, logger, metrics


class BluelabConnect(drivers.Sensor):

    def setup(self):
        self.pickle_file_name = 'bluelab-connect-line-count.pickle'

    def read(self):
        line_count = self.get_line_count()

        with open(self.log_file) as csv_file:
            reader = csv.reader(csv_file, delimiter=',')

            # skip the header line
            next(reader)

            # skip past all the lines already read
            # NOTE: could cause StopIteration if file got truncated
            for _ in range(line_count):
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

                line_count += 1

        self.set_line_count(line_count)

    def get_line_count(self):
        try:
            with open(self.pickle_file_name, 'rb') as pickle_file:
                return pickle.load(pickle_file)
        except (OSError, IOError) as e:
            return 0

    def set_line_count(self, line_count):
        with open(self.pickle_file_name, 'wb') as pickle_file:
            pickle.dump(line_count, pickle_file)
