# Running Outside Window

Keep the repository in its own virtual environment. On an always-on machine, use
your operating system's scheduler to run the collector every 15 minutes. Supply
the webhook and any provider credentials in that job's environment, not in command
arguments. Local CSV/ICS inputs, when used, must be refreshed separately.

## Linux systemd example

The supplied units assume an existing dedicated `trmnl` user and installation in
`/opt/trmnl-outside-window`, including its `.venv`. Keep the code read-only to that user and give
it ownership of `private/` with mode 700 and its files with mode 600. Create
`private/config.json` and `private/collector.env` locally. The latter uses `NAME=value`
lines without `export`, including `TRMNL_WEBHOOK_URL` and required source credentials.

```sh
sudo cp deploy/trmnl-outside-window.service deploy/trmnl-outside-window.timer /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable --now trmnl-outside-window.timer
sudo systemctl start trmnl-outside-window.service
sudo systemctl status trmnl-outside-window.service
```

These are deployment examples, not services already installed on your machine.
Check service failures and the timestamp on the display. Rotate a leaked webhook
URL in TRMNL and update the local environment file. Never commit private files.
