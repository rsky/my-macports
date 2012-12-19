PHP_FPM_TEMPLATE = templates/www/opt-php-fpm/Portfile.in
PHP_FPM_PORTFILE = macports/www/opt-php-fpm/Portfile
PHP53_FPM_PORTFILE = macports/www/opt-php53-fpm/Portfile
PHP54_FPM_PORTFILE = macports/www/opt-php54-fpm/Portfile
PHP_FPM_PORTFILES = $(PHP_FPM_PORTFILE) $(PHP53_FPM_PORTFILE) $(PHP54_FPM_PORTFILE)
ALL_PORTFILES = $(PHP_FPM_PORTFILES)

all: $(ALL_PORTFILES)

$(PHP_FPM_PORTFILE): $(PHP_FPM_TEMPLATE)
	mkdir -p macports/www/opt-php-fpm
	cat $(PHP_FPM_TEMPLATE) | sed 's/%DIRNAME%/main/g' | sed 's/%SUFFIX%//g' > $@

$(PHP53_FPM_PORTFILE): $(PHP_FPM_TEMPLATE)
	mkdir -p macports/www/opt-php53-fpm
	cat $(PHP_FPM_TEMPLATE) | sed 's/%DIRNAME%/5.3/g' | sed 's/%SUFFIX%/53/g' > $@

$(PHP54_FPM_PORTFILE): $(PHP_FPM_TEMPLATE)
	mkdir -p macports/www/opt-php54-fpm
	cat $(PHP_FPM_TEMPLATE) | sed 's/%DIRNAME%/5.4/g' | sed 's/%SUFFIX%/54/g' > $@
