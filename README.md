# Bluelab Connect

Install the [Bluelab Connect Software](https://www.bluelab.com/products/type/connect/connect-software)

```
gardnr add metric water electro-conductivity ec
gardnr add metric water ph ph
gardnr add metric water temperature water-temp

gardnr add driver bluelab-connect bluelab_connect.driver:BluelabConnect -c log_file="log.csv" -cec_metric=ec -c ph_metric=ph -c temp_metric=water-temp
```
