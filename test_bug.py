from validator import valid_port
import sys
# Automated validation test
if valid_port(80) and valid_port(443) and not valid_port(70000):
    print("TEST OK")
    sys.exit(0)

print("TEST FAILED")
sys.exit(1)