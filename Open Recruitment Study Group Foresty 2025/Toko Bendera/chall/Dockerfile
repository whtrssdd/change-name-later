FROM php:7-alpine

# update package list and install dependencies
RUN apk update && \
	apk add --no-cache \
	libpng-dev \
	libjpeg-turbo-dev \
	libwebp-dev \
	libxpm-dev \
	freetype-dev \
	zip \
	unzip \
	wget

RUN docker-php-ext-configure gd --with-freetype \
	--with-jpeg \
	--with-webp \
	--with-xpm

# Use production environment
RUN mv $PHP_INI_DIR/php.ini-production $PHP_INI_DIR/php.ini

# Install PHP extensions
RUN docker-php-ext-install gd -j$(nproc)

WORKDIR /app

# Install dompdf
RUN ["wget", "https://github.com/dompdf/dompdf/releases/download/v1.2.0/dompdf_1-2-0.zip", "-O", "dompdf.zip"]
RUN ["unzip", "dompdf.zip"]
RUN ["rm", "dompdf.zip"]

RUN adduser -u 1000 ctf -D  && \
	chown -R ctf:ctf /app && \
	chmod -R 500 /app && \
	chmod -R 777 /app/dompdf/lib/fonts && \
	chmod -R 555 /app/dompdf/lib/fonts/dompdf_font_family_cache.dist.php

USER ctf

COPY ./src /app
COPY ./flag.txt /flag.txt

ENV PORT 80

EXPOSE 80
CMD ["sh", "-c", "ulimit -t 5 && php -S 0.0.0.0:80"]
