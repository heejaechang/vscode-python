# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
import os.path

TEST_ROOT = os.path.dirname(__file__)
SRC_ROOT = os.path.dirname(TEST_ROOT)
PROJECT_ROOT = os.path.dirname(SRC_ROOT)
IPYTHON_ROOT = os.path.join(SRC_ROOT, "ipython")
TESTING_TOOLS_ROOT = os.path.join(SRC_ROOT, "testing_tools")
DEBUG_ADAPTER_ROOT = os.path.join(SRC_ROOT, "debug_adapter")

PYTHONFILES = os.path.join(SRC_ROOT, "lib", "python")
REQUIREMENTS = os.path.join(PROJECT_ROOT, "requirements.txt")
