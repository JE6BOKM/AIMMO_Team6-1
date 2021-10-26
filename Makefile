recreate-migration:
	# find all migration files except those in oscar: we need to preserve default oscar migrations file orders
	find . -path "*/migrations/*.py" ! -path "*/sites/*.py" ! -name "__init__.py" -delete
	pyclean -v .
