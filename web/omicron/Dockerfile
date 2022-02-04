FROM php:7.3-alpine
COPY files /tmp/

RUN apk add --update --no-cache apache2 mysql mysql-client php7-apache2 php7-phar php7-session php7-mysqli php7-zip php7-gd php7-json php7-tokenizer php7-pdo php7-pdo_mysql curl zip  \
    && cp /tmp/my.cnf /etc/mysql/my.cnf \
    && mv /tmp/my.cnf /etc/my.cnf \
    && mv /tmp/mariadb-server.cnf /etc/my.cnf.d/mariadb-server.cnf \
    && mysql_install_db --user=mysql --datadir=/var/lib/mysql \
    && sh -c 'mysqld_safe &' \
	&& sleep 3s \
    && mysqladmin -uroot password 'vvxhid1337' \
    && mysql -e "source /tmp/db.sql;" -uroot -pvvxhid1337 \
    && mv /tmp/docker-php-entrypoint /usr/local/bin/docker-php-entrypoint \
    && mv /tmp/httpd.conf /etc/apache2/httpd.conf \
    && mv /tmp/src/* /tmp/src/.env /tmp/src/.styleci.yml /var/www/html \
    && chmod -R 755 /var/www/html \
    && chmod -R 775 /var/www/html/storage \
    && chown -R root:www-data /var/www/html \
    && rm -rf /tmp/* 
    # && rm -rf /etc/apk

RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

WORKDIR /var/www/html
RUN composer install
RUN php artisan key:generate
EXPOSE 80

VOLUME ["/var/log/apache2"]

CMD ["/bin/sh", "-c", "docker-php-entrypoint"]
