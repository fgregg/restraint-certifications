

certification_history.csv : certifications.csv
	python scripts/history.py $< > $@

certifications.csv :
	python scripts/fetch.py | csvsort > $@
