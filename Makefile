

certification_history.csv : certifications.csv
	python scripts/history.py $< > tmp
	mv tmp $@

certifications.csv :
	python scripts/fetch.py | csvsort > $@
