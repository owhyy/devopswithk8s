#!/usr/bin/env python

import uuid
from datetime import timezone, datetime
import time


def run(value):
    print(f"{datetime.now(timezone.utc).isoformat()}: {value}")
    time.sleep(5)

if __name__ == "__main__":
    value = uuid.uuid4()
    while True:
        run(value)
