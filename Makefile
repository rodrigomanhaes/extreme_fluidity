all: test

deps: specloud should-dsl fluidity

specloud:
	@python -c 'import specloud' 2>/dev/null || pip install --no-deps specloud -r http://github.com/hugobr/specloud/raw/master/requirements.txt

should-dsl:
	@python -c 'import should_dsl' 2>/dev/null || pip install http://github.com/hugobr/should-dsl/tarball/master

fluidity:
	@python -c 'import fluidity' 2>/dev/null || pip install http://github.com/nsi-iff/fluidity/tarball/master

test: deps
	@echo =======================================
	@echo ========= Running unit specs ==========
	@specloud spec
	@echo

