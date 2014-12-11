def stub_log_error(exc):
    raise RuntimeError("Could not log error")

try:
    1 / 0
except Exception as e:
    try:
        stub_log_error(e)
    except:
        pass
    raise
