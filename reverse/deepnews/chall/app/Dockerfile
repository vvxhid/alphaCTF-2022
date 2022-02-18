FROM budtmo/docker-android-x86-10.0

COPY app-release.apk /app/app-release.apk

COPY flag.txt /flag.txt
RUN chmod 777 /flag.txt
RUN chmod o+w /

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT [ "/entrypoint.sh" ]

