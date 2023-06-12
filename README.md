This repository is meant for extending Tipply website functionality. Tipply offers streamers a way to get donations from their fans. The website doesn't have any webhook functionality, that might be handy to have some IRL display of donations.

# How does this work
Python script watches donation alert page (the same one that's used in OBS to display donations on stream) and when it notices any changes it fires request to URL specified via .env file