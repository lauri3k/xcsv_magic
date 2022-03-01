<!doctype html>
<html>
<head>
    <title>csv_magic</title>
    
    <script>const base_url = "{{ base_url }}"</script>
    <script type="text/javascript" src="{{ base_url }}/csv_magic/static/js/papaparse.min.js"></script>
    <script type="text/javascript" src="{{ base_url }}/csv_magic/static/js/csv.js"></script>
</head>
<body>
     <form id="form">
        <input
            type="file"
            id="file"
            required="required"
            accept=".csv"
            onchange="readCsv(this)"
			/>
        <input type="submit" value="Download" disabled="true" id="button" />
    </form>
</body>
</html>