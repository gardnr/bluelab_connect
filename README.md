# Bluelab Connect

Install the [Bluelab Connect Software](https://www.bluelab.com/products/type/connect/connect-software)

```
gardnr add metric water electro-conductivity ec
gardnr add metric water ph ph
gardnr add metric water temperature water-temp

gardnr add driver bluelab-connect bluelab_connect.driver:BluelabConnect -c log_file="log.csv" -c ec_metric=ec -c ph_metric=ph -c temp_metric=water-temp
```

The `log_file` config is the CSV file that Bluelab Connect Software logs to. Check under _Settings -> Data logging -> Log data directory_ to find where the log file is. Then, look in that directory to find the name of the file. Set log_file to the full path to the log file (directory and filename). Optionally, `pickle_file_name` config to set the name of the pickle file to keep track of the log file state.
