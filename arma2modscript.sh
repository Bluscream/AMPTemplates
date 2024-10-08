#!/bin/bash
find ./arma2/33905/steamapps/workshop/content/33900/ -depth -name "*[A-Z]*" -print0 |
	xargs -0 -I {} bash -c "mv \"{}\" \"\`echo \"{}\" | sed 's,\(.*\)\/\(.*\),\1\/\L\2,'\`\""
cd ./arma2/33905 &&
	find ./steamapps/workshop/content/33900 -maxdepth 1 -mindepth 1 -type d -exec ln -sf -t ./ {} +
exit 0
