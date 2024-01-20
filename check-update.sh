#!/bin/sh
curl -L "https://download.netsurf-browser.org/netsurf/releases/source-full/" 2>/dev/null |sed -ne 's,.*netsurf-all-\(.*\).tar.gz\".*,\1,p' |tail -n1

