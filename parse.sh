curl 'https://dom.gosuslugi.ru/interactive-reports/api/rest/services/commonMetersReport/table' \
  -H 'Content-Type: application/json;charset=UTF-8' \
  --data-binary '{"withFederalDistricts":false,"serviceType":"COLD_WATER","territories":[],"territoryCategory":"ADMINISTRATIVE","operationYearFrom":1700,"operationYearTo":2020}'