#!/bin/bash
find ./arma2oa/33930/steamapps/workshop/content/33930/ -depth -name "*[A-Z]*" -print0 |\
 xargs -0 -I {} bash -c "mv \"{}\" \"\`echo \"{}\" | sed 's,\(.*\)\/\(.*\),\1\/\L\2,'\`\"";\
 cd ./arma2oa/33930 &&\
 find ./steamapps/workshop/content/33930 -maxdepth 1 -mindepth 1 -type d -exec ln -sf -t ./ {} +
exit 0