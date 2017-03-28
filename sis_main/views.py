from django.http import HttpResponse


HTML = """
<!DOCTYPE html>
<html lang = "es">
	<head>
		<meta charset = "UTF-8">
		<title> Hola Mundo </title>
		<meta http - equiv = "content-type" content = "text/html; charset=utf-8">
		<meta name = "robots" content = "NONE,NOARCHIVE">
		<style type = "text/css" media = "screen">
			html * {padding: 0; margin: 0; }
			body * {padding: 10px 20px; }
			body ** {padding: 0; }
			body {font: small sans-serif; }
			body > div {border - bottom: 1px solid  # ddd;}
			h1 {font-weight: normal; }
			#summary {background: #e0ebff}
		</style>
	</head>
	<body>
		<div id = "summary">
			<h1> ¡Hola Mundo!</h1>
		</div>
	</body>
</html>"""

def hola(request):
    return HttpResponse(HTML)