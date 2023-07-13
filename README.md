# Nivalty

### Install uvicorn

- For ubuntu

```shell
sudo apt install python-uvicorn
```

- For fedora

```shell
sudo dnf install python-uvicorn
```

- Using pip

```shell
pip install uvicorn
```

### Run node of blockchain

```shell
uvicorn node:app
```

```shell
INFO:     Started server process [163692]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

And then send a request

```shell
curl http://127.0.0.1:8000/last_block
```

Result:

```json
{
  "block_id": 0,
  "prev_hash": "0",
  "data": [],
  "timestamp": 1689275524
}
```
